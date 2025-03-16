import pygame  # Importa el módulo pygame para usar sus funcionalidades en el juego
import random  # Importa el módulo random para generar valores aleatorios

class PowerUp:  # Define la clase PowerUp, que representa un objeto de potenciador en el juego
    def __init__(self, x, y):  # Constructor que inicializa las posiciones (x, y) del potenciador
        self.x = x  # Coordenada X de la posición inicial del potenciador
        self.y = y  # Coordenada Y de la posición inicial del potenciador
        self.ancho = 20  # El ancho del potenciador (tamaño del rectángulo)
        self.alto = 20  # El alto del potenciador (tamaño del rectángulo)
        self.color = (0, 255, 0)  # Color del potenciador (verde en este caso)
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)  # Crea un objeto Rectángulo para manejar la posición y el tamaño

    def dibujar(self, ventana):  # Método para dibujar el potenciador en la ventana
        pygame.draw.rect(ventana, self.color, self.rect)  # Dibuja el rectángulo en la ventana con el color especificado
    
    def movimiento(self):  # Método para actualizar la posición del potenciador (simulando la caída)
        self.y += 2  # Aumenta la coordenada Y, haciendo que el potenciador "caiga" hacia abajo
        self.rect.y = self.y  # Actualiza la posición del rectángulo con la nueva coordenada Y
