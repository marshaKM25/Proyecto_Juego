import pygame
import random

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.color = (0, 255, 0)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
    
    def dibujar(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)
    
    def movimiento(self):
        self.y += 2  # Velocidad de caída
        self.rect.y = self.y
