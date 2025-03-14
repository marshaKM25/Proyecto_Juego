import pygame  # Importamos la biblioteca pygame para manejar gráficos y eventos.

# Clase Bala que representa una bala en el juego.
class Bala:
    # Constructor de la clase Bala.
    # Inicializa las propiedades de la bala como su posición, tamaño, velocidad y color.
    def __init__(self, x, y):
        self.x = x  # Coordenada x de la bala en la pantalla.
        self.y = y  # Coordenada y de la bala en la pantalla.
        self.ancho = 20  # Ancho de la imagen que representa la bala.
        self.alto = 20   # Alto de la imagen que representa la bala.
        self.velocidad = 10  # Velocidad a la que la bala se moverá hacia arriba.
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)  # Rectángulo que representa la posición de la bala.

        # Cargar la imagen de la bala (asegúrate de que la imagen sea PNG con fondo transparente).
        try:
            self.imagen = pygame.image.load("imagenes/bala.png")  # Ruta a la imagen de la bala con fondo transparente.
            self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))  # Redimensiona la imagen
            self.imagen = self.imagen.convert_alpha()  # Convierte la imagen para manejar la transparencia.
        except pygame.error as e:
            print(f"Error al cargar la imagen de la bala: {e}")
            self.imagen = None  # Si no se carga la imagen, se evita un error.

    # Método para dibujar la bala en la ventana.
    def dibujar(self, ventana):
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rectángulo antes de dibujarlo (por si se mueve).
        if self.imagen:
            ventana.blit(self.imagen, (self.x, self.y))  # Dibuja la imagen de la bala
        else:
            pygame.draw.rect(ventana, (255, 255, 255), self.rect)  # Si no se carga la imagen, dibuja un rectángulo blanco (como fallback).

    # Método para mover la bala.
    # Este movimiento solo afecta la coordenada y, desplazando la bala hacia arriba.
    def movimiento(self):
        self.y -= self.velocidad  # Disminuye la coordenada y, moviendo la bala hacia arriba.
