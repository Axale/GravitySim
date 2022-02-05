from time import sleep
import pygame as game
import sys as sys
        

def main():
    game.init()
    black = game.Color(0, 0, 0)
    white = game.Color(255, 255, 255)

    displayscreen = game.display.set_mode((1200, 800))
    displayscreen.fill(black)
    logs = open('logs.txt', 'r')
    inputlogs = logs.read()
    inputlist = inputlogs.split(" ")
    index = 0
    lenlist = len(inputlist)

    while 1:
        
        for event in game.event.get():
            if event.type == game.QUIT: sys.exit()
        if index >= lenlist:
            break
        
        print(index)
        displayscreen.fill(black)
        Draw(displayscreen, white, float(inputlist[index]), float(inputlist[index+1]))
        Draw(displayscreen, white, float(inputlist[index + 2]), float(inputlist[index + 3]))
        Draw(displayscreen, white, float(inputlist[index + 4]), float(inputlist[index + 5]))
        game.display.flip()
        index += 30

def Draw(displayscreen, white, Coord1, Coord2):
    if Coord1 > 0 and Coord1 < 1200 and Coord2 > 0 and Coord2 < 800:
        game.draw.circle(displayscreen, white, game.Vector2(Coord1, Coord2), 5, width=0)

if __name__ == "__main__":
    main()