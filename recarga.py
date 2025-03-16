import pygame
import random

class Recarga:
    def __init__(self, x, y):
        self.imagen = pygame.image.load("imagenes/recarga.png")  # Asegúrate de tener esta imagen
        self.imagen = pygame.transform.scale(self.imagen, (50, 50))  # Redimensiona la imagen (50x50 píxeles)
        self.rect = self.imagen.get_rect(topleft=(x, y))
        self.velocidad = 2  # Velocidad con la que cae el ítem

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect)

    def movimiento(self):
        self.rect.y += self.velocidad  # Mueve el ítem hacia abajo

    def fuera_de_pantalla(self):
        """Verifica si el ítem de recarga se ha salido de la pantalla por abajo."""
        return self.rect.y > ALTO  # Si la posición 'y' del rectángulo es mayor que el alto de la pantalla

def generar_recarga():
    """Genera un ítem de recarga dentro de los límites de la pantalla."""
    x = random.randint(0, ANCHO - 50)  # Asegura que el ítem no se salga por los bordes
    return Recarga(x, -50)  # Se genera fuera de la pantalla, en la parte superior
