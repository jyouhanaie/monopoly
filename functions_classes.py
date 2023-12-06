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
        

class PropertyButton(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.vertical_buttons = [2, 4, 6, 9, 10, 22, 24, 25, 27, 28, 30]
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
        if position in self.vertical_buttons:
            if self.get_position(self.position)[0] < mousePos[0] < self.get_position(self.position)[0] + 65 and
            self.get_position(self.position)[1] < mousePos[1] < self.get_position(self.position)[1] + 110:
                return True
        else:
            if self.get_position(self.position)[0] < mousePos[0] < self.get_position(self.position)[0] + 110 and
            self.get_position(self.position)[1] < mousePos[1] < self.get_position(self.position)[1] + 65:
                return True
        return False


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
        
        
def find_monopoly_set(property_positions):
    for color, positions in color_groups.items():
        if all(position in property_positions for position in positions):
            return [position for position in positions if position in property_positions]

    return []

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
        self.rolledDoubled = False
        self.doublesCounter = 0
        self.injail = False
        self.jailCounter = 0
        
        
    def get_position(self):
        return self.position
    
    def add_position(self, addValue):
        self.position = self.position + addValue;
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


def playerTurn(player, rolls):
    global moneyText1
    global moneyText2
    global gameAnnouncementText
    global gameAnnouncement_rect
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
            roll_sum = sum(rolls)
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
                    event = pygame.event.wait()
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
                                     player.properties[-1].house_count += 1;
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
                                    
                            
                    

            if 200 <= mousePos[0] <= 400 and 450 <= mousePos[1] <= 550: 
                if pygame.mouse.get_pressed()[0] == True:
                    endTurnClicked = True
                if endTurnClicked:
                    #if released button, do action
                    if pygame.mouse.get_pressed()[0] == False:
                        endTurnClicked = False
                        waitToEndTurn = False
        for i in range(len(buttonsToDraw)):
            all_sprites.remove(buttonsToDraw[i])