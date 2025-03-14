import pygame  # Importamos la biblioteca pygame para manejar gráficos y eventos.

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
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)  # Rectángulo que representa la posición del enemigo

        # Cargar la imagen del enemigo (asegúrate de que la imagen sea PNG con fondo transparente).
        try:
            self.imagen = pygame.image.load("imagenes/enemigo.png")  # Ruta a la imagen con fondo transparente
            self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))  # Redimensiona la imagen
            self.imagen = self.imagen.convert_alpha()  # Convierte la imagen para manejar la transparencia
        except pygame.error as e:
            print(f"Error al cargar la imagen del enemigo: {e}")
            self.imagen = None  # Si la imagen no se carga, se evita un error

    # Método para dibujar al enemigo en la ventana.
    def dibujar(self, ventana):
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rectángulo antes de dibujarlo (por si se mueve).
        if self.imagen:
            ventana.blit(self.imagen, (self.x, self.y))  # Dibuja la imagen del enemigo
        else:
            pygame.draw.rect(ventana, (255, 0, 0), self.rect)  # Si no se carga la imagen, dibuja un rectángulo rojo (como fallback).

    # Método para mover al enemigo.
    def movimiento(self):
        self.y += self.velocidad  # Aumenta la coordenada y, moviendo al enemigo hacia abajo.

