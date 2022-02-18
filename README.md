# GravitySim
Just an Gravitational Model I made for fun and practice with python and physics. Also introduced me to Python OOP and PyGame.
Not meant to be a tool for scientific study.

  Hello! I made this over the span of a few days, just as a fun activity. It definitely took a bit more time than I was expecting since the simulation didn't work perfectly once I started doing the three body version, but now it works pretty well (with the right starting conditions).
  
At the same time, this simulation isn't going to be the most perfectly accurate simulation, anyways. This is due to that fact that I just used the kinematic equation for position, rather than doing out the differential equations. This was mainly a side project, so I didn't want to spend too much time on it while school is going.
I don't even use the gravitation constant G here, since the model is is not meant to be a tool for scientific study and I didn't want to have to calculate large masses.

This is slowly becoming an exercise in mathematics than it is an exercise of programming, but that's fine. Will continue work over Spring Break, got nothing else to do.

Default Start:
Masses are 75
Each mass starts 50 pixels away from the center of the window
Each mass is 120 degrees away from eachother
Each mass has a velocity of a magnitude of 1, perpendicular to the line between the mass and the center of the screen

Todo:

~~Write C++ file to speed up simulation generation~~ *
  
  Clean up and comment existing python code, as well as optimize it
  
  Give each mass a different color
  
  Replace Kinematic Equation with Runge-Kutta method
  
  Consolidate Write and Visualization files, to make it a bit more seamless.

* C++ has trouble with decimals, it seems, which means that it wouldn't be good with what I am using it for. Maybe I'll try increasing scale and see how that turns out.
