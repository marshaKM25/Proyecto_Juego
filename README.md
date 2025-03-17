# Juego de Disparos

Este es un sencillo juego desarrollado en Python utilizando la biblioteca pygame.
El objetivo es sobrevivir el mayor tiempo posible mientras se acumulan puntos y se eliminan enemigos con disparos.

## Requisitos

Antes de ejecutar el juego, asegúrate de tener Conda instalado y sigue estos pasos para configurar el entorno correctamente

### 1. Crear el entorno con Conda

Ejecuta el siguiente comando en la terminal:


conda create -n juego python=3.12

### 2. Activar el entorno del juego

conda activate juego

### 3. Instalar dependencias

pip install pygame

### 4. Ejecutar el juego

python mi_juego.py



### ARCHIVOS
-mi_juego.py: Archivo principal que maneja la lógica del juego.  
-personaje.py: Define la clase Cubo, que representa al jugador.  
-enemigo.py: Define la clase Enemigo, que representa a los enemigos en el juego.  
-bala.py: Define la clase Bala, que representa los disparos del jugador y permite eliminar enemigos.  
-puntuaciones.txt: Archivo donde se guardan las puntuaciones de los jugadores.  
-Carpeta sonido/: Contiene efectos de sonido para los disparos (bala.mp3) y cuando el jugador pierde una vida (perder_vida.mp3).  
-Carpeta imagenes/: Las imágenes de la nave y enemigos  

### MECANICA DEL JUEGO
El jugador puede disparar proyectiles para eliminar enemigos.  
Los enemigos desaparecerán cuando sean alcanzados por un disparo.  
Se acumulan puntos por cada enemigo eliminado.  
Tambien abra un item que hará que recargemos más rapido y disparemos en menos tiempo.  
