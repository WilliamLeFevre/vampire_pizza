import pygame
from pygame import *

pygame.init()

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH, WINDOW_HEIGHT)

GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption("Attack of the Vampire Pizzas!")

pizza_img = image.load("game_assets/vampire.png")
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100, 100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900, 400))

draw.circle(GAME_WINDOW, (255, 0, 0), (925, 425), 25, 0)

draw.rect(GAME_WINDOW, (160, 82, 45), (890, 390, 125, 125), 5)
draw.rect(GAME_WINDOW, (160, 82, 45), (890, 265, 125, 125), 0)

game_running = True

while game_running:

    for event in pygame.event.get():

        if event.type == QUIT:
            game_running = False
        display.update()

pygame.quit()