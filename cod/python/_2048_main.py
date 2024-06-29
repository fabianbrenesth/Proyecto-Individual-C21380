# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 10:03:22 2024

@author: Fabian
"""

import pygame

from _2048_Juego import GAME

#Inicializa el juego
pygame.init()

#Variables a utilizar

FPS = 60  #frames per second, que tan rapido corre el juego

WIDTH, HEIGHT = 800, 800  #dimensiones de la ventana
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // ROWS
RECT_WIDTH = WIDTH // COLS

OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
BACKGROUND_COLOR = (205, 192, 180)
FONT_COLOR = (119, 110, 101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20  #velocidad a la que se mueven las fichas

# La ventana donde van a salir las cosas
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")


def run_2048_game():
    """
    Función principal para ejecutar el juego 2048.
    
    Inicia el bucle principal del juego y gestiona los eventos y la lógica del juego.
    """
    def main(window):
        """
        Bucle principal del juego.

        Parameters
        --------------
        window (pygame.Surface): La ventana del juego.

        Returns
        -------------
        No devuelve nada.
        """
        clock = pygame.time.Clock()
        run = True

        game = GAME(window, RECT_WIDTH, RECT_HEIGHT, COLS, ROWS)

        while run:
            clock.tick(FPS)  # ASI LA VELOCIDAD ES LA MISMA SIEMPRE SIN IMPORTAR LA COMPU

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # SI SE LE DA A EXIT SE ACABA
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        game.move_tiles("left", clock, MOVE_VEL, FPS, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)
                    if event.key == pygame.K_RIGHT:
                        game.move_tiles("right", clock, MOVE_VEL, FPS, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)
                    if event.key == pygame.K_UP:
                        game.move_tiles("up", clock, MOVE_VEL, FPS, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)
                    if event.key == pygame.K_DOWN:
                        game.move_tiles("down", clock, MOVE_VEL, FPS, BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)

            game.draw(BACKGROUND_COLOR, FONT, FONT_COLOR, OUTLINE_COLOR, OUTLINE_THICKNESS, WIDTH, HEIGHT)

        pygame.quit()

    main(WINDOW)


if __name__ == "__main__":
    run_2048_game()