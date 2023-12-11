import pygame
from pygame.locals import *
import sprites
from sprites import PropertyButton

# define the color groups to be referenced when finding monopolies
color_groups = {
    "Brown": [2, 4],
    "Light Blue": [7, 9, 10],
    "Pink": [12, 14, 15],
    "Orange": [17, 19, 20],
    "Red": [22, 24, 25],
    "Yellow": [27, 28, 30],
    "Green": [32, 33, 35],
    "Blue": [38, 40]}

def find_monopoly_set(property_positions):
    '''
    Finds all monopolies a player owns

    property_positions is a list of ints which represent the positions of the properties the player owns
    
    returns a list containing the int positions of all the properties the player owns that are part of a monopoly 
    '''
    # checks every color in color_groups and checks if the player owns all the properties in any group
    # returns a list containing the int positions of all the properties the player owns that are part of a monopoly
    for color, positions in color_groups.items():
        if all(position in property_positions for position in positions):
            return [position for position in positions if position in property_positions]
    
    #if the player has no monopolies, returns an empty list 
    return []

def find_monopoly_sets_separated(property_positions):
    '''
    Finds all monopolies a player owns

    property_positions is a list of ints which represent the positions of the properties the player owns
    
    returns a list of lists containing the int positions of all the properties the player owns that are part of a monopoly
    grouped by monopoly set
    '''
    # define an empty list to be appended with lists of monopolies owned by the player
    all_sets = []
    # checks every color in color_groups and checks if the player owns all the properties in any group
    for color, positions in color_groups.items():
        if all(position in property_positions for position in positions):
            # gets a list of the int positions of all the properties the player owns that are part of one of his monopolies
            color_set = [position for position in positions if position in property_positions]
            
            # appends that list to the list of all monopolies the player owns
            all_sets.append(sorted(color_set))
    
    return all_sets

def drawPropertyButtons(P1, P2, window):
    '''
    Adds all PropertyButton objects corresponding to the properties each player owns to the list of sprites to be drawn and
    then draws each of these objects using the blit method

    P1 is the first Player object to get properties from
    P2 is the second Player object to get properties from
    window is the pygame.display.set_mode object on which all sprites are being blitted/drawn
    '''
    all_property_sprites1 = pygame.sprite.Group()
    all_property_sprites2 = pygame.sprite.Group()

    for p in P1.properties:
        all_property_sprites1.add(PropertyButton(p.position, P1.playerNumber))
    for p in P2.properties:
        all_property_sprites2.add(PropertyButton(p.position, P2.playerNumber))

    for i in all_property_sprites1:
        window.blit(i.image, i.rect)
    for i in all_property_sprites2:
        window.blit(i.image, i.rect)
