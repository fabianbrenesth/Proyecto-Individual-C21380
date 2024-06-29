# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:28:49 2024

@author: Fabian
"""

import pygame
import random

from _2048_Cuadros import Tile

class GAME:
    def __init__(self, window, RECT_WIDTH, RECT_HEIGHT, COLS, ROWS):
        """
        Inicializa el juego con los parámetros dados.

        Parameters
        --------------
        window (pygame.Surface): La ventana del juego.
        RECT_WIDTH (int): Ancho de los rectángulos de las fichas.
        RECT_HEIGHT (int): Altura de los rectángulos de las fichas.
        COLS (int): Número de columnas en la cuadrícula.
        ROWS (int): Número de filas en la cuadrícula.

        Returns
        -------------
        No devuelve nada.
        """
        self.window = window
        self.RECT_WIDTH = RECT_WIDTH
        self.RECT_HEIGHT = RECT_HEIGHT
        self.COLS = COLS
        self.ROWS = ROWS
        self.tiles = {}
        self.tiles = self.generate_tiles()

    def draw_grid(self, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT):
        """
        Dibuja la cuadrícula del juego en la ventana.

        Parameters
        --------------
        OUTLINE_COLOR (tuple): Color de las líneas de la cuadrícula.
        OUTLINE_THICKNESS (int): Grosor de las líneas de la cuadrícula.
        WIDTH (int): Ancho de la ventana.
        HEIGHT (int): Altura de la ventana.

        Returns
        -------------
        No devuelve nada.
        """
        for row in range(1, self.ROWS):
            y = row * self.RECT_HEIGHT
            pygame.draw.line(self.window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)

        for col in range(1, self.COLS):
            x = col * self.RECT_WIDTH
            pygame.draw.line(self.window, OUTLINE_COLOR, (x, 0), (x, HEIGHT), OUTLINE_THICKNESS)

        pygame.draw.rect(self.window, OUTLINE_COLOR, (0, 0, WIDTH, HEIGHT), OUTLINE_THICKNESS)

    def draw(self, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT):
        """
        Dibuja el estado actual del juego en la ventana.

        Parameters
        --------------
        BACKGROUND_COLOR (tuple): Color de fondo de la ventana.
        FONT (pygame.font.Font): Fuente para renderizar los valores de las fichas.
        FONT_COLOR (tuple): Color de los valores de las fichas.
        OUTLINE_COLOR (tuple): Color de las líneas de la cuadrícula.
        OUTLINE_THICKNESS (int): Grosor de las líneas de la cuadrícula.
        WIDTH (int): Ancho de la ventana.
        HEIGHT (int): Altura de la ventana.

        Returns
        -------------
        No devuelve nada.
        """
        self.window.fill(BACKGROUND_COLOR)

        for tile in self.tiles.values():
            tile.draw(self.window, FONT, FONT_COLOR)

        self.draw_grid(OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)

        pygame.display.update()

    def get_random_pos(self):
        """
        Obtiene una posición aleatoria en la cuadrícula que no esté ocupada por una ficha.

        Parameters
        --------------
        No tiene parámetros.

        Returns
        -------------
        tuple: Fila y columna aleatoria.
        """
        row = None
        col = None
        while True:
            row = random.randrange(0, self.ROWS)
            col = random.randrange(0, self.COLS)

            if f"{row}{col}" not in self.tiles:
                break

        return row, col

    def move_tiles(self, direction, clock, MOVE_VEL, FPS, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT):
        """
        Mueve las fichas en la dirección especificada y actualiza el estado del juego.

        Parameters
        --------------
        direction (str): Dirección en la que mover las fichas ('left', 'right', 'up', 'down').
        clock (pygame.time.Clock): Reloj del juego para controlar la velocidad de movimiento.
        MOVE_VEL (int): Velocidad de movimiento de las fichas.
        FPS (int): Cuadros por segundo del juego.
        BACKGROUND_COLOR (tuple): Color de fondo de la ventana.
        FONT (pygame.font.Font): Fuente para renderizar los valores de las fichas.
        FONT_COLOR (tuple): Color de los valores de las fichas.
        OUTLINE_COLOR (tuple): Color de las líneas de la cuadrícula.
        OUTLINE_THICKNESS (int): Grosor de las líneas de la cuadrícula.
        WIDTH (int): Ancho de la ventana.
        HEIGHT (int): Altura de la ventana.

        Returns
        -------------
        str: Estado del juego ('continue' o 'lost').
        """
        updated = True
        blocks = set()

        if direction == "left":
            sort_func = lambda x: x.col
            reverse = False
            delta = (-MOVE_VEL, 0)
            boundary_check = lambda tile: tile.col == 0
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row}{tile.col - 1}")
            merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
            move_check = (
                lambda tile, next_tile: tile.x > next_tile.x + self.RECT_WIDTH + MOVE_VEL
            )
            ceil = True
        elif direction == "right":
            sort_func = lambda x: x.col
            reverse = True
            delta = (MOVE_VEL, 0)
            boundary_check = lambda tile: tile.col == self.COLS - 1
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row}{tile.col + 1}")
            merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
            move_check = (
                lambda tile, next_tile: tile.x + self.RECT_WIDTH + MOVE_VEL < next_tile.x
            )
            ceil = False
        elif direction == "up":
            sort_func = lambda x: x.row
            reverse = False
            delta = (0, -MOVE_VEL)
            boundary_check = lambda tile: tile.row == 0
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row - 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
            move_check = (
                lambda tile, next_tile: tile.y > next_tile.y + self.RECT_HEIGHT + MOVE_VEL
            )
            ceil = True
        elif direction == "down":
            sort_func = lambda x: x.row
            reverse = True
            delta = (0, MOVE_VEL)
            boundary_check = lambda tile: tile.row == self.ROWS - 1
            get_next_tile = lambda tile: self.tiles.get(f"{tile.row + 1}{tile.col}")
            merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
            move_check = (
                lambda tile, next_tile: tile.y + self.RECT_HEIGHT + MOVE_VEL < next_tile.y
            )
            ceil = False

        while updated:
            clock.tick(FPS)
            updated = False
            sorted_tiles = sorted(self.tiles.values(), key=sort_func, reverse=reverse)

            for i, tile in enumerate(sorted_tiles):
                if boundary_check(tile):
                    continue

                next_tile = get_next_tile(tile)
                if not next_tile:
                    tile.move(delta)
                elif (
                    tile.value == next_tile.value
                    and tile not in blocks
                    and next_tile not in blocks
                ):
                    if merge_check(tile, next_tile):
                        tile.move(delta)
                    else:
                        next_tile.value *= 2
                        sorted_tiles.pop(i)
                        blocks.add(next_tile)
                elif move_check(tile, next_tile):
                    tile.move(delta)
                else:
                    continue

                tile.set_pos(ceil)
                updated = True

            self.update_tiles(sorted_tiles, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)

        return self.end_move()

    def end_move(self):
        """
        Finaliza el movimiento, añade una nueva ficha si hay espacio.

        Parameters
        --------------
        No tiene parámetros.

        Returns
        -------------
        str: Estado del juego ('continue' o 'lost').
        """
        if len(self.tiles) == 16:
            return "lost"

        row, col = self.get_random_pos()
        self.tiles[f"{row}{col}"] = Tile(random.choice([2, 4]), row, col, self.RECT_WIDTH, self.RECT_HEIGHT)
        return "continue"

    def update_tiles(self, sorted_tiles, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT):
        """
        Actualiza las fichas en el estado del juego.

        Parameters
        --------------
        sorted_tiles (list): Lista de fichas ordenadas.
        BACKGROUND_COLOR (tuple): Color de fondo de la ventana.
        FONT (pygame.font.Font): Fuente para renderizar los valores de las fichas.
        FONT_COLOR (tuple): Color de los valores de las fichas.
        OUTLINE_COLOR (tuple): Color de las líneas de la cuadrícula.
        OUTLINE_THICKNESS (int): Grosor de las líneas de la cuadrícula.
        WIDTH (int): Ancho de la ventana.
        HEIGHT (int): Altura de la ventana.

        Returns
        -------------
        No devuelve nada.
        """
        self.tiles.clear()
        for tile in sorted_tiles:
            self.tiles[f"{tile.row}{tile.col}"] = tile

        self.draw(BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)

    def generate_tiles(self):
        """
        Genera las fichas iniciales del juego.

        Parameters
        --------------
        No tiene parámetros.

        Returns
        -------------
        dict: Diccionario con las fichas iniciales.
        """
        tiles = {}
        for _ in range(2):
            row, col = self.get_random_pos()
            tiles[f"{row}{col}"] = Tile(2, row, col, self.RECT_WIDTH, self.RECT_HEIGHT)

        return tiles