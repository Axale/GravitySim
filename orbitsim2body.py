
import pygame as game
import sys as sys

timestep = 1

class MassObject:

    def __init__(self, location, velocity, mass):
        self.location = game.Vector2(location)
        self.white = game.Color(255, 255, 255)
        self.velocity = game.Vector2(velocity)
        self.mass = mass

    def Draw(self, displayscreen):
        game.draw.circle(displayscreen, self.white, self.location, 5, width=0)

    def RelVects(self, Onex, Oney):
        self.relvect = game.Vector2((Onex - self.location.x, Oney - self.location.y))
        self.normrelvect = self.relvect.normalize()

    def Move(self):
        self.location.x += self.velocity.x * timestep + .5 * self.accel.x * (timestep ** 2)
        self.location.y += self.velocity.y * timestep + .5 * self.accel.y * (timestep ** 2)
        self.velocity.x += self.accel.x * timestep
        self.velocity.y += self.accel.y * timestep

    def CalcMove(self, MassOne):
        Accel = ((MassOne))/(self.relvect.magnitude()**2)
        self.accel = game.Vector2(self.normrelvect.x * Accel, self.normrelvect.y * Accel)
        



def main():
    game.init() 
    black = game.Color(0, 0, 0)
    
    displayscreen = game.display.set_mode((1200, 800))
    displayscreen.fill(black)
    Fixed = MassObject((450, 400), (0, -.25), 100)
    Moving = MassObject((750, 400), (0, .25), 100)
    Fixed.Draw(displayscreen)
    Moving.Draw(displayscreen)
    game.display.flip()

    while 1:
        for event in game.event.get():
            if event.type == game.QUIT: sys.exit()

        displayscreen.fill(black)

        Moving.RelVects(Fixed.location.x, Fixed.location.y)
        Fixed.RelVects(Moving.location.x, Moving.location.y)

        Fixed.CalcMove(Moving.mass)
        Moving.CalcMove(Fixed.mass)

        Moving.Move()
        Fixed.Move()

        Fixed.Draw(displayscreen)
        Moving.Draw(displayscreen)
        game.display.flip()




if __name__ == "__main__":
    main()