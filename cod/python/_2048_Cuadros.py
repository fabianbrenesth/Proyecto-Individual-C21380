# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:13:13 2024

@author: Fabian
"""
import pygame
import math

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value, row, col, RECT_WIDTH, RECT_HEIGHT):
        """
        Construye el objeto Tile (Cuadro).

        Parameters
        --------------
        value (int): Valor de la ficha.
        row (int): Fila de la ficha.
        col (int): Columna de la ficha.
        RECT_WIDTH (int): Ancho del rectángulo de la ficha.
        RECT_HEIGHT (int): Altura del rectángulo de la ficha.

        Returns
        -------------
        No devuelve nada.
        """
        self.value = value
        self.row = row
        self.col = col
        self.RECT_WIDTH = RECT_WIDTH
        self.RECT_HEIGHT = RECT_HEIGHT
        self.x = col * RECT_WIDTH
        self.y = row * RECT_HEIGHT

    def get_color(self):
        """
        Obtiene el color de la ficha basado en su valor.

        Parameters
        --------------
        No tiene parámetros.

        Returns
        -------------
        tuple: El color correspondiente al valor de la ficha.
        """
        color_index = int(math.log2(self.value)) - 1
        color = self.COLORS[color_index]
        return color

    def draw(self, window, FONT, FONT_COLOR):
        """
        Dibuja la ficha en la ventana del juego.

        Parameters
        --------------
        window (pygame.Surface): La ventana donde se dibuja la ficha.
        FONT (pygame.font.Font): La fuente para renderizar el texto del valor de la ficha.
        FONT_COLOR (tuple): El color del texto del valor de la ficha.

        Returns
        -------------
        No devuelve nada.
        """
        color = self.get_color()
        pygame.draw.rect(window, color, (self.x, self.y, self.RECT_WIDTH, self.RECT_HEIGHT))

        text = FONT.render(str(self.value), 1, FONT_COLOR)
        window.blit(
            text,
            (
                self.x + (self.RECT_WIDTH / 2 - text.get_width() / 2),
                self.y + (self.RECT_HEIGHT / 2 - text.get_height() / 2),
            ),
        )

    def set_pos(self, ceil=False):
        """
        Establece la posición de la ficha en la cuadrícula.

        Parameters
        --------------
        ceil (bool): Si es True, redondea hacia arriba al calcular la fila y columna.

        Returns
        -------------
        No devuelve nada.
        """
        if ceil:
            self.row = math.ceil(self.y / self.RECT_HEIGHT)
            self.col = math.ceil(self.x / self.RECT_WIDTH)
        else:
            self.row = math.floor(self.y / self.RECT_HEIGHT)
            self.col = math.floor(self.x / self.RECT_WIDTH)

    def move(self, delta):
        """
        Mueve la ficha en la cuadrícula.

        Parameters
        --------------
        delta (tuple): Desplazamiento en x e y.

        Returns
        -------------
        No devuelve nada.
        """
        self.x += delta[0]
        self.y += delta[1]