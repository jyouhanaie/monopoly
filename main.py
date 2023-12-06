import pygame
from pygame.locals import *
import random
import sys
import function_classes

pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
 
width,height = 800,800
window = pygame.display.set_mode((width,height))

bg_img = pygame.image.load('monopoly_board.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))



roll = dice()
buyButton = buy()
auctionButton = auction()
property_numbers = [2, 4, 7, 9, 10, 12, 14, 15, 17, 19, 20, 22, 24, 25, 27, 28, 30, 32, 33, 35, 38, 40]
property_buttons = [PropertyButton(position) for position in property_numbers]

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

P1 = Player()
P1.playerNumber = 1
P1.surf.fill((0,0,0))
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

#list of all player objects
players = [P1,P2]
playerCount = len(players)
turnCounter = 0;

async def main():
    while True:
        window.blit(bg_img,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                break
        #add money info
        window.blit(moneyText1, text_rect1)
        window.blit(moneyText2, text_rect2)
        window.blit(gameAnnouncementText, gameAnnouncement_rect)
        #mouse coords
        mousePos = pygame.mouse.get_pos()
        
        #if hit button
        if 200 <= mousePos[0] <= 400 and 450 <= mousePos[1] <= 550: 
            if pygame.mouse.get_pressed()[0] == True:
                clicked = True
            if clicked:
                #if released button, do action
                if pygame.mouse.get_pressed()[0] == False:
                    clicked = False
                    #get rid of game announcement text
                    gameAnnouncementText = font.render(f"  ", True, (0,0,0))
                    #roll twice
                    rolls = [roll.dice_roll(), roll.dice_roll()]  
                    print (rolls)
                    #turn counter for keeping track of whose turn it is
                    #playerTurn = turn action function
                    playerTurn(players[turnCounter], rolls)
                    print(players[turnCounter].list_properties())
                    if players[turnCounter].rolledDoubles:
                        turnCounter -= 1
                    
                    turnCounter += 1
                    if turnCounter >= playerCount:
                        turnCounter = 0
        
        #display sprites
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)
        
        pygame.display.update()
        await asyncio.sleep(0)  # Let other tasks run


# This is the program entry point
asyncio.run(main())