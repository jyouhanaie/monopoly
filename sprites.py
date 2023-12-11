import pygame
from pygame.locals import *
import random

vec = pygame.math.Vector2  # 2 for two dimensional

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
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(center = (300, 500))

    def dice_roll(self):
        roll = random.randint(1, 6)
        return roll

class buy(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect(center = (300, 350))
        self.visible = True

        
class auction(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (500, 350))


class house(pygame.sprite.Sprite):
    def __init__(self, position, house_count, hotel_count):
        super().__init__()
        self.buttons1 = [2, 4, 6, 7, 9, 10]
        self.buttons2 = [12, 14, 15, 16, 17, 19, 20]
        self.buttons3 = [22, 24, 25, 26, 27, 28, 30]
        self.buttons4 = [32, 33, 35, 36, 38, 40]
        
        self.surfList = []
        self.rectList = []
        
        self.position = position
        self.house_count = house_count
        self.hotel_count = hotel_count
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
        # Define positions for different Monopoly properties
        property_positions = {2: (630, 695), 4: (499, 695), 6: (368, 695), 7: (302, 695), 9: (171, 695), 10: (105, 695), 
         12: (0, 630), 14: (0, 499), 15: (0, 433), 16: (0, 367), 17: (0, 301), 19: (0, 170), 20: (0, 104),
         22: (105, 0), 24: (236, 0), 25: (301, 0), 26: (367, 0), 27: (434, 0), 28: (498, 0), 30: (629, 0),
         32: (695, 105), 33: (695, 170), 35: (695, 301), 36: (695, 367), 38: (695, 499), 40: (695, 630)}
        return property_positions[self.position]


class PropertyButton(pygame.sprite.Sprite):
    #temp, change back to 150 or smth later
    
    def __init__(self, position, playerNumber):
        super().__init__()
        self.vertical_buttons = [2, 4, 6, 7, 9, 10, 22, 24, 25, 26, 27, 28, 30, 29] # changed 6 to 7 in this list for light blues
        if position in self.vertical_buttons:
            self.image = pygame.Surface((65, 105), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((105,65), pygame.SRCALPHA)
        self.colorDict = [(255, 0, 0, 100), (0, 0, 255, 100), ( 0, 255, 0, 100) , (255, 255, 0, 100)]
        self.image.fill(self.colorDict[playerNumber - 1])
        
        self.position = position
        self.rect = self.image.get_rect(topleft=self.get_position())

    def get_position(self):
        # Define positions for different Monopoly properties
        property_positions = {2: (630, 695), 4: (499, 695), 6: (368, 695), 7: (302, 695), 9: (171, 695), 10: (105, 695), 
         12: (0, 630), 14: (0, 499), 15: (0, 433), 16: (0, 367), 17: (0, 301), 19: (0, 170), 20: (0, 104),
         22: (105, 0), 24: (236, 0), 25: (301, 0), 26: (367, 0), 27: (434, 0), 28: (498, 0), 30: (629, 0),
         32: (695, 105), 33: (695, 170), 35: (695, 301), 36: (695, 367), 38: (695, 499), 40: (695, 630),
         13: (0, 565), 29: (565, 0)}
        return property_positions[self.position]
    def mouseOn(self, mousePos):
        if self.position in self.vertical_buttons:
            if self.get_position()[0] < mousePos[0] < self.get_position()[0] + 65 and self.get_position()[1] < mousePos[1] < self.get_position()[1] + 110:
                return True
        else:
            if self.get_position()[0] < mousePos[0] < self.get_position()[0] + 110 and self.get_position()[1] < mousePos[1] < self.get_position()[1] + 65:
                return True
        return False


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((20, 20))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = (770, 770))
        
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
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
        return self.position
    
    def add_position(self, addValue):
        self.position = self.position + addValue
        if self.position > 40:
            self.position = self.position - 40
            self.cash += 200
            print("+200 for passing go")
        if self.position <1:
            self.position = self.position + 40
    
    def move(self, coordinates):
        self.pos.x = coordinates[0]
        self.pos.y = coordinates[1]
        self.rect.midbottom = self.pos
    
    def position_to_coordinates(self, position):
        for key in space_dict:
            if key == position:
                return space_dict[key]
    def list_properties(self):
        property_list = [propertyName.name for propertyName in self.properties]
        return property_list
