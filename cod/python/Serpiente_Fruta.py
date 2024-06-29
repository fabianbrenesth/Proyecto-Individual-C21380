# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 21:58:06 2024

@author: Fabian
"""
import pygame,random
from pygame.math import Vector2

class FRUIT:
	def __init__(self, cell_number):
        """
        Inicializa la fruta en una posición aleatoria.

        Parameters
        --------------
        cell_number (int): Número de celdas en la cuadrícula.

        Returns
        -------------
        No devuelve nada.
        """
		self.randomize(cell_number)

	def draw_fruit(self, cell_size, screen, apple):
        """
        Dibuja la fruta en la pantalla.

        Parameters
        --------------
        cell_size (int): Tamaño de cada celda en la cuadrícula.
        screen (pygame.Surface): La superficie en la que se dibuja la fruta.
        apple (pygame.Surface): La imagen de la fruta.

        Returns
        -------------
        No devuelve nada.
        """
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(apple,fruit_rect)
		#pygame.draw.rect(screen,(126,166,114),fruit_rect)

	def randomize(self, cell_number):
        """
        Ubica la fruta en una posición aleatoria en la cuadrícula.

        Parameters
        --------------
        cell_number (int): Número de celdas en la cuadrícula.

        Returns
        -------------
        No devuelve nada.
        """
		self.x = random.randint(0,cell_number - 1)
		self.y = random.randint(0,cell_number - 1)
		self.pos = Vector2(self.x,self.y)