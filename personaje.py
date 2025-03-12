import pygame  # Importamos la biblioteca pygame para manejar gráficos y eventos.

class Cubo:
    def __init__(self, x, y):
        """
        Crea un cubo con una posición inicial.
        
        Parámetros:
        x (int): Posición horizontal del cubo.
        y (int): Posición vertical del cubo.
        """
        self.x = x  # Guarda la posición en X
        self.y = y  # Guarda la posición en Y
        self.ancho = 50  # Define el ancho del cubo
        self.alto = 50  # Define el alto del cubo
        self.velocidad = 10  # Velocidad con la que se moverá el cubo
        self.color = "red"  # Color del cubo
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)  # Crea un rectángulo que representa el cubo

    def dibujar(self, ventana):
        """
        Dibuja el cubo en la pantalla.
        
        Parámetros:
        ventana (pygame.Surface): La ventana donde se dibujará el cubo.
        """
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)  # Actualiza el rectángulo con la posición actual
        pygame.draw.rect(ventana, self.color, self.rect)  # Dibuja el cubo en la ventana con su color y forma
