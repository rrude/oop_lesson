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

GAME_WIDTH = 4
GAME_HEIGHT = 4

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"



####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    #Initialize and register rock 1
    rock1 = Rock()
    GAME_BOARD.register(rock1)
    GAME_BOARD.set_el(1, 1, rock1)


    #Initialize and register rock 2
    rock2 = Rock()
    GAME_BOARD.register(rock2)
    GAME_BOARD.set_el(2, 2, rock2)

    #Initialize and register rock 3
    rock3 = Rock()
    GAME_BOARD.register(rock3)
    GAME_BOARD.set_el(3, 3, rock3)


    print "The first rock is at", (rock1.x, rock1.y)
    print "The second rock is at", (rock2.x, rock2.y)
    print "The third rock is at", (rock3.x, rock3.y)
    print "Rock 1 image", rock1.IMAGE
    print "Rock 2 image", rock2.IMAGE
    print "Rock 3 image", rock3.IMAGE 