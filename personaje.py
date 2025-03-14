import pygame  # Importamos la biblioteca pygame para manejar gráficos y eventos.

class Cubo:
    def __init__(self, x, y):
        """
        Crea un cubo con una posición inicial.
        
        Parámetros:
        x (int): Posición horizontal del cubo.
        y (int): Posición vertical del cubo.
        """
        self.x = x  
        self.y = y  
        self.ancho = 50  
        self.alto = 50  
        self.velocidad = 10  
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)  

        try:
            self.imagen = pygame.image.load("imagenes/nave.png")  # Asegúrate de que la imagen sea PNG con fondo transparente
            self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
            self.imagen = self.imagen.convert_alpha()  # Convierte la imagen para manejar la transparencia
        except pygame.error as e:
            print(f"Error al cargar la imagen: {e}")
            self.imagen = None  # Evita errores si no se encuentra la imagen

    def dibujar(self, ventana):
        self.rect.topleft = (self.x, self.y)  # Actualiza la posición del rectángulo (para colisiones)

        if self.imagen:
            ventana.blit(self.imagen, (self.x, self.y))  # Dibuja la imagen con transparencia

