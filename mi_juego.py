#Este es el programa principal

# Importamos la librería Pygame para crear y gestionar el juego
import pygame

# Importamos la clase Cubo desde el módulo 'personaje', que probablemente define el personaje del juego
from personaje import Cubo

# Importamos la clase Enemigo desde el módulo 'enemigo', que maneja la lógica de los enemigos
from enemigo import Enemigo

# Importamos la clase Bala desde el módulo 'bala', que define el comportamiento de las balas disparadas
from bala import Bala

# Importamos la clase Recarga desde el módulo 'recarga', que gestiona la recarga de munición
from recarga import Recarga  # Importamos la clase Recarga

# Importamos el módulo random para generar números aleatorios 
import random


pygame.init()
pygame.mixer.init()

# Configuración de la ventana y el juego
ANCHO = 1020
ALTO = 500
VENTANA = pygame.display.set_mode([ANCHO, ALTO], pygame.RESIZABLE)
FPS = 60
FUENTE = pygame.font.SysFont("Comic Sans", 40)
SONIDO_DISPARO = pygame.mixer.Sound('sonido/bala.mp3')
SONIDO_PERDER_VIDA = pygame.mixer.Sound('sonido/perder_vida.mp3')

# Variables del juego
jugando = True
reloj = pygame.time.Clock()
vida = 5
puntos = 0

# Control de tiempo
tiempo_pasado = 0
tiempo_entre_enemigos = 500
tiempo_entre_enemigos_base = 1500
ultima_bala = 0
tiempo_entre_balas = 500

# Límite máximo de enemigos
MAX_ENEMIGOS = 10

# Listas de objetos
balas = []
cubo = Cubo(ANCHO / 2, ALTO - 75)
enemigos = []
recargas = []  # Lista para almacenar los ítems de recarga

def crear_bala():
    """Crea una nueva bala si ha pasado el tiempo suficiente desde la última."""
    global ultima_bala
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Bala(cubo.rect.centerx, cubo.rect.centery))
        ultima_bala = pygame.time.get_ticks()
        SONIDO_DISPARO.play()

def gestionar_teclas(teclas):
    """Gestiona el movimiento del jugador y el disparo."""
    if teclas[pygame.K_a]:  # Movimiento hacia la izquierda
        cubo.x -= cubo.velocidad
        # Verificar que no se salga del límite izquierdo
        if cubo.x < 0:
            cubo.x = 0  # Lo fijamos en el borde izquierdo

    if teclas[pygame.K_d]:  # Movimiento hacia la derecha
        cubo.x += cubo.velocidad
        # Verificar que no se salga del límite derecho
        if cubo.x + cubo.ancho > ANCHO:
            cubo.x = ANCHO - cubo.ancho  # Lo fijamos en el borde derecho

    if teclas[pygame.K_SPACE]:  # Disparar
        crear_bala()

# Bucle principal del juego
while jugando and vida > 0:
    tiempo_pasado += reloj.tick(FPS)

    # Generación de enemigos
    if tiempo_pasado > tiempo_entre_enemigos and len(enemigos) < MAX_ENEMIGOS:
        # Crear una instancia de Enemigo temporal para obtener su ancho
        enemigo_temporal = Enemigo(0, -100)  # La posición x no importa aquí
        # Generar la posición x dentro de los límites de la pantalla
        posicion_x = random.randint(0, ANCHO - enemigo_temporal.ancho)
        # Crear el enemigo con la posición x ajustada
        enemigos.append(Enemigo(posicion_x, -100))
        tiempo_pasado = 0
        tiempo_entre_enemigos = random.randint(50, tiempo_entre_enemigos_base)
        if tiempo_entre_enemigos_base > 80:
            tiempo_entre_enemigos_base -= 20

    # Generación aleatoria del ítem de recarga
    if random.randint(1, 300) == 1:  # Probabilidad de generar un ítem
        recargas.append(Recarga(random.randint(0, ANCHO - 50), -50))

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
    
    enemigos_a_eliminar = []  # Lista auxiliar para almacenar enemigos a eliminar
    
    for enemigo in enemigos[:]:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()
        # Verificar colisión con el jugador
        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1
            SONIDO_PERDER_VIDA.play()
            print(f"Te quedan {vida} vidas")
            enemigos_a_eliminar.append(enemigo)  # Agregar el enemigo a eliminar
        # Si el enemigo sale de la pantalla, se suma un punto
        if enemigo.y + enemigo.alto > ALTO:
            puntos += 1
            enemigos_a_eliminar.append(enemigo)  # Agregar el enemigo a eliminar
        # Verificar colisión con balas
        for bala in balas[:]:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigos_a_eliminar.append(enemigo)  # Agregar el enemigo a eliminar
                balas.remove(bala)
                break
    
    # Eliminar los enemigos de la lista después de la iteración
    for enemigo in enemigos_a_eliminar:
        if enemigo in enemigos:  # Verificar que el enemigo todavía esté en la lista
            enemigos.remove(enemigo)
    
    # Dibujar y mover balas
    for bala in balas[:]:
        bala.dibujar(VENTANA)
        bala.movimiento()
        if bala.y < 0:
            balas.remove(bala)

    # Dibujar y mover ítems de recarga
    for recarga in recargas[:]:
        recarga.dibujar(VENTANA)
        recarga.movimiento()
        
        # Verificar si el jugador recoge el ítem
        if pygame.Rect.colliderect(cubo.rect, recarga.rect):
            tiempo_entre_balas = max(100, tiempo_entre_balas - 200)  # Reduce el tiempo de espera entre disparos
            recargas.remove(recarga)
            print("¡Recarga rápida activada!")
    
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
