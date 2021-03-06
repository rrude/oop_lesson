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
class Furniture(GameElement):
    SOLID = True

class Teacher1(Furniture):
    IMAGE = "Horns"
    def interact(self, player):  
        if len(PLAYER.inventory) >= 4:
            GAME_BOARD.draw_msg("You did it. You've got some mad programming skills.")
            makehackbright()
        elif sum(player.energy) > 30:
            PLAYER.energy.append(-5)
            GAME_BOARD.draw_msg("You're late! That will cost you one joke. -5 from your energy. ENERGY LEVEL: %s" % (sum(player.energy)))
        else:
            GAME_BOARD.draw_msg("You look exhausted! Grab some zzz's. ENERGY LEVEL: %s" % (sum(player.energy)))

class Teacher2(Furniture):
    IMAGE = "Boy"
    def interact(self, player):
        
        if len(PLAYER.inventory) >= 4:
            print len(PLAYER.inventory)
            GAME_BOARD.draw_msg("You did it. You've got some mad programming skills.")
            makehackbright()        

        elif sum(player.energy) < 60:
            PLAYER.energy.append(10)
            GAME_BOARD.draw_msg("Teach sez: 'You're FINE. You aren't behind at all!' +10 energy boost! ENERGY LEVEL: %s" % (sum(player.energy)))
        

        else:
            PLAYER.energy.append(-10)
            GAME_BOARD.draw_msg("Here's an ambiguous hint to confu--I mean, help you. ENERGY LEVEL: %s" % (sum(player.energy)))
            makepython()


class Desk(Furniture):
    IMAGE = "Desk"

class Coffeemaker(GameElement):
    IMAGE = "CoffeeMaker"  
    SOLID = True
    def interact(self, player):
        GAME_BOARD.draw_msg("Let's HOMEbrew some coffee. Get it?! Haha, I'm so funny.")
        makecoffee()


class SofaLeft(Furniture):
    IMAGE = "SofaLeft"
    def interact(self, player):
        if sum(player.energy) < 50:
            player.energy.append(20)
            GAME_BOARD.draw_msg("Couch nap! Energy boost! +15 ENERGY LEVEL: %s" % (sum(player.energy)))
        else:
            GAME_BOARD.draw_msg("Be a hacker not a slacker. Get back to the lab! ENERGY LEVEL: %s" % (sum(player.energy)))

class SofaRight(Furniture):
    IMAGE = "SofaRight"

class BrownSofa(Furniture):
    IMAGE = "SofaBrown"

class BrownSofaRed(Furniture):
    IMAGE = "SofaBrownRed"

class Collectibles(GameElement):
    SOLID = False
    IMAGE = "Coffee"
    def __repr__(self):
        return self.IMAGE
    #Put stuff here

class Coffee(Collectibles):
    IMAGE = "Coffee"
    def interact(self, player):
        player.energy.append(10)
        GAME_BOARD.draw_msg("Coffee break! ENERGY LEVEL: %s." % (sum(player.energy)))


class Python(Collectibles):
    IMAGE = "Python"
    
    def interact(self, player):
        if sum(player.energy) < 20:
            self.SOLID = True
            GAME_BOARD.draw_msg("Not enough energy to learn PYTHON SKILLS. Find energy fast. ENERGY LEVEL: %s" % (sum(player.energy)))
        else:            
            self.SOLID = False
            player.energy.append(-20)
            player.inventory.append(self)
            GAME_BOARD.draw_msg("PYTHON SKILLS. You have %d items! Press 'i' to view Inventory. ENERGY LEVEL: %s." % (len(player.inventory), sum((player.energy))))

# class Pizza(Collectibles):
#     IMAGE = "OrangeGem"
#     def interact(self, player):
#         player.inventory.append(self)
#         GAME_BOARD.draw_msg("Carbs are brain food. You have %d items!" % (len(player.inventory)))


class Gem(Collectibles):
    IMAGE = "Ruby" 
    def interact(self, player):
        #player.inventory.append(self)
        if sum(player.energy) < 40:
            self.SOLID = True
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            initialize()
            GAME_BOARD.draw_msg("BUMMER! Not enough energy. Death by Ruby. Try again.")
        else:
            player.energy.append(-40)
            GAME_BOARD.draw_msg("EVIL RUBY. CAN'T BRAIN. -40. ENERGY LEVEL: %s. Find coffee ASAP." % (sum((player.energy))))


class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Hacker(GameElement):
    IMAGE = "Hackbright" 
    SOLID = False  
    def interact(self, player):
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        initialize()
        GAME_BOARD.draw_msg("YOU CAN'T WIN HACKBRIGHT") 

class Recur(GameElement):
    IMAGE = "Recursion"  
    SOLID = True
    def interact(self, player):
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        initialize()
        GAME_BOARD.draw_msg("Recursion Trap! Try again.")



class Character(GameElement):
    IMAGE = "Hackbrighter"

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
        self.energy = [50]
        GameElement.__init__(self)
        self.inventory = []






####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    #Red Sofa Placement
    sofaright = SofaRight()
    GAME_BOARD.register(sofaright)
    GAME_BOARD.set_el(3, 2, sofaright)

    sofaleft = SofaLeft()
    GAME_BOARD.register(sofaleft)
    GAME_BOARD.set_el(2, 2, sofaleft)

    #Brown Sofa Placement
    sofabrown = BrownSofa()
    GAME_BOARD.register(sofabrown)
    GAME_BOARD.set_el(1, 6, sofabrown)
    GAME_BOARD.set_el(3, 6, sofabrown)

    sofabrownred = BrownSofaRed()
    GAME_BOARD.register(sofabrownred)
    GAME_BOARD.set_el(2, 6, sofabrownred)

    desk = Desk()
    GAME_BOARD.register(desk)
    GAME_BOARD.set_el(6, 2, desk)
    GAME_BOARD.set_el(6, 3, desk)
    GAME_BOARD.set_el(6, 5, desk)
    GAME_BOARD.set_el(6, 6, desk)
    GAME_BOARD.set_el(8, 2, desk)
    GAME_BOARD.set_el(8, 3, desk)
    GAME_BOARD.set_el(8, 5, desk)
    GAME_BOARD.set_el(8, 6, desk)

    recursion = Recur()
    GAME_BOARD.register(recursion)
    GAME_BOARD.set_el(8, 0, recursion)
    #initialize instructor w joke request
    teacher1 = Teacher1()
    GAME_BOARD.register(teacher1)
    GAME_BOARD.set_el(0, 3, teacher1)
    #initalize teacher w wisdom
    teacher2 = Teacher2()
    GAME_BOARD.register(teacher2)
    GAME_BOARD.set_el(5, 7, teacher2)

    hackbright = Hacker()
    GAME_BOARD.register(hackbright)

    coffeemaker = Coffeemaker()
    GAME_BOARD.register(coffeemaker)
    GAME_BOARD.set_el(0, 7, coffeemaker)
    #initialize coffee
    coffee_positions = [
            (2, 7),
            (0, 5)
        ]
    coffee_list = []
    for pos in coffee_positions:
        coffee = Coffee()
        GAME_BOARD.register(coffee)
        GAME_BOARD.set_el(pos[0], pos[1], coffee)
        coffee_list.append(coffee)

    for item in coffee_list:
        print coffee

    #initialize python
    python_positions = [
            (7, 2),
            (8, 4),
            (3, 1) 
        ]
    python_list = []
    for pos in python_positions:
        python = Python()
        GAME_BOARD.register(python)
        GAME_BOARD.set_el(pos[0], pos[1], python)
        python_list.append(python)

    for item in python_list:
        print python
        
    #this initialized the Gem (blue one)
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(9, 7, gem)
        
    # initialize the girl
    global PLAYER
    PLAYER = Character()    
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(0, 0, PLAYER)
    print PLAYER

    GAME_BOARD.draw_msg("Welcome to Hackbright! Work hard, but watch your energy. Don't fear the pythons you need at least 4!")
    
def makecoffee():
        coffee = Coffee()
        GAME_BOARD.register(coffee)
        GAME_BOARD.set_el(5, 4, coffee)
        GAME_BOARD.set_el(2, 7, coffee)
        GAME_BOARD.set_el(6, 7, coffee)
        GAME_BOARD.set_el(6, 0, coffee)
        print coffee

def makepython():
        python = Python()
        GAME_BOARD.register(python)
        GAME_BOARD.set_el(4, 3, python)
        GAME_BOARD.set_el(3, 4, python)

def makehackbright():
        hackbright = Hacker()
        GAME_BOARD.register(hackbright)
        GAME_BOARD.set_el(3, 4, hackbright)
             


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
            #below not working yet
            # if existing_el == Python:
            #     if sum(PLAYER.energy) < 20:
            #        print "Can't Brain must get energy\!"

            if existing_el:
                existing_el.interact(PLAYER)
       
           
            if existing_el is None or not existing_el.SOLID:
                GAME_BOARD.del_el(PLAYER.x, PLAYER.y) 
                GAME_BOARD.set_el(next_x, next_y, PLAYER)






