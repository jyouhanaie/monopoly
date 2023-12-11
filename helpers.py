import pygame
from pygame.locals import *
import sprites
from sprites import PropertyButton

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
    for color, positions in color_groups.items():
        if all(position in property_positions for position in positions):
            return [position for position in positions if position in property_positions]
    return []

def find_monopoly_sets_separated(property_positions):
    all_sets = []
    for color, positions in color_groups.items():
        if all(position in property_positions for position in positions):
            color_set = [position for position in positions if position in property_positions]
            all_sets.append(sorted(color_set))
    return all_sets

def drawPropertyButtons(P1, P2, window):
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
