# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:01:13 2024

@author: Fabian
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPixmap, QPalette, QBrush
from PyQt5.QtCore import Qt
import subprocess

class MainWindow(QWidget):
    def __init__(self):
        """
        Inicializa la ventana principal, configura el título, el tamaño y los elementos de la interfaz.
        
        Parameters
        --------------
        No tiene parámetros.
        
        Returns
        -------------
        No devuelve nada.
        """
        super().__init__()

        self.setWindowTitle("Juegos")
        self.setFixedSize(500, 400)
        
        # Para agregar la imágen de fondo
        palette = QPalette()
        bg_image = QPixmap("Graphics/background1.jpeg").scaled(self.size(), Qt.IgnoreAspectRatio)
        palette.setBrush(QPalette.Background, QBrush(bg_image))
        self.setPalette(palette)

        layout = QVBoxLayout()

        # Títulos
        title_label = QLabel("Seleccione un juego:")
        title_label.setFont(QFont('Helvetica', 20, QFont.Bold))
        title_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 0.6); padding: 10px; border-radius: 5px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Botones
        btn_2048 = QPushButton("Jugar 2048")
        btn_2048.setFont(QFont('Helvetica', 14))
        btn_2048.setStyleSheet("background-color: rgba(0, 0, 0, 0.6); color: white; padding: 10px; border-radius: 5px;")
        btn_2048.clicked.connect(self.run_2048_game)
        layout.addWidget(btn_2048, alignment=Qt.AlignCenter)

        btn_snake = QPushButton("Jugar Serpiente")
        btn_snake.setFont(QFont('Helvetica', 14))
        btn_snake.setStyleSheet("background-color: rgba(0, 0, 0, 0.6); color: white; padding: 10px; border-radius: 5px;")
        btn_snake.clicked.connect(self.run_snake_game)
        layout.addWidget(btn_snake, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def run_2048_game(self):
        """
        Ejecuta el juego 2048.

        Parameters
        --------------
        No tiene parámetros.
        
        Returns
        -------------
        No devuelve nada.
        """
        self.close()
        subprocess.run([sys.executable, '_2048_main.py'])

    def run_snake_game(self):
        """
        Ejecuta el juego de la serpiente.

        Parameters
        --------------
        No tiene parámetros.
        
        Returns
        -------------
        No devuelve nada.
        """
        self.close()
        subprocess.run([sys.executable, 'Serpiente_main.py'])
        

def main():
    """
    Función principal para ejecutar la aplicación de la interfaz de selección de juegos.

    Parameters
    --------------
    No tiene parámetros.
    
    Returns
    -------------
    No devuelve nada.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()