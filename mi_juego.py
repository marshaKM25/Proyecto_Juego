import pygame
from personaje import Cubo
from enemigo import Enemigo
import random

pygame.init()

# pip install pygame

ANCHO = 500
ALTO = 500
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60
FUENTE = pygame.font.SysFont("Comic Sans", 40)

jugando = True

reloj = pygame.time.Clock()

vida = 5
puntos = 0

tiempo_pasado = 0
tiempo_entre_enemigos = 500
cubo = Cubo(ANCHO / 2, ALTO - 75)
enemigos = []

# Función para gestionar el movimiento del jugador
def gestionar_teclas(teclas):
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad

# Bucle principal del juego
while jugando and vida > 0:

    tiempo_pasado += reloj.tick(FPS)

    # Generación de enemigos
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))
        tiempo_pasado = 0

    eventos = pygame.event.get()

    teclas = pygame.key.get_pressed()

    # Renderizado de los textos de vida y puntos
    texto_vida = FUENTE.render(f"Vida: {vida}", True, "white")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")

    # Gestionar movimiento del jugador
    gestionar_teclas(teclas)

    # Procesar eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    # Movimiento y colisiones de enemigos
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        # Colisión entre cubo y enemigo
        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1
            print(f"Te quedan {vida} vidas")
            enemigos.remove(enemigo)

        # Si el enemigo llega al fondo
        if enemigo.y + enemigo.alto > ALTO:
            puntos += 1
            enemigos.remove(enemigo)

    # Mostrar los textos en pantalla
    VENTANA.blit(texto_vida, (20, 20))
    VENTANA.blit(texto_puntos, (20, 50))

    pygame.display.update()

pygame.quit()
