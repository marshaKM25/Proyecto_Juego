# Juego de Disparos

Este es un sencillo juego desarrollado en Python utilizando la biblioteca `pygame`.  
El objetivo es sobrevivir el mayor tiempo posible mientras se acumulan puntos y eliminar a los enemigos con disparos.

## Requisitos

Antes de ejecutar el juego, asegúrate de tener Conda instalado y sigue estos pasos para configurar el entorno correctamente.

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
El juego consta de los siguientes archivos:

mi_juego.py: Archivo principal que maneja la lógica del juego.
personaje.py: Define la clase Cubo, que representa al jugador.
enemigo.py: Define la clase Enemigo, que representa a los enemigos en el juego.
bala.py: Define la clase Bala, que representa los disparos del jugador y permite eliminar enemigos.

### MECANICA DEL JUEGO
El jugador puede disparar proyectiles para eliminar enemigos.
Los enemigos desaparecerán cuando sean alcanzados por un disparo.
Se acumulan puntos por cada enemigo eliminado.