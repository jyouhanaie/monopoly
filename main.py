
import pygame
from pygame.locals import *
import random
import sys
import asyncio
import sprites
from sprites import *
import spaces
from spaces import *
import helpers
from helpers import *

#randomize seed
random.seed()
#initialize pygame
pygame.init()

#create a vector object
vec = pygame.math.Vector2  # 2 for two dimensional
 
#set game window height and width
width,height = 800,800
window = pygame.display.set_mode((width,height))

#set background image 
bg_img = pygame.image.load('monopoly_board.jpg')
bg_img = pygame.transform.scale(bg_img,(width,height))

#create a dice, buy, and auction object(defined in sprites.py)
roll = dice()
buyButton = buy()
auctionButton = auction()

#set the position numbers for the properties of each row/column of the board
#row1 is the bottom of the board, row2 is the left side, row 3 is the top, row 4 is the right
row1 = [2, 4, 6, 7, 9, 10]
row2 = [12, 13, 14, 15, 16, 17, 19, 20]
row3 = [22, 24, 25, 26, 27, 28, 29, 30]
row4 = [32, 33, 35, 36, 38, 40]

#create a Property object for each of the colored properties on the board
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

#create a railroad object for each of the 4 railroads
reading_railroad = Railroad(200, "Reading Railroad", 6)
pennsylvania_railroad = Railroad(200, "Pennsylvania Railroad", 16)
b_o_railroad = Railroad(200, "B&O Railroad", 26)
short_line_railroad = Railroad(200, "Short Line Railroad", 36)

#create a utilities object for each of the utitilies
electric_company = Utility("Electric Company", 13)
water_works = Utility("Water Works", 29)

#create a list of all of the chance cards
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

#create a list for all of the community chest cards
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
#shuffle the list or "deck" of chance and community chest cards
random.shuffle(chance_cards)
random.shuffle(community_chest_cards)

#create a dictionary relating the position number to the property/railroad/utilities object
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
    13: electric_company,
    29: water_works
}
#create a list of the keys of property objects
property_positions = list(property_objects.keys())

#list for each of the positions of the chance and community chest spaces
chance_positions = [8, 23, 27]
community_chest_positions = [3, 18, 34]  

#create a player object. This game has 2 players
#Player.surf.fill(vec) sets the color of the player object
P1 = Player()
P1.playerNumber = 1
P1.surf.fill((255,0,0))
P2 = Player()
P2.playerNumber = 2
P2.surf.fill((0,0,255))

# Set up the font
font = pygame.font.Font(None, 36)  # You can specify the font file and size here

# Create a text surface for each player's money
moneyText1 = font.render(f"${P1.cash}", True, (0, 0, 0))
moneyText2 = font.render(f"${P2.cash}", True, (0, 0, 0))

# Get the rect object for the text surface
text_rect1 = moneyText1.get_rect()
text_rect2 = moneyText2.get_rect()

# set the position of the text
text_rect1.center = (200, 200)
text_rect2.center = (600, 200)

#create display text for game announcements, and set position
gameAnnouncementText = font.render("    ", True, (0,0,0))
gameAnnouncement_rect = gameAnnouncementText.get_rect()
gameAnnouncement_rect.center = (400,425)

#create lists of texts for properties which are mortgaged
#mortgaged properties will be displayed with the letter M written on the property
morgagedIndicators = []
morgagedIndicatorRects = []

#create an sprite groups object(works like a list) to store multiple sprites. 
#we add the dice, and each of the players to the group
all_sprites = pygame.sprite.Group()

all_sprites.add(roll)
all_sprites.add(P1)
all_sprites.add(P2)

#bools for detecting whether a button was clicked or not later
clicked = False
actionChosen = False

#list of all player objects, turn counter, and total player count variables
players = [P1,P2]
playerCount = len(players)
turnCounter = 0

#create another group for the property action buttons(buy and auction)
propertyActionButtons = pygame.sprite.Group()


async def playerTurn(player, rolls):
    """
    This function defines the game engine for a players turn(activated when a person hits the dice button)

    Parameters:
    - player (Player): Player object whose turn it is
    -rolls ([int. int]): outcomes of 2 dice rolls into a list

    Returns:
    None
    """
    #defines some global variables. This is required to explicitly tell the function to use variables defined outside the scope.
    global moneyText1
    global moneyText2
    global gameAnnouncementText
    global gameAnnouncement_rect
    global actionChosen
    
    #once a player pressed the dice button, remove it until their turn can be completed
    all_sprites.remove(roll)
    
    #display the player's dice rolls
    diceRollText = font.render(f"{rolls[0]}, {rolls[1]}", True, (0,0,0))
    diceRollRect = diceRollText.get_rect()
    diceRollRect.center = (400, 250)
    window.blit(diceRollText, diceRollRect)

    #if a player is in jail, reduce their jailCounter(starts at 3)
    #then announce the player is in jail
    #if the player is on their last turn of jail, let them out of jail, but take 50 dollars
    if player.injail:
        player.jailCounter -= 1
        gameAnnouncementText = font.render(f"player {player.playerNumber} is in jail!", True, (0,0,0))
        gameAnnouncement_rect = gameAnnouncementText.get_rect()
        gameAnnouncement_rect.center = (400,300)
        if player.jailCounter == 1:
            player.injail = False
            player.cash -= 50
    
    else:
        #if a player rolls doubles, increase doubles counter(needed to check if doubles has been rolled 3 consecutive times or not)
        if rolls[0] == rolls[1]:
            player.doublesCounter += 1
            player.rolledDoubles = True
        #if not doubles, reset doubles counter
        else:
            player.rolledDoubles = False
            player.doublesCounter = 0
        #move player according to dice
        roll_sum = rolls[0] + rolls[1]
        player.add_position(roll_sum)
        player.move(player.position_to_coordinates(player.position))
        
        #if 3 consecutive doubles or if lands on Go to Jail
        #send them to jail, arrange the counters appropriately
        if player.doublesCounter >= 3 or player.position == 31:
            player.position = 11
            player.move(player.position_to_coordinates(player.position))
            player.injail = True
            player.jailCounter = 3
            player.rolledDoubles = False
            player.doublesCounter = 0
        #if not 3 consecutive doubles
        else:
            #if landed on income tax, take their money and announce it
            if player.position == 5:
                player.cash -= 200
                action = "Income Tax"
                gameAnnouncementText = font.render(f"{action}", True, (0,0,0))
                gameAnnouncement_rect = gameAnnouncementText.get_rect()
                gameAnnouncement_rect.center = (400,150)
                window.blit(gameAnnouncementText, gameAnnouncement_rect)
            #if landed on luxary tax take players money and announce it
            elif player.position == 39:
                player.cash -= 100
                action = "Luxury Tax"
                gameAnnouncementText = font.render(f"{action}", True, (0,0,0))
                gameAnnouncement_rect = gameAnnouncementText.get_rect()
                gameAnnouncement_rect.center = (400,150)
                window.blit(gameAnnouncementText, gameAnnouncement_rect)
                
            # if landed on community chest cards
            elif player.position in community_chest_positions:
                # get card action, move card to the back of the list
                action = community_chest_cards[0]
                community_chest_cards.append(action)
                community_chest_cards.pop(0)
                
                #announce the community chest card landed on
                gameAnnouncementText = font.render(f"{action}", True, (0,0,0))
                gameAnnouncement_rect = gameAnnouncementText.get_rect()
                gameAnnouncement_rect.center = (400,150)
                window.blit(gameAnnouncementText, gameAnnouncement_rect)
                
                
                # custom responses to each card
                #do the action of the community chest card
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
            
            # if landed on chance cards                    
            elif player.position in chance_positions:
                # get card action, move card to the back of the list
                action = chance_cards[0]
                chance_cards.append(action)
                chance_cards.pop(0)
                
                #announce the chance card landed on
                gameAnnouncementText = font.render(f"{action}", True, (0,0,0))
                gameAnnouncement_rect = gameAnnouncementText.get_rect()
                gameAnnouncement_rect.center = (400,150)
                window.blit(gameAnnouncementText, gameAnnouncement_rect)
                
                # custom responses to each card
                # apply effects of chance card
                if action == "Advance to Go (Collect $200)":
                    player.position = 1
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Advance to Illinois Avenue. If you pass Go, collect $200":
                    if player.position == 37:
                        player.cash += 200
                    player.position = 25
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Advance to St. Charles Place. If you pass Go, collect $200":
                    if player.position in [23, 37]:
                        player.cash += 200
                    player.position = 12
                    player.move(player.position_to_coordinates(player.position))
                elif action == "Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.":
                    if player.position == 8:
                        player.position = 13
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 23:
                        player.position = 29
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 37:
                        player.position = 13
                        player.move(player.position_to_coordinates(player.position))
                        player.cash += 200
                elif action == "Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled":
                    if player.position == 8:
                        player.position = 16
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 23:
                        player.position = 26
                        player.move(player.position_to_coordinates(player.position))
                    elif player.position == 37:
                        player.position = 6
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
                    player.position = 6
                    player.cash += 200
                elif action == "Advance to Boardwalk":
                    player.position = 40
                elif action == "You have been elected Chairman of the Board. Pay each player $50":
                    player.cash -= (50 * (playerCount - 1))
                    for p in range(1, playerCount):
                        if p != player.playerNumber:
                            players[p - 1].cash -= 10
                elif action == "Your building loan matures. Collect $150":
                    player.cash += 150
                    
            #if landed in an owned property/railroad/utility space
            for p in players:
                if p.playerNumber != player.playerNumber:
                    for opponentProperty in p.properties:
                        #set rentToPay as the amount of cash owed to the property owner
                        if player.position == opponentProperty.position:
                            #if landed on owned utilities
                            if player.position == 13: #eletric company
                                if electric_company in p.properties:
                                    rentToPay = 10 * (rolls[0] + rolls[1])
                                else:
                                    rentToPay = 4 + (rolls[0] + rolls[1])
                            elif player.position == 29: #water works
                                if water_works in p.properties:
                                    rentToPay = 10 * (rolls[0] + rolls[1])
                                else:
                                    rentToPay = 4 + (rolls[0] + rolls[1])
                            else:
                                rentToPay = opponentProperty.get_rent_cost()
                            #pay respective cash to the property owner
                            player.cash -= rentToPay
                            
    #update money display
    if player.playerNumber == 1:    
        moneyText1 = font.render(f"${player.cash}", True, (0, 0, 0))
    elif player.playerNumber == 2:
        moneyText2 = font.render(f"${player.cash}", True, (0, 0, 0))
    
    #await decision or end turn
    #bools to check for button hit detection
    waitToEndTurn = True
    endTurnClicked = False
    buyHouseClicked = False
    actionChosen = True
    clickedAction = False
    sellPropertyClicked = False
    
    #bool for if the player is on an unowned property
    onUnownedProperty = player.position in property_objects
    #stay on the player's turn until the user chooses to end their turn
    while waitToEndTurn:
        #if hit x button, quit the program
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
                
        #if landed on unowned property
        if onUnownedProperty:
            #show auction/buy buttons
            propertyActionButtons.add(auctionButton)
            propertyActionButtons.add(buyButton)
            
            #display new button sprites
            #wait till either buy or auction is chosen
            #if buy button is hit
            if 250 <= mousePos[0] <= 350 and 300 <= mousePos[1] <= 400: 
                if pygame.mouse.get_pressed()[0] == True:
                    clickedAction = True
                if clickedAction:
                    #if mouse is released(still on the button)
                    if pygame.mouse.get_pressed()[0] == False:
                        clickedAction = False
                        onUnownedProperty = False
                        #subtract property cost from player's balance
                        player.cash -= property_objects[player.position].cost
                        #update the player money display
                        if player.playerNumber == 1:    
                            moneyText1 = font.render(f"${player.cash}", True, (0, 0, 0))
                        elif player.playerNumber == 2:
                            moneyText2 = font.render(f"${player.cash}", True, (0, 0, 0))
                        #add the property to the player's properties list
                        player.properties.append(property_objects[player.position])
                        #if the player landed on a railroad, add a "house". 1 "house" means 1 railroad owned, 2 "houses" mean 2 railroads owned, etc.
                        #this was done to help implement railroad's rent cost, as it is a function of how many railroads a player owns
                        railroadPositions = [6,16,26,36]
                        if player.position in railroadPositions:
                             player.properties[-1].house_count += 1
                        property_objects.pop(player.position)
            #if auction button is hit(do nothing) 
            if 450 <= mousePos[0] <= 550 and 300 <= mousePos[1] <= 400: 
                if pygame.mouse.get_pressed()[0] == True:
                       clickedAction = True
                if clickedAction:
                    if pygame.mouse.get_pressed()[0] == False:
                        clickedAction = False
                        onUnownedProperty = False
        #if we are not on an unowned property
        #display dice button again as end turn button
        #remove display for buy/auction if applicable
        #update display
        if onUnownedProperty == False:
            propertyActionButtons.empty()
            if roll not in all_sprites:
                all_sprites.add(roll)
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)
        for entity in propertyActionButtons:
            window.blit(entity.surf, entity.rect)
        pygame.display.update()
        
        #monopoly detection
        #necessary for allowing players to buy houses
        #create list for all of the property positions owned by the player
        propertyPositionsList = []
        for prop in player.properties:
            propertyPositionsList.append(prop.position)
        #create a list of properties which form a monopoly owned by the player
        set_of_monopolies = find_monopoly_set(propertyPositionsList)
        #create a list for each of the property objects which form a monopoly
        monopolyProperties = []
        #create a list of lists, where each inner list is the owned property's position used to create a monopoly.
        colorSet = find_monopoly_sets_separated(propertyPositionsList)
        #if colorSet is not empty
        if colorSet:
            #create a list of lists, meant to recreate colorSet but with property objects instead of positions
            propertySet = []   
            for i in colorSet:
                tempColorSet = []
                for p in player.properties:
                    if p.position in i:
                        tempColorSet.append(p)
                propertySet.append(tempColorSet)
            #Adds the list of properties which a house is buyable on to monopolyProperties
            for i in propertySet:
                houseCounts = []
                for j in i:
                    houseCounts.append(j.house_count + 5 * j.hotel_count)
                maxHouses = min(min(houseCounts) + 1, 5)
                for k in i:
                    if k.house_count < maxHouses:
                        monopolyProperties.append(PropertyButton(k.position, player.playerNumber))
        #if the player owns at least 1 monopoly
        if set_of_monopolies:
            #if clicked on buttons to buy house/hotel
            for button in monopolyProperties:
                if button.mouseOn(mousePos):
                    if pygame.mouse.get_pressed()[0] == True:
                        endTurnClicked = True
                    if endTurnClicked:
                        #if released button, do action
                        if pygame.mouse.get_pressed()[0] == False:
                            endTurnClicked = False
                            #buy the house, subtract appropriate amount of cash from the player
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
                                        
        #sell house/mortgage property
        allProperties = []
        #text variables to display whether a property is mortgaged or not
        global morgagedIndicators
        global morgagedIndicatorRects
        #list of propertyButtons to represent each property owned by the player
        for p in player.properties:
            allProperties.append(PropertyButton(p.position, player.playerNumber))
        #create lists
        morgagedIndicators = []
        morgagedIndicatorRects = []
        propertyPositionsList = []
        sellableProperties = []
        mortgageableProperties = []
        #create list for property positions
        for prop in player.properties:
            propertyPositionsList.append(prop.position)
        #create list for properties apart of a monopoly
        set_of_monopolies = find_monopoly_set(propertyPositionsList)
        #create a list for properties which can be mortgaged
        for q in player.properties:
            if q.position not in set_of_monopolies:
                mortgageableProperties.append(q)
        #add properties which can be mortgaged to mortgageableProperties
        #if there is a house on the property, the property to sellableProperties instead
        colorSet = find_monopoly_sets_separated(propertyPositionsList)
        if colorSet:
            propertySet = []   
            for i in colorSet:
                tempPropSet = []
                for p in player.properties:
                    if p.position in i:
                        tempPropSet.append(p)
                propertySet.append(tempPropSet)
            for i in propertySet:
                houseCounts = []
                for j in i:
                    houseCounts.append(j.house_count + 5 * j.hotel_count)
                minHouses = max(max(houseCounts) - 1, -1)
                for k in i:
                    if k.house_count > minHouses:
                        if k.house_count > 0:
                            sellableProperties.append(k)
                        if k.house_count == 0:
                            mortgageableProperties.append(k)
        #for each property, add the mortgage indicator text to the moirtgagedIndicators list
        for button in allProperties:
            for p in player.properties:
                if p.position == button.position: #maybe unnecessary
                    if p.mortgaged == True:
                        Mfont = font.render("M", True, (255,140,0))
                        morgagedIndicators.append(Mfont)
                        MfontRect = Mfont.get_rect()
                        tempTuple = button.get_position()
                        if p.position in row1:
                            MfontRect.center = (tempTuple[0] + 33, tempTuple[1] + 68)
                        if p.position in row2:
                            MfontRect.center = (tempTuple[0] + 38, tempTuple[1] + 33)
                        if p.position in row3:
                            MfontRect.center = (tempTuple[0] + 33, tempTuple[1] + 38)
                        if p.position in row4:
                            MfontRect.center = (tempTuple[0] + 68, tempTuple[1] + 33)
                        morgagedIndicatorRects.append(MfontRect)
                    #if the mouse is on an owned property
                    #check for right click(our chosen bind for mortgaging a property)a
                    if button.mouseOn(mousePos):
                        if pygame.mouse.get_pressed()[2] == True:
                            sellPropertyClicked = True
                        if sellPropertyClicked:
                            #if released button, do action
                            if pygame.mouse.get_pressed()[2] == False:
                                sellPropertyClicked = False
                                #for each property the player owns:
                                for p2 in player.properties:
                                    if p2.position == button.position:
                                        houseCost = 0
                                        #set houseCost to be the amount of money the player gains/lose for selling a house/hotel or mortgaging/unmortgaging a property
                                        #if it is sellable, sell a house
                                        if p2 in sellableProperties:
                                            if p2.color == "Brown" or p2.color == "Light Blue":
                                                houseCost = 50
                                            elif p2.color == "Purple" or p2.color == "Orange":
                                                houseCost = 100
                                            elif p2.color == "Red" or p2.color == "Yellow":
                                                houseCost = 150
                                            elif p2.color == "Green" or p2.color == "Blue":
                                                houseCost = 200
                                            player.cash += (houseCost / 2)
                                            if p2.hotel_count == 1:
                                                p2.hotel_count = 0
                                                p2.house_count = 4
                                            else:
                                                p2.house_count -=1
                                        #if property is not mortgaged, mortgage property
                                        elif p2 in mortgageableProperties:
                                            p2.mortgaged = True
                                            player.cash += (p2.cost / 2)
                                        # if property is already mortgaged, unmortgage
                                        elif p2.mortgaged == True:
                                            p2.mortgaged = False
                                            player.cash -= (p2.cost / 2 * 1.1)

        #draw M for mortgaged properties
        for i in range(len(morgagedIndicators)):
            window.blit(morgagedIndicators[i], morgagedIndicatorRects[i])    
            
        #update money balance text
        if player.playerNumber == 1:    
            moneyText1 = font.render(f"${player.cash}", True, (0, 0, 0))
        elif player.playerNumber == 2:
            moneyText2 = font.render(f"${player.cash}", True, (0, 0, 0))

        #draw houses/hotels for each property
        house_sprites = pygame.sprite.Group()
        for prop in player.properties:
            if prop.isRailroad == False:
                house_sprites.add(house(prop.position, prop.house_count, prop.hotel_count))
        for i in house_sprites:
            for j in range(len(i.surfList)):
                window.blit(i.surfList[j], i.rectList[j])
                
        #if the property is unowned, give the player an option to end turn
        #this is necessary to force a player to either buy or auction when landing on an unowned property
        if onUnownedProperty == False:
            #if clicked on end turn button
            if 200 <= mousePos[0] <= 400 and 450 <= mousePos[1] <= 550: 
                if pygame.mouse.get_pressed()[0] == True:
                    endTurnClicked = True
                if endTurnClicked:
                    #if released button, do action
                    if pygame.mouse.get_pressed()[0] == False:
                        endTurnClicked = False
                        waitToEndTurn = False
                        #reset the announcement text
                        gameAnnouncementText = font.render(f"   ", True, (0,0,0))
                        
        #neccessary for async functions. #required for web hosting
        await asyncio.sleep(0)  # Let other tasks run


async def main():
    """
    Runs the main game loop 

    Parameters:
    None
    Returns:
    None
    """
    #explicitly use the existing global variables
    global clicked
    global gameAnnouncementText
    global gameAnnouncement_rect
    global players
    global playerCount
    global turnCounter
    global rolls
    global morgagedIndicators
    global morgagedIndicatorRects
    
    #bool for if the game a player has lost
    gameOver = False
    playerLoseString = ""
    
    #main game update function
    while True:
        #draw background window
        window.blit(bg_img,(0,0))
        #if player quits game, close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
                
        #display player balance info
        window.blit(moneyText1, text_rect1)
        window.blit(moneyText2, text_rect2)
        
        #display the game announcement
        window.blit(gameAnnouncementText, gameAnnouncement_rect)
        
        #mouse coords
        mousePos = pygame.mouse.get_pos()
        
        #draw the colored tint used to denote a property is owned by a player
        drawPropertyButtons(P1, P2, window)
        
        #draw houses for each property with houses
        house_sprites = pygame.sprite.Group()
        for player in players:
            for prop in player.properties:
                if prop.isRailroad == False:
                    house_sprites.add(house(prop.position, prop.house_count, prop.hotel_count))
            for i in house_sprites:
                for j in range(len(i.surfList)):
                    window.blit(i.surfList[j], i.rectList[j])
                    
        #draw M for mortgaged properties
        for i in range(len(morgagedIndicators)):
            window.blit(morgagedIndicators[i], morgagedIndicatorRects[i])    
            
        #if player run out of money, make them lose, end the game
        for p in players:
            if p.cash < 0:
                gameOver = True
                playerLoserString = p.playerNumber
                
        #if hit dice button
        if 200 <= mousePos[0] <= 400 and 450 <= mousePos[1] <= 550: 
            if pygame.mouse.get_pressed()[0] == True:
                clicked = True
            if clicked:
                #if released button, do action
                if pygame.mouse.get_pressed()[0] == False:
                    clicked = False
                    #get rid of game announcement text
                    gameAnnouncementText = font.render(f"  ", True, (0,0,0))
                    #roll dice twice
                    rolls = [roll.dice_roll(), roll.dice_roll()]  
                    #turn counter for keeping track of whose turn it is
                    #playerTurn = turn action function
                    if gameOver == False:
                        #activate function for a player's turn
                        await playerTurn(players[turnCounter], rolls)
                    #if a player rolls doubles, it is their turn again
                    if players[turnCounter].rolledDoubles:
                        turnCounter -= 1
                    #update the players turn
                    turnCounter += 1
                    if turnCounter >= playerCount:
                        turnCounter = 0
                        
        #if a player has lost:
        #display that the player has lost as an announcement
        #display my life's moto
        if gameOver:
            displayText = "Player" + playerLoseString + "Loses"
            gameAnnouncementText = font.render(displayText, True, (0,0,0))
            gameAnnouncement_rect = gameAnnouncementText.get_rect()
            gameAnnouncement_rect.center = (400, 300)
            endText = font.render("Graphics Design is My Passion!", True, (0,0,0))
            endTextRect = endText.get_rect()
            endTextRect.center = (400, 700)
            window.blit(endText, endTextRect)
        
        
        #display player and dice sprites
        for entity in all_sprites:
            window.blit(entity.surf, entity.rect)
        pygame.display.update()
        await asyncio.sleep(0)  # This line is critical; ensure you keep the sleep time at 0
#calls the main loop to run
asyncio.run(main())

