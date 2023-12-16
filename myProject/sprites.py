import pygame
from pygame.locals import *
import random

vec = pygame.math.Vector2  # 2 for two dimensional

# dictionary that maps int positions between 1 and 40 to coordinates in the browser window
space_dict = {
    1: [770, 770],
    2: [670, 770],
    3: [600, 770],
    4: [530, 770],
    5: [470, 770],
    6: [400, 770],
    7: [330, 770],
    8: [270, 770],
    9: [200, 770],
    10: [140, 770],
    11: [30, 770],
    12: [30, 670],
    13: [30, 610],
    14: [30, 540],
    15: [30, 470],
    16: [30, 410],
    17: [30, 340],
    18: [30, 280],
    19: [30, 210],
    20: [30, 150],
    21: [30, 40],
    22: [140, 40],
    23: [200, 40],
    24: [270, 40],
    25: [330, 40],
    26: [400, 40],
    27: [470, 40],
    28: [530, 40],
    29: [600, 40],
    30: [670, 40],
    31: [770, 40],
    32: [770, 150],
    33: [770, 210],
    34: [770, 280],
    35: [770, 340],
    36: [770, 410],
    37: [770, 470],
    38: [770, 540],
    39: [770, 610],
    40: [770, 670]}

class dice(pygame.sprite.Sprite): 
    '''
    This class is a black button sprite used to represent where the user should click to roll the dice or end turn.
    It also contains the dice_roll() function, which generates a random number between 1 and 6 as the dice roll.
    
    inherits from pygame.sprite.Sprite class
    '''
    def __init__(self):
        '''
        Constructs all the necessary attributes for the dice object
        '''
        super().__init__() 
        # set the surface size, color, and center
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(center = (300, 500))

    def dice_roll(self):
        '''
        Generates a random number between 1 and 6 as a dice roll
        
        Returns the random number between 1 and 6 as an int
        '''
        roll = random.randint(1, 6)
        return roll

class buy(pygame.sprite.Sprite): 
    '''
    This class is a green button sprite used to represent where the user should click to buy an unowned property they have landed on.
    
    inherits from pygame.sprite.Sprite class
    '''
    def __init__(self):
        '''
        Constructs all the necessary attributes for the buy object
        '''
        super().__init__() 
        # set the surface size, color, and center, and make visible
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (300, 350))
        self.visible = True

        
class auction(pygame.sprite.Sprite): 
    '''
    This class is a red button sprite used to represent where the user should click 
    to auction (or not buy) an unowned property they have landed on.
    
    inherits from pygame.sprite.Sprite class
    '''
    def __init__(self):
        '''
        Constructs all the necessary attributes for the auction object
        '''
        super().__init__() 
        # set the surface size, color, and center
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (500, 350))


class house(pygame.sprite.Sprite):
    '''
    This class is a number of green sprites that is a function of house_count and hotel_count
    that is placed on the top of a property that a player owns as part of a monopoly
    if the player has purchased a house on that property
    
    inherits from pygame.sprite.Sprite class
    '''
    def __init__(self, position, house_count, hotel_count):
        '''
        Constructs all the necessary attributes for the house object
        Determines the correct placement of the houses and hotels relative to the top left of the property using position
        
        position is an int representing the numerical position of the property the house is being placed on
        house_count is an int representing the number of houses to be placed on that property
        hotel_count is an int representingthe number of hotels to be placed on that property
        '''
        super().__init__()
        # define list of positions on each side of the board that can have houses/hotels built on them
        self.buttons1 = [2, 4, 6, 7, 9, 10]
        self.buttons2 = [12, 14, 15, 16, 17, 19, 20]
        self.buttons3 = [22, 24, 25, 26, 27, 28, 30]
        self.buttons4 = [32, 33, 35, 36, 38, 40]
        
        self.surfList = []
        self.rectList = []
        
        self.position = position
        self.house_count = house_count
        self.hotel_count = hotel_count
        
        # set the surface size, color, and top left positions based on position parameter
        if self.position in self.buttons1:
            if self.hotel_count == 1:
                self.surfList = [pygame.Surface((20,15))]
                self.surfList[0].fill((255,100,100))
                self.rectList = [self.surfList[0].get_rect(topleft = (self.get_position()[0] + 5, self.get_position()[1] + 5))]
            else:
                for i in range(house_count):
                    self.surfList.append(pygame.Surface((10, 10)))
                    self.surfList[i].fill((0,255,0))
                    leftPosition = self.get_position()
                    leftPosition = (leftPosition[0] + (i*13) + 5, leftPosition[1] + 5)
                    self.rectList.append(self.surfList[i].get_rect(topleft = leftPosition))
        if self.position in self.buttons2:
            if self.hotel_count == 1:
                self.surfList = [pygame.Surface((15,20))]
                self.surfList[0].fill((255,100,100))
                self.rectList = [self.surfList[0].get_rect(topleft = (self.get_position()[0] + 85, self.get_position()[1] + 5))]
            else:
                for i in range(house_count):
                    self.surfList.append(pygame.Surface((10, 10)))
                    self.surfList[i].fill((0,255,0))
                    leftPosition = self.get_position()
                    leftPosition = (leftPosition[0] + 90, leftPosition[1] + (i*13) + 5)
                    self.rectList.append(self.surfList[i].get_rect(topleft = leftPosition))
        if self.position in self.buttons3:
            if self.hotel_count == 1:
                self.surfList = [pygame.Surface((20,15))]
                self.surfList[0].fill((255,100,100))
                self.rectList = [self.surfList[0].get_rect(topleft = (self.get_position()[0] + 40, self.get_position()[1] + 85))]
            else:
                for i in range(house_count):
                    self.surfList.append(pygame.Surface((10, 10)))
                    self.surfList[i].fill((0,255,0))
                    leftPosition = self.get_position()
                    leftPosition = (leftPosition[0] - (i*13) + 50, leftPosition[1] + 90)
                    self.rectList.append(self.surfList[i].get_rect(topleft = leftPosition))
        if self.position in self.buttons4:
            if self.hotel_count == 1:
                self.surfList = [pygame.Surface((15,20))]
                self.surfList[0].fill((255,100,100))
                self.rectList = [self.surfList[0].get_rect(topleft = (self.get_position()[0] + 5, self.get_position()[1] + 50))]
            else:
                for i in range(house_count):
                    self.surfList.append(pygame.Surface((10, 10)))
                    self.surfList[i].fill((0,255,0))
                    leftPosition = self.get_position()
                    leftPosition = (leftPosition[0] + 5, leftPosition[1] - (i*13) + 50)
                    self.rectList.append(self.surfList[i].get_rect(topleft = leftPosition))
    
    def get_position(self):
        '''
        Defines positions for all the different Monopoly properties as a reference point for the houses/hotels
        
        returns the coordinates of the property this house object has been made for using the position parameter
        '''
        property_positions = {2: (630, 695), 4: (499, 695), 6: (368, 695), 7: (302, 695), 9: (171, 695), 10: (105, 695), 
         12: (0, 630), 14: (0, 499), 15: (0, 433), 16: (0, 367), 17: (0, 301), 19: (0, 170), 20: (0, 104),
         22: (105, 0), 24: (236, 0), 25: (301, 0), 26: (367, 0), 27: (434, 0), 28: (498, 0), 30: (629, 0),
         32: (695, 105), 33: (695, 170), 35: (695, 301), 36: (695, 367), 38: (695, 499), 40: (695, 630)}
        return property_positions[self.position]


class PropertyButton(pygame.sprite.Sprite):
    '''
    This class is a transparent sprite that signifies that the player of the color being used to shade the property owns it.
    
    inherits from pygame.sprite.Sprite class
    '''
    def __init__(self, position, playerNumber):
        '''
        Constructs all the necessary attributes for the PropertyButton object
        Matches vertical/horizontal orientation of shaded PropertyButton object with actual property using vertical_buttons
        
        playerNumber is an int representingthe player who owns the property.
        This is used to determine the color of the PropertyButton object.
        '''
        super().__init__()
        
        # define list of vertically oriented properties
        self.vertical_buttons = [2, 4, 6, 7, 9, 10, 22, 24, 25, 26, 27, 28, 30, 29]
        # define shape of PropertyButton object based on vertical or horizontal orientation
        if position in self.vertical_buttons:
            self.image = pygame.Surface((65, 105), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((105,65), pygame.SRCALPHA)
        
        # define dictionary of colors to be used with playerNumber to determine what color to make PropertyButton
        self.colorDict = [(255, 0, 0, 100), (0, 0, 255, 100)]
        # set color of PropertyButton object to the corresponding player's color
        self.image.fill(self.colorDict[playerNumber - 1])
        
        # set position of PropertyButton object and get top left position of the object
        self.position = position
        self.rect = self.image.get_rect(topleft=self.get_position())

    def get_position(self):
        '''
        Defines positions for all the different Monopoly properties as a reference point for the houses/hotels
        
        returns the coordinates of the property this house object has been made for using the position parameter
        '''
        property_positions = {2: (630, 695), 4: (499, 695), 6: (368, 695), 7: (302, 695), 9: (171, 695), 10: (105, 695), 
         12: (0, 630), 14: (0, 499), 15: (0, 433), 16: (0, 367), 17: (0, 301), 19: (0, 170), 20: (0, 104),
         22: (105, 0), 24: (236, 0), 25: (301, 0), 26: (367, 0), 27: (434, 0), 28: (498, 0), 30: (629, 0),
         32: (695, 105), 33: (695, 170), 35: (695, 301), 36: (695, 367), 38: (695, 499), 40: (695, 630),
         13: (0, 565), 29: (565, 0)}
        return property_positions[self.position]
    
    def mouseOn(self, mousePos):
        '''
        Detects if mouse is hovering over the PropertyButton object
        
        returns a Boolean that represents whether the mouse is currently hovering over the button
        '''
        # set range of coordinates to check based on vertical or horizontal orientation of PropertyButton
        # return True if the mouse is on the object
        if self.position in self.vertical_buttons:
            if self.get_position()[0] < mousePos[0] < self.get_position()[0] + 65 and self.get_position()[1] < mousePos[1] < self.get_position()[1] + 110:
                return True
        else:
            if self.get_position()[0] < mousePos[0] < self.get_position()[0] + 110 and self.get_position()[1] < mousePos[1] < self.get_position()[1] + 65:
                return True
        return False


class Player(pygame.sprite.Sprite):
    '''
    This class is a sprite that represents a player's position on the board
    
    inherits from pygame.sprite.Sprite class
    '''
    def __init__(self):
        '''
        Constructs all the necessary attributes for the Player object
        '''
        super().__init__() 
        # set the size of the Player object
        self.surf = pygame.Surface((20, 20))
        # set the color of the Player object to white by default
        # each player object will have its color changed in the main file
        self.surf.fill((255,255,255))
        # define how and where to draw Player object
        self.rect = self.surf.get_rect(center = (770, 770))
        
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
        # set initial values for attributes of Player object to be used in game logic
        # playerNumber will be changed upon the creation of each player
        self.playerNumber = 0
        self.cash = 1500
        self.position = 1
        self.properties = []
        
        self.railroad_count = 0
        self.utility_count = 0
        
        self.getoutofjailfree = 0
        self.rolledDoubles = False
        self.doublesCounter = 0
        self.injail = False
        self.jailCounter = 0
        
        
    def get_position(self):
        '''
        Gets the current position value of the Player object
        
        returns the value of self.position, which is an int between 1 and 40
        '''
        return self.position
    
    def add_position(self, addValue):
        '''
        Changes the position of the Player object according to the most recent dice roll for that player
        
        addValue is an int representing the amount to be added to the player's current position, 
        which is equal to the value of the value of the current dice roll
        '''
        self.position = self.position + addValue
        # check if position has exceeded 40
        # this means the player has passed Go, and thus the player's position should be reset to 1 and counting
        if self.position > 40:
            self.position = self.position - 40
            # add $200 to player's balance for passing Go
            self.cash += 200
        # checks for rare occassion that player has moved backwards behind go and applies reverse logic to properly set position
        if self.position <1:
            self.position = self.position + 40
    
    def move(self, coordinates):
        '''
        Changes the coordinates of the Player object
        
        coordinates is the set of coordinates that the Player should have, which is determined by pos.x and pos.y
        '''
        self.pos.x = coordinates[0]
        self.pos.y = coordinates[1]
        self.rect.midbottom = self.pos
    
    def position_to_coordinates(self, position):
        '''
        Maps the int position between 1 and 40 of the Player object to the corresponding coordinates
        so that the sprite can be drawn in the correct location
        
        position is the int position between 1 and 40 of the Player object
        '''
        # returns corresponding coordinates using space_dict, which maps int positions to coordinates
        for key in space_dict:
            if key == position:
                return space_dict[key]
    
    def list_properties(self):
        '''
        Gets the list of all properties the Player owns
        
        returns a list of property names, which are strings
        '''
        property_list = [propertyName.name for propertyName in self.properties]
        return property_list
