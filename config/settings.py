"""
Configuraciones globales del juego Mario Bros.
Este archivo centraliza todas las configuraciones para facilitar el mantenimiento.
"""

class GameSettings:
    """Configuraciones principales del juego"""
    
    # Configuración de ventana
    WINDOW_WIDTH = 256
    WINDOW_HEIGHT = 192
    WINDOW_TITLE = "Mario Bros - Pyxel"
    FPS = 60
    
    # Colores principales (usando la paleta de Pyxel)
    COLOR_SKY = 12      # Azul claro
    COLOR_GROUND = 4    # Marrón
    COLOR_MARIO = 8     # Rojo
    COLOR_TEXT = 7      # Blanco
    COLOR_BLACK = 0     # Negro
    
    # Configuración de física
    GRAVITY = 0.5
    JUMP_STRENGTH = -8
    MARIO_SPEED = 2
    MAX_FALL_SPEED = 8
    
    # Tamaños de entidades
    MARIO_WIDTH = 16
    MARIO_HEIGHT = 16
    TILE_SIZE = 16
    
    # Controles
    KEY_LEFT = "LEFT"
    KEY_RIGHT = "RIGHT"
    KEY_JUMP = "SPACE"
    KEY_RUN = "Z"
    KEY_PAUSE = "P"
    KEY_QUIT = "Q"

class LevelSettings:
    """Configuraciones específicas de niveles"""
    
    # Dimensiones del nivel
    LEVEL_WIDTH = 512   # Ancho del nivel en píxeles
    LEVEL_HEIGHT = 192  # Alto del nivel en píxeles
    
    # Altura del suelo
    GROUND_Y = 160
    
    # Configuración de cámara
    CAMERA_SPEED = 2
    CAMERA_OFFSET_X = 64  # Offset de Mario respecto al borde izquierdo

class AudioSettings:
    """Configuraciones de audio"""
    
    # Volúmenes (0-100)
    MASTER_VOLUME = 80
    MUSIC_VOLUME = 60
    SFX_VOLUME = 80
    
    # Canales de audio
    MUSIC_CHANNEL = 0
    JUMP_CHANNEL = 1
    COIN_CHANNEL = 2
    ENEMY_CHANNEL = 3
