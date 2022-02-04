#include <iostream>
#include <fstream>
#include <cmath>

long double const TIMESTEP = .01;
using namespace std;

class MassObject{
	public:
	long double location[2], velocity[2], accel[2], relvectors[4];
	int mass;

	MassObject(long double locationx, long double locationy, long double velocityx, long double velocityy, int massgiven){
		location[0] = locationx;
		location[1] = locationy;
		velocity[0] = velocityx;
		velocity[1] = velocityy;
		mass = massgiven;
	}

	void RelVects(long double* OneVect, long double* TwoVect){
		relvectors[0] = location[0] - OneVect[0];
		relvectors[1] = location[1] - OneVect[1];
		relvectors[2] = location[0] - TwoVect[0];
		relvectors[3] = location[1] - TwoVect[1];
	}
	
	void Move(){
		location[0] += velocity[0] * TIMESTEP + .5 * accel[0] * (TIMESTEP * TIMESTEP);
        location[1] += velocity[1] * TIMESTEP + .5 * accel[1] * (TIMESTEP * TIMESTEP);
        velocity[0] += accel[0] * TIMESTEP;
        velocity[1] += accel[1] * TIMESTEP;
	}

	void CalcMove(int MassOne, int MassTwo){
		accel[0] = -MassOne * relvectors[0]/(pow(pow(relvectors[0], 2.0) + pow(relvectors[1], 2.0), 1.5)) - MassTwo * relvectors[2]/(pow(pow(relvectors[2], 2.0) + pow(relvectors[3], 2.0), 1.5));
    	accel[1] = -MassOne * relvectors[1]/(pow(pow(relvectors[0], 2.0) + pow(relvectors[1], 2.0), 1.5)) - MassTwo * relvectors[3]/(pow(pow(relvectors[2], 2.0) + pow(relvectors[3], 2.0), 1.5));;
	}
} ;


int main(void){
	MassObject One = MassObject(556.69873, 375, pow(3., .5) /2, -1/2, 75);
	MassObject Two = MassObject(643.30127, 375, pow(3., .5) /2, 1/2, 75);
	MassObject Three = MassObject(600, 450, -1, 0, 75);
	ofstream logs;
	logs.open("logs.txt");

	for(int i = 0; i < 1000002; i++){
		logs << One.location[0] << ' ' << One.location[1] << ' ' << Two.location[0] << ' ' <<  Two.location[1] << ' ' <<  Three.location[0] << ' ' <<  Three.location[1] << ' ';

		One.RelVects(Two.location, Three.location);
		Two.RelVects(One.location, Three.location);
		Three.RelVects(One.location, Two.location);

		One.CalcMove(Two.mass, Three.mass);
		Two.CalcMove(One.mass, Three.mass);
		Three.CalcMove(One.mass, Two.mass);
		
		One.Move();
		Two.Move();
		Three.Move();
	}
	logs.close();

	return 0;
}
