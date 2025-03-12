import pygame
from personaje import Cubo  # Importa la clase Cubo desde el módulo personaje
from enemigo import Enemigo  # Importa la clase Enemigo desde el módulo enemigo
import random  # Importa la biblioteca random para generar valores aleatorios

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana del juego
ANCHO = 500
ALTO = 500
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FPS = 60  # Velocidad de fotogramas por segundo

# Fuente para mostrar texto en pantalla
FUENTE = pygame.font.SysFont("Comic Sans", 40)

# Variables de estado del juego
jugando = True  # Controla si el juego sigue en ejecución
reloj = pygame.time.Clock()  # Reloj para controlar la velocidad del juego
vida = 5  # Cantidad de vidas del jugador
puntos = 0  # Puntuación del jugador

tiempo_pasado = 0  # Control del tiempo transcurrido
# Tiempo en milisegundos entre la generación de enemigos
tiempo_entre_enemigos = 500  

# Creación del personaje principal
cubo = Cubo(ANCHO / 2, ALTO - 75)

# Lista para almacenar los enemigos generados
enemigos = []

# Función para gestionar el movimiento del jugador
def gestionar_teclas(teclas):
    if teclas[pygame.K_a]:  # Si se presiona la tecla 'A', mueve el cubo a la izquierda
        cubo.x -= cubo.velocidad
    if teclas[pygame.K_d]:  # Si se presiona la tecla 'D', mueve el cubo a la derecha
        cubo.x += cubo.velocidad

# Bucle principal del juego
while jugando and vida > 0:
    
    tiempo_pasado += reloj.tick(FPS)  # Actualiza el tiempo transcurrido en función del FPS

    # Generación de enemigos
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))  # Crea un nuevo enemigo en una posición aleatoria
        tiempo_pasado = 0  # Reinicia el contador de tiempo

    # Captura los eventos del juego (teclado, cierre de ventana, etc.)
    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()  # Obtiene las teclas presionadas

    # Renderiza los textos de vida y puntuación
    texto_vida = FUENTE.render(f"Vida: {vida}", True, "white")
    texto_puntos = FUENTE.render(f"Puntos: {puntos}", True, "white")

    # Gestiona el movimiento del jugador
    gestionar_teclas(teclas)

    # Procesa los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:  # Si se cierra la ventana, finaliza el juego
            jugando = False

    # Limpia la pantalla antes de dibujar los nuevos elementos
    VENTANA.fill("black")
    cubo.dibujar(VENTANA)  # Dibuja el cubo en la pantalla

    # Itera sobre los enemigos existentes
    for enemigo in enemigos:
        enemigo.dibujar(VENTANA)  # Dibuja el enemigo
        enemigo.movimiento()  # Mueve el enemigo

        # Verifica si hay colisión entre el cubo y un enemigo
        if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
            vida -= 1  # Reduce la vida del jugador
            print(f"Te quedan {vida} vidas")
            enemigos.remove(enemigo)  # Elimina al enemigo tras la colisión

        # Si el enemigo llega al fondo de la pantalla
        if enemigo.y + enemigo.alto > ALTO:
            puntos += 1  # Suma puntos
            enemigos.remove(enemigo)  # Elimina al enemigo de la lista

    # Muestra la información en la pantalla
    VENTANA.blit(texto_vida, (20, 20))
    VENTANA.blit(texto_puntos, (20, 50))

    # Actualiza la pantalla con los cambios
    pygame.display.update()

# Finaliza Pygame cuando el juego termina
pygame.quit()
