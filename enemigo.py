import pygame

# Clase Enemigo que representa a un enemigo en el juego.
class Enemigo:
    # Constructor de la clase Enemigo.
    # Inicializa las propiedades del enemigo como su posición, tamaño y velocidad.
    def __init__(self, x, y):
        self.x = x  # Coordenada x del enemigo en la pantalla.
        self.y = y  # Coordenada y del enemigo en la pantalla.
        self.ancho = 65  # Ancho del rectángulo que representa al enemigo.
        self.alto = 65  # Alto del rectángulo que representa al enemigo.
        self.velocidad = 5  # Velocidad a la que el enemigo se moverá hacia abajo.
        self.color = "purple"  # Color del enemigo (el rectángulo será de color púrpura).
        # Se crea un objeto Rect de pygame que representa el área ocupada por el enemigo.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)

    # Método para dibujar al enemigo en la ventana.
    # Recibe la ventana donde debe dibujarse y luego dibuja un rectángulo que representa al enemigo.
    def dibujar(self, ventana):
        # Actualiza la posición del rectángulo antes de dibujarlo (por si el enemigo se mueve).
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # Dibuja el rectángulo en la ventana con el color especificado.
        pygame.draw.rect(ventana, self.color, self.rect)

    # Método para mover al enemigo.
    # Este movimiento solo afecta la coordenada y, desplazando al enemigo hacia abajo.
    def movimiento(self):
        self.y += self.velocidad  # Aumenta la coordenada y, moviendo al enemigo hacia abajo.
