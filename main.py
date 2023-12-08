
import pygame
from pygame.locals import *
import random
import sys
import asyncio

# Use the current time as a seed

# Use the hash of the seed to get a random number


pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
width,height = 800,800
window = pygame.display.set_mode((width,height))

bg_img = pygame.image.load('monopoly_board.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))

class dice(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((200, 100))
        self.surf.fill((0,0,0))
        self.rect = self.surf.get_rect(center = (300, 500))

    def dice_roll(self):
        roll = random.randint(1, 6)
        return roll
roll = dice()

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
        


buyButton = buy()
auctionButton = auction()


class PropertyButton(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.vertical_buttons = [2, 4, 7, 9, 10, 22, 24, 25, 27, 28, 30] # changed 6 to 7 in this list for light blues
        if position in self.vertical_buttons:
            self.image = pygame.Surface((65, 105), pygame.SRCALPHA)
        else:
            self.image = pygame.Surface((105,65), pygame.SRCALPHA)
        self.image.fill((255, 255, 255, 150))
        
        self.position = position
        self.rect = self.image.get_rect(topleft=self.get_position(position))

    def get_position(self, pos):
        # Define positions for different Monopoly properties
        property_positions = {2: (630, 694), 4: (499, 694), 7: (302, 696), 9: (173, 697), 10: (106, 695), 
         12: (0, 631), 14: (0, 498), 15: (1, 433), 17: (0, 300), 19: (2, 172), 20: (2, 106),
         22: (105, 1), 24: (236, 1), 25: (301, 0), 27: (434, 1), 28: (497, 1), 30: (629, 0),
         32: (695, 105), 33: (694, 170), 35: (695, 300), 38: (695, 498), 40: (695, 629)}
        return property_positions[self.position]
    def mouseOn(self, mousePos):
        if self.position in self.vertical_buttons:
            if self.get_position(self.position)[0] < mousePos[0] < self.get_position(self.position)[0] + 65 and self.get_position(self.position)[1] < mousePos[1] < self.get_position(self.position)[1] + 110:
                return True
        else:
            if self.get_position(self.position)[0] < mousePos[0] < self.get_position(self.position)[0] + 110 and self.get_position(self.position)[1] < mousePos[1] < self.get_position(self.position)[1] + 65:
                return True
        return False

# added spaces to include railroads and utilities for drawing ownership rectangles
spaces = [2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 16, 17, 19, 20, 22, 24, 25, 26, 27, 28, 29, 30, 32, 33, 35, 36, 38, 40]
property_numbers = [2, 4, 7, 9, 10, 12, 14, 15, 17, 19, 20, 22, 24, 25, 27, 28, 30, 32, 33, 35, 38, 40]
property_buttons = [PropertyButton(position) for position in property_numbers]


class Space():
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_position():
        return self.position
        
class Property(Space):
    def __init__(self, color, cost, rent_costs, *args, **kwargs):
        
        self.color = color
        self.cost = cost
        
        self.rent_costs = rent_costs
        self.house_count = 0
        self.hotel_count = 0
        
        super().__init__(*args, **kwargs)
        
        self.owner = "unowned"
        self.mortgaged = False
    
    def get_color():
        return self.color
    
    def get_cost():
        return self.cost
    
    def get_owner():
        return self.owner
    
    def get_status():
        return self.mortgaged
    
    def get_houses():
        return self.house_count
    
    def get_hotels():
        return self.hotel_count

    def get_rent_cost(self):
        return self.rent_costs[self.house_count + (5 * self.hotel_count)]
        
        
        
class Railroad(Space):
    def __init__(self, cost, *args, **kwargs):
        self.cost = cost
        #is this a smart way of doing this? idk
        self.house_count = 0
        self.hotel_count = 0
        self.rent_costs = [25, 50, 100, 200]
        super().__init__(*args, **kwargs)
    def get_rent_cost(self):
        return self.rent_costs[self.house_count]
        
class Utility(Property):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class Chance(Space):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
class Community_Chest(Space):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
class Jail(Space):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
class Go_FreeParking_IncomeTax(Space):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
class Go_to_Jail(Space):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

class Jail_or_Just_Visiting(Space):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
mediterranean_avenue = Property("Brown", 60, [2, 10, 30, 90, 160, 250], "Mediterranean Avenue", 2)
baltic_avenue = Property("Brown", 60, [4, 20, 60, 180, 320, 450], "Baltic Avenue", 4)
oriental_avenue = Property("Light Blue", 100, [6, 30, 90, 270, 400, 550], "Oriental Avenue", 7)
vermont_avenue = Property("Light Blue", 100, [8, 40, 100, 300, 450, 600], "Vermont Avenue", 9)
connecticut_avenue = Property("Light Blue", 120, [6, 30, 90, 270, 400, 550], "Connecticut Avenue", 10)
st_charles_place = Property("Purple", 140, [10, 50, 150, 450, 625, 750], "St. Charles Place", 12)
states_avenue = Property("Purple", 140, [10, 50, 150, 450, 625, 750], "States Avenue", 14)
virginia_avenue = Property("Purple", 160, [12, 60, 180, 500, 700, 900], "Virginia Avenue", 15)
st_james_place = Property("Orange", 180, [14, 70, 200, 550, 750, 950], "St. James Place", 17)
tennessee_avenue = Property("Orange", 180, [14, 70, 200, 550, 750, 950], "Tennessee Avenue", 19)
new_york_avenue = Property("Orange", 200, [16, 80, 220, 600, 800, 1000], "New York Avenue", 20)
kentucky_avenue = Property("Red", 220, [18, 90, 250, 700, 875, 1050], "Kentucky Avenue", 22)
indiana_avenue = Property("Red", 220, [18, 90, 250, 700, 875, 1050], "Indiana Avenue", 24)
illinois_avenue = Property("Red", 240, [20, 100, 300, 750, 925, 1100], "Illinois Avenue", 25)
atlantic_avenue = Property("Yellow", 260, [22, 110, 330, 800, 975, 1150], "Atlantic Avenue", 27)
ventnor_avenue = Property("Yellow", 260, [22, 110, 330, 800, 975, 1150], "Ventnor Avenue", 28)
marvin_gardens = Property("Yellow", 280, [24, 120, 360, 850, 1025, 1200], "Marvin Gardens", 30)
pacific_avenue = Property("Green", 300, [26, 130, 390, 900, 1100, 1275], "Pacific Avenue", 32)
north_carolina_avenue = Property("Green", 300, [26, 130, 390, 900, 1100, 1275], "North Carolina Avenue", 33)
pennsylvania_avenue = Property("Green", 320, [28, 150, 450, 1000, 1200, 1400], "Pennsylvania Avenue", 35)
park_place = Property("Blue", 350, [35, 175, 500, 1100, 1300, 1500], "Park Place", 38)
boardwalk = Property("Blue", 400, [50, 200, 600, 1400, 1700, 2000], "Boardwalk", 40)

reading_railroad = Railroad(200, "Reading Railroad", 6)
pennsylvania_railroad = Railroad(200, "Pennsylvania Railroad", 16)
b_o_railroad = Railroad(200, "B&O Railroad", 26)
short_line_railroad = Railroad(200, "Short Line Railroad", 36)

chance_cards = ["Advance to Go (Collect $200)", 
                "Advance to Illinois Avenue. If you pass Go, collect $200", 
                "Advance to St. Charles Place. If you pass Go, collect $200", 
                "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.", 
                "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled", 
                "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled", 
                "Bank pays you dividend of $50", 
                "Get Out of Jail Free", 
                "Go Back 3 Spaces", 
                "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200", 
                "Make general repairs on all your property. For each house pay $25. For each hotel pay $100", 
                "Speeding fine $15", 
                "Take a trip to Reading Railroad. If you pass Go, collect $200", 
                "Advance to Boardwalk", 
                "You have been elected Chairman of the Board. Pay each player $50", 
                "Your building loan matures. Collect $150"
               ]

community_chest_cards = ["Advance to Go (Collect $200)", 
                         "Bank error in your favor. Collect $200", 
                         "Doctor’s fee. Pay $50", 
                         "From sale of stock you get $50", 
                         "Get Out of Jail Free", 
                         "Go to Jail. Go directly to jail, do not pass Go, do not collect $200", 
                         "Holiday fund matures. Receive $100", 
                         "Income tax refund. Collect $20", 
                         "It is your birthday. Collect $10 from every player", 
                         "Life insurance matures. Collect $100", 
                         "Pay hospital fees of $100", 
                         "Pay school fees of $50", 
                         "Receive $25 consultancy fee", 
                         "You are assessed for street repair. $40 per house. $115 per hotel", 
                         "You have won second prize in a beauty contest. Collect $10", 
                         "You inherit $100"
                        ]

random.shuffle(chance_cards)
random.shuffle(community_chest_cards)



property_objects = {
    2: mediterranean_avenue,
    4: baltic_avenue,
    7: oriental_avenue,
    9: vermont_avenue,
    10: connecticut_avenue,
    12: st_charles_place,
    14: states_avenue,
    15: virginia_avenue,
    17: st_james_place,
    19: tennessee_avenue,
    20: new_york_avenue,
    22: kentucky_avenue,
    24: indiana_avenue,
    25: illinois_avenue,
    27: atlantic_avenue,
    28: ventnor_avenue,
    30: marvin_gardens,
    32: pacific_avenue,
    33: north_carolina_avenue,
    35: pennsylvania_avenue,
    38: park_place,
    40: boardwalk,
    6: reading_railroad,
    16: pennsylvania_railroad,
    26: b_o_railroad,
    36: short_line_railroad,
}
property_positions = list(property_objects.keys())

chance_positions = [8, 23, 27]
community_chest_positions = [3, 18, 34]

color_groups = {
    "Brown": [1, 3],
    "Light Blue": [6, 8, 9],
    "Pink": [11, 13, 14],
    "Orange": [16, 18, 19],
    "Red": [21, 23, 24],
    "Yellow": [26, 27, 29],
    "Green": [31, 32, 34],
    "Dark Blue": [37, 39]}

def find_monopoly_set(property_positions):
    for color, positions in color_groups.items():
        if all(position in property_positions for position in positions):
            return [position for position in positions if position in property_positions]

    return []



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
    
    
P1 = Player()
P1.playerNumber = 1
P1.surf.fill((255,0,0))
P2 = Player()
P2.playerNumber = 2
P2.surf.fill((0,0,255))



# Set up the font
font = pygame.font.Font(None, 36)  # You can specify the font file and size here

# Create a text surface
moneyText1 = font.render(f"${P1.cash}", True, (0, 0, 0))  # True enables anti-aliasing
moneyText2 = font.render(f"${P2.cash}", True, (0, 0, 0))  # True enables anti-aliasing
# Get the rect object for the text surface
text_rect1 = moneyText1.get_rect()
text_rect2 = moneyText2.get_rect()

# Center the text on the screen
text_rect1.center = (200, 200)
text_rect2.center = (600, 200)


gameAnnouncementText = font.render("    ", True, (0,0,0))
gameAnnouncement_rect = gameAnnouncementText.get_rect()
gameAnnouncement_rect.center = (400,425)





all_sprites = pygame.sprite.Group()

all_sprites.add(roll)
all_sprites.add(P1)
all_sprites.add(P2)
clicked = False
actionChosen = False


async def playerTurn(player, rolls):
    global moneyText1
    global moneyText2
    global gameAnnouncementText
    global gameAnnouncement_rect
    global actionChosen
    all_sprites.remove(roll)

    if player.injail:
        player.jailCounter -= 1
        gameAnnouncementText = font.render(f"player {player.playerNumber} is in jail!", True, (0,0,0))
        gameAnnouncement_rect = gameAnnouncementText.get_rect()
        gameAnnouncement_rect.center = (400,425)
        if player.jailCounter == 1:
            player.injail = False
            player.cash -= 50
    else:
        #if doubles
        if rolls[0] == rolls[1]:
            player.doublesCounter += 1
            gameAnnouncementText = font.render(f"player {player.playerNumber} rolled doubles!", True, (0,0,0))
            gameAnnouncement_rect = gameAnnouncementText.get_rect()
            gameAnnouncement_rect.center = (400,425)
            player.rolledDoubles = True
        #if not doubles
        else:
            player.rolledDoubles = False
            player.doublesCounter = 0
        #if 3 consecutive doubles or if lands on Go to Jail
        if player.doublesCounter >= 3 or player.position == 31:
            player.position = 11
            player.move(player.position_to_coordinates(player.position))
            player.injail = True
            player.jailCounter = 3
            player.rolledDoubles = False
            player.doublesCounter = 0
        #if not 3 consecutive doubles
        else:
            roll_sum = rolls[0] + rolls[1]
            player.add_position(roll_sum)
            player.move(player.position_to_coordinates(player.position))
            
            # community chest cards                    
            if player.position in community_chest_positions:
                # get card action, move card to the back of the list
                action = community_chest_cards[0]
                community_chest_cards.append(action)
                community_chest_cards.pop(0)
                
                # custom responses to each card
                if action == "Advance to Go (Collect $200)":
                    player.position = 1
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Bank error in your favor. Collect $200":
                    player.cash += 200
                elif action == "Doctor’s fee. Pay $50":
                    player.cash -= 50
                elif action == "From sale of stock you get $50":
                    player.cash += 50
                elif action == "Get Out of Jail Free":
                    player.getoutofjailfree += 1
                elif action == "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200":
                    player.position = 11
                    player.move(player.position_to_coordinates(player.position))
                    player.injail = True
                    player.jailCounter = 3
                    player.rolledDoubles = False
                    player.doublesCounter = 0
                elif action == "Holiday fund matures. Receive $100":
                    player.cash += 100
                elif action == "Income tax refund. Collect $20":
                    player.cash += 100
                elif action == "It is your birthday. Collect $10 from every player":
                    player.cash += ((playerCount - 1) * 10)
                    for p in range(1, playerCount):
                        if p != player.playerNumber:
                            players[p - 1].cash -= 10
                    # not sure how to remove $10 from other players
                    # will also need to change +=10 to be based on 10*# of other players eventually
                elif action == "Life insurance matures. Collect $100":
                    player.cash += 100
                elif action == "Pay hospital fees of $100":
                    player.cash -= 100
                elif action == "Pay school fees of $50":
                    player.cash -= 50
                elif action == "Receive $25 consultancy fee":
                    player.cash += 25
                elif action == "You are assessed for street repair. $40 per house. $115 per hotel":
                    totalHouses = 0
                    totalHotels = 0
                    for p in player.properties:
                        totalHouses += p.house_count
                        totalHotels += p.hotel_count
                    player.cash -= (40 * totalHouses) + (125 * totalHotels)
                elif action == "You have won second prize in a beauty contest. Collect $10":
                    player.cash += 10
                elif action == "You inherit $100":
                    player.cash += 100
            
            # chance cards                    
            if player.position in chance_positions:
                # get card action, move card to the back of the list
                action = chance_cards[0]
                chance_cards.append(action)
                chance_cards.pop(0)
                
                # custom responses to each card
                if action == "Advance to Go (Collect $200)":
                    player.position = 1
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Advance to Illinois Avenue. If you pass Go, collect $200":
                    if player.position == 37:
                        player.cash += 200
                    player.position == 25
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Advance to St. Charles Place. If you pass Go, collect $200":
                    if player.position in [23, 37]:
                        player.cash += 200
                    player.position == 12
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.":
                    if player.position == 8:
                        player.position == 13
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 23:
                        player.position == 29
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 37:
                        player.position == 13
                        player.move(player.position_to_coordinates(player.position))
                        player.cash += 200
                elif action == "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled":
                    if player.position == 8:
                        player.position == 16
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 23:
                        player.position == 26
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 37:
                        player.position == 6
                        player.move(player.position_to_coordinates(player.position))
                        player.cash += 200
                elif action == "Bank pays you dividend of $50":
                    player.cash += 50
                elif action == "Get Out of Jail Free":
                    player.getoutofjailfree += 1
                elif action == "Go Back 3 Spaces":
                    player.position -= 3
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Go to Jail. Go directly to Jail, do not pass Go, do not collect $200":
                    player.position = 11
                    player.move(player.position_to_coordinates(player.position))
                    player.injail = True
                    player.jailCounter = 3
                    player.rolledDoubles = False
                    player.doublesCounter = 0
                elif action == "Make general repairs on all your property. For each house pay $25. For each hotel pay $100":
                    totalHouses = 0
                    totalHotels = 0
                    for p in player.properties:
                        totalHouses += p.house_count
                        totalHotels += p.hotel_count
                    player.cash -= (25 * totalHouses) + (100 * totalHotels)
                elif action == "Speeding fine $15":
                    player.cash -= 15
                elif action == "Take a trip to Reading Railroad. If you pass Go, collect $200":
                    player.position == 6
                    player.cash += 200
                elif action == "Advance to Boardwalk":
                    player.position == 40
                elif action == "You have been elected Chairman of the Board. Pay each player $50":
                    player.cash -= (50 * (playerCount - 1))
                    for p in range(1, playerCount):
                        if p != player.playerNumber:
                            players[p - 1].cash -= 10
                elif action == "Your building loan matures. Collect $150":
                    player.cash += 150
            
            #if landed in an owned property/railroad space
            for p in players:
                if p.playerNumber != player.playerNumber:
                    for opponentProperty in p.properties:
                        if player.position == opponentProperty.position:
                            rentToPay = opponentProperty.get_rent_cost()
                            player.cash -= rentToPay
                            print(f"paid {rentToPay} for rent")
            
            #if landed in an unowned property/railroad space(later to add utilties)
            if player.position in property_objects:
                actionChosen = True
                #show auction/buy buttons
                all_sprites.add(auctionButton)
                all_sprites.add(buyButton)
                #display new button sprites
                for entity in all_sprites:
                    window.blit(entity.surf, entity.rect)
                pygame.display.update()
                #wait till either buy or auction is chosen
                clickedAction = False
                while actionChosen:
                    mousePos = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                    #if the x button is hit, quit
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    #if buy button is hit
                    if 250 <= mousePos[0] <= 350 and 300 <= mousePos[1] <= 400: 
                        if pygame.mouse.get_pressed()[0] == True:
                            clickedAction = True
                        if clickedAction:
                            if pygame.mouse.get_pressed()[0] == False:
                                clickedAction = False
                                actionChosen = False
                                #remove button sprites
                                all_sprites.remove(auctionButton)
                                all_sprites.remove(buyButton)
                                player.cash -= property_objects[player.position].cost
                                if player.playerNumber == 1:    
                                    moneyText1 = font.render(f"${player.cash}", True, (0, 0, 0))
                                elif player.playerNumber == 2:
                                    moneyText2 = font.render(f"${player.cash}", True, (0, 0, 0))
                                player.properties.append(property_objects[player.position])
                                railroadPositions = [6,16,26,36]
                                if player.position in railroadPositions:
                                     player.properties[-1].house_count += 1
                                property_objects.pop(player.position)
                    #if auction button is hit(do nothing for now) 
                    if 450 <= mousePos[0] <= 550 and 300 <= mousePos[1] <= 400: 
                        if pygame.mouse.get_pressed()[0] == True:
                               clickedAction = True
                        if clickedAction:
                            if pygame.mouse.get_pressed()[0] == False:
                                clickedAction = False
                                actionChosen = False
                                #remove button sprites
                                all_sprites.remove(auctionButton)
                                all_sprites.remove(buyButton)
                    await asyncio.sleep(0)  # This line is critical; ensure you keep the sleep time at 0
            
    all_sprites.add(roll)
    for entity in all_sprites:
        window.blit(entity.surf, entity.rect)
    pygame.display.update()
    waitToEndTurn = True
    endTurnClicked = False
    buyHouseClicked = False
    propertyPositionsList = []
    for prop in player.properties:
        propertyPositionsList.append(prop.position)
    set_of_monopolies = find_monopoly_set(propertyPositionsList)
    if set_of_monopolies:
        print("player has a set")
        buttonsToDraw = []
        for b in property_buttons:
            if b.position in set_of_monopolies:
                all_sprites.add(b)
                buttonsToDraw.append(b)
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)
        pygame.display.update()
        
        while waitToEndTurn:
            mousePos = pygame.mouse.get_pos()
            event = pygame.event.wait()
            #if the x button is hit, quit
            if event.type == pygame.QUIT:
                pygame.quit()
            
            #if clicked on buttons buy house/hotel
            for button in buttonsToDraw:
                if button.mouseOn(mousePos):
                    if pygame.mouse.get_pressed()[0] == True:
                        endTurnClicked = True
                    if endTurnClicked:
                        #if released button, do action
                        if pygame.mouse.get_pressed()[0] == False:
                            endTurnClicked = False
                            for p in player.properties:
                                if p.position == button.position:
                                    houseCost = 0
                                    if p.color == "Brown" or p.color == "Light Blue":
                                        houseCost = 50
                                    elif p.color == "Purple" or p.color == "Orange":
                                        houseCost = 100
                                    elif p.color == "Red" or p.color == "Yellow":
                                        houseCost = 150
                                    elif p.color == "Green" or p.color == "Blue":
                                        houseCost = 200
                                    player.cash -= houseCost
                                    p.house_count += 1
                                    if p.house_count >= 5:
                                        p.house_count = 0
                                        p.hotel_count = 1
            # await line was here, moved it to end of while loop
            
            
            if 200 <= mousePos[0] <= 400 and 450 <= mousePos[1] <= 550: 
                if pygame.mouse.get_pressed()[0] == True:
                    endTurnClicked = True
                if endTurnClicked:
                    #if released button, do action
                    if pygame.mouse.get_pressed()[0] == False:
                        endTurnClicked = False
                        waitToEndTurn = False
                        
            await asyncio.sleep(0)  # Let other tasks run
        
        for i in range(len(buttonsToDraw)):
            all_sprites.remove(buttonsToDraw[i])
            
#list of all player objects
players = [P1,P2]
playerCount = len(players)
turnCounter = 0
            
            

async def main():
    global clicked
    global gameAnnouncementText
    global gameAnnouncement_rect
    global players
    global playerCount
    global turnCounter
    global rolls
    
    while True:
        window.blit(bg_img,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
        #add money info   

        window.blit(moneyText1, text_rect1)
        window.blit(moneyText2, text_rect2)
        window.blit(gameAnnouncementText, gameAnnouncement_rect)
        
        #add property ownership indicators
        vertical_spaces = [2, 4, 6, 7, 9, 10, 22, 24, 25, 26, 27, 28, 29, 30]
        for prop in P1.properties:
            propertyPositionsList.append(prop.position)
            
        for prop in P2.properties:
            propertyPositionsList.append(prop.position)
        
        #mouse coords
        mousePos = pygame.mouse.get_pos()
        rolls = [roll.dice_roll(), roll.dice_roll()]  
        gameAnnouncementText = font.render(f"{rolls[0] == rolls[1]}", True, (0,0,0))
        gameAnnouncement_rect = gameAnnouncementText.get_rect()
        window.blit(gameAnnouncementText, gameAnnouncement_rect)
        #if hit button
        if 200 <= mousePos[0] <= 400 and 450 <= mousePos[1] <= 550: 
            
            
            if pygame.mouse.get_pressed()[0] == True:

                clicked = True
            if clicked:
                
                #if released button, do action

                if pygame.mouse.get_pressed()[0] == False:
                    clicked = False
                    
                    gameAnnouncementText = font.render(f"   ", True, (0,0,0))

                    #get rid of game announcement text

                    #roll twice
                    rolls = [roll.dice_roll(), roll.dice_roll()]  
                    #print (rolls)
                    #turn counter for keeping track of whose turn it is
                    #playerTurn = turn action function
                    asyncio.run(playerTurn(players[turnCounter], rolls))
                    #print(players[turnCounter].list_properties())
                    if players[turnCounter].rolledDoubles:
                        turnCounter -= 1

                    turnCounter += 1
                    if turnCounter >= playerCount:
                        turnCounter = 0
                        
        #display sprites
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)
        
        
        
        pygame.display.update()
        await asyncio.sleep(0)  # This line is critical; ensure you keep the sleep time at 0

asyncio.run(main())


    
            
'''



'''