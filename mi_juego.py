import pygame
from personaje import Cubo
from enemigo import Enemigo
from bala import Bala
import random

pygame.init()
pygame.mixer.init()

# Configuración de la ventana y el juego
ANCHO = 500
ALTO = 500
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60
FUENTE = pygame.font.SysFont("Comic Sans", 40)
SONIDO_DISPARO = pygame.mixer.Sound('sonido/bala.mp3')
SONIDO_PERDER_VIDA = pygame.mixer.Sound('sonido/perder_vida.mp3')  # Nuevo sonido para perder vida

# Variables del juego
jugando = True
reloj = pygame.time.Clock()
vida = 5
puntos = 0

# Control de tiempo
tiempo_pasado = 0
tiempo_entre_enemigos = 500
ultima_bala = 0
tiempo_entre_balas = 500

# Listas de objetos
balas = []
cubo = Cubo(ANCHO / 2, ALTO - 75)
enemigos = []

def crear_bala():
    """Crea una nueva bala si ha pasado el tiempo suficiente desde la última."""
    global ultima_bala
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(cubo.rect.centerx, cubo.rect.centery))
        ultima_bala = pygame.time.get_ticks()
        SONIDO_DISPARO.play()

def gestionar_teclas(teclas):
    """Gestiona el movimiento del jugador y el disparo."""
    if teclas[pygame.K_a]:
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:
        cubo.x += cubo.velocidad
    if teclas[pygame.K_SPACE]:
        crear_bala()

# Bucle principal del juego
while jugando and vida > 0:
    tiempo_pasado += reloj.tick(FPS)

    # Generación de enemigos
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))
        tiempo_pasado = 0

    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()

    # Renderiza la información en pantalla
    texto_vida = FUENTE.render(f"Vida: {vida}", True, "white")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")

    # Manejo de entrada del usuario
    gestionar_teclas(teclas)

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    # Dibujar elementos en pantalla
    VENTANA.fill("black")
    cubo.dibujar(VENTANA)

    for enemigo in enemigos[:]:  # Iterar sobre una copia de la lista para evitar errores al eliminar elementos
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        # Verificar colisión con el jugador
        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1
            SONIDO_PERDER_VIDA.play()  # Reproducir sonido de perder vida
            print(f"Te quedan {vida} vidas")
            enemigos.remove(enemigo)

        # Si el enemigo sale de la pantalla, se suma un punto
        if enemigo.y + enemigo.alto > ALTO:
            puntos += 1
            enemigos.remove(enemigo)

        # Verificar colisión con balas
        for bala in balas[:]:  # Iterar sobre una copia de la lista
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigos.remove(enemigo)
                balas.remove(bala)
                break  # Evitar iteraciones innecesarias

    # Dibujar y mover balas
    for bala in balas[:]:
        bala.dibujar(VENTANA)
        bala.movimiento()
        if bala.y < 0:  # Eliminar la bala si sale de la pantalla
            balas.remove(bala)

    # Mostrar textos en pantalla
    VENTANA.blit(texto_vida, (20, 20))
    VENTANA.blit(texto_puntos, (20, 50))

    pygame.display.update()

# Finaliza Pygame correctamente
pygame.quit()

# Guardar la puntuación al final del juego
nombre = input("Introduce tu nombre: ")
with open("puntuaciones.txt", "a") as archivo:
    archivo.write(f"{nombre} - {puntos}\n")

print("Puntuación guardada correctamente.")
