
from time import time
import pygame as game
import sys as sys

timestep = .01


class MassObject:

    def __init__(self, location, velocity, mass):
        self.location = game.Vector2(location)
        self.white = game.Color(255, 255, 255)
        self.velocity = game.Vector2(velocity)
        self.mass = mass

    def Draw(self, displayscreen):
        game.draw.circle(displayscreen, self.white, self.location, 5, width=0)

    def RelVects(self, Onex, Oney, Twox, Twoy):
        self.relvectr2 = game.Vector2((self.location.x - Onex, self.location.y - Oney))
        self.relvectr3 = game.Vector2(((self.location.x - Twox, self.location.y - Twoy)))

    def Move(self):
        self.location.x += self.velocity.x * timestep + .5 * self.accelx * (timestep ** 2)
        self.location.y += self.velocity.y * timestep + .5 * self.accely * (timestep ** 2)
        self.velocity.x += self.accelx * timestep
        self.velocity.y += self.accely * timestep

    def CalcMove(self, MassOne, MassTwo):

        self.accelx = -MassOne * self.relvectr2.x/((self.relvectr2.magnitude())**(3)) - MassTwo * self.relvectr3.x/((self.relvectr3.x**2 + self.relvectr3.y**2)**(3/2))
        self.accely = -MassOne * self.relvectr2.y/((self.relvectr2.magnitude())**(3)) - MassTwo * self.relvectr3.y/((self.relvectr3.x**2 + self.relvectr3.y**2)**(3/2))


def main():
    game.init()
    black = game.Color(0, 0, 0)
    
    displayscreen = game.display.set_mode((1200, 800))
    displayscreen.fill(black)
    Fixed = MassObject((556.69873, 375), ((3**.5)/2, -1/2), 75)
    Moving = MassObject((643.30127, 375), ((3**.5)/2, 1/2), 75)
    Third = MassObject((600, 450), (-1, 0), 75)
    Fixed.Draw(displayscreen)
    Moving.Draw(displayscreen)
    Third.Draw(displayscreen)
    game.display.flip()

    while 1:
        for event in game.event.get():
            if event.type == game.QUIT: sys.exit()

        displayscreen.fill(black)

        Moving.RelVects(Fixed.location.x, Fixed.location.y, Third.location.x, Third.location.y)
        Fixed.RelVects(Moving.location.x, Moving.location.y, Third.location.x, Third.location.y)
        Third.RelVects(Moving.location.x, Moving.location.y, Fixed.location.x, Fixed.location.y)

        Fixed.CalcMove(Moving.mass, Third.mass)
        Moving.CalcMove(Fixed.mass, Third.mass)
        Third.CalcMove(Moving.mass, Fixed.mass)

        Moving.Move()
        Fixed.Move()
        Third.Move()

        Fixed.Draw(displayscreen)
        Moving.Draw(displayscreen)
        Third.Draw(displayscreen)
        game.display.flip()


if __name__ == "__main__":
    main()