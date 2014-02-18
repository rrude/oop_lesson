import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"

class Character(GameElement):
    IMAGE = "Horns"

####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    
    rock_positions = [
            (2, 1),
            (1, 2),
            (3 ,2),
            (2, 3)
        ]
    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    for rock in rocks:
        print rock 

    # initialize the girl
    global PLAYER
    PLAYER = Character()    
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is wicked awesome.")

def keyboard_handler():
    if KEYBOARD[key.UP]:
        GAME_BOARD.draw_msg("You pressed up")
        next_y = PLAYER.y -1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

    elif KEYBOARD[key.LEFT]:
        GAME_BOARD.draw_msg("You pressed left")
        next_x = PLAYER.x -1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)

    elif KEYBOARD[key.RIGHT]:
        GAME_BOARD.draw_msg("You pressed right")
        next_x = PLAYER.x + 1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, PLAYER.y, PLAYER)

    elif KEYBOARD[key.DOWN]:
        GAME_BOARD.draw_msg("You pressed down")
        next_y = PLAYER.y +1
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

    elif KEYBOARD[key.SPACE]:
        GAME_BOARD.erase_msg()    









    # #Initialize and register rock 1
    # rock1 = Rock()
    # GAME_BOARD.register(rock1)
    # GAME_BOARD.set_el(1, 1, rock1)


    # #Initialize and register rock 2
    # rock2 = Rock()
    # GAME_BOARD.register(rock2)
    # GAME_BOARD.set_el(2, 2, rock2)

    # #Initialize and register rock 3
    # rock3 = Rock()
    # GAME_BOARD.register(rock3)
    # GAME_BOARD.set_el(3, 3, rock3)


    # print "The first rock is at", (rock1.x, rock1.y)
    # print "The second rock is at", (rock2.x, rock2.y)
    # print "The third rock is at", (rock3.x, rock3.y)
    # print "Rock 1 image", rock1.IMAGE
    # print "Rock 2 image", rock2.IMAGE
    # print "Rock 3 image", rock3.IMAGE 