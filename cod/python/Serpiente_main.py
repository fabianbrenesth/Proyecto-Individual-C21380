# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:21:09 2024

@author: Fabian
"""

import pygame,sys
from pygame.math import Vector2

from Serpiente_Juego import GAME

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#Correr todo el juego  
def run_snake_game():
    main_game = GAME(cell_number)
    
    while True:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			pygame.quit()
    			sys.exit()
    		if event.type == SCREEN_UPDATE:
    			main_game.update(cell_number)
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_UP:
    				if main_game.snake.direction.y != 1:
    					main_game.snake.direction = Vector2(0,-1)
    			if event.key == pygame.K_RIGHT:
    				if main_game.snake.direction.x != -1:
    					main_game.snake.direction = Vector2(1,0)
    			if event.key == pygame.K_DOWN:
    				if main_game.snake.direction.y != -1:
    					main_game.snake.direction = Vector2(0,1)
    			if event.key == pygame.K_LEFT:
    				if main_game.snake.direction.x != 1:
    					main_game.snake.direction = Vector2(-1,0)
    
    	screen.fill((175,215,70))
    	main_game.draw_elements(cell_size, screen, apple, cell_number, game_font)
    	pygame.display.update()
    	clock.tick(60)

#Solo si se escoge se corre        
if __name__ == "__main__":
    run_snake_game()