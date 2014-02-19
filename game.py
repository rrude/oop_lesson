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

GAME_WIDTH = 10
GAME_HEIGHT = 8

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Horns"

    def next_pos(self, direction):
        if direction == "up":
            return(self.x, self.y-1)
        elif direction == "down":
            return(self.x, self.y+1)
        elif direction == "left":
            return(self.x-1, self.y)
        elif direction == "right":
            return(self.x+1, self.y)  
        return None

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []


class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!" % (len(player.inventory)))


####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    
    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
            (2, 3)
        ]
    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

    for rock in rocks:
        print rock 

    # initialize the girl
    global PLAYER
    PLAYER = Character()    
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("This game is wicked awesome.")
    #this initialized the Gem (blue one)
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

def keyboard_handler():
    
    if KEYBOARD[key.I]:
        #make I show inventory
        GAME_BOARD.draw_msg("Inventory: %s" % PLAYER.inventory)  

    direction = None

    if KEYBOARD[key.UP]:
        direction = "up"

    if KEYBOARD[key.LEFT]:
       direction = "left"

    if KEYBOARD[key.RIGHT]:
       direction = "right"

    if KEYBOARD[key.DOWN]:
        direction = "down"

    if direction:
        #sets new location tuple (x, y) from .next_pos method
        next_location = PLAYER.next_pos(direction)
        #set x, y variables for next location
        next_x = next_location[0]
        next_y = next_location[1]   

        #added these next two ifs trying to stop player from moving off board
        #if 0 > next_x > 4 or 0 > next_y > 4:
        if next_x == GAME_WIDTH or next_x == -1:
            next_x = PLAYER.x
            next_y = PLAYER.y

        if next_y == GAME_HEIGHT or next_y == -1:
            next_x = PLAYER.x
            next_y = PLAYER.y    
            #GAME_BOARD.set_el(next_x, next_y)
        else:
        #check for existing elements to interact with
            existing_el = GAME_BOARD.get_el(next_x, next_y)
        
            if existing_el:
                existing_el.interact(PLAYER)
       
            
            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y) 
                GAME_BOARD.set_el(next_x, next_y, PLAYER)

     









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