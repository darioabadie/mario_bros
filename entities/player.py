"""
Clase Mario - El personaje principal del juego.
Maneja movimiento, salto, animaciones y estados del jugador.
"""

import pyxel
from entities.base import Entity
from config.settings import GameSettings
from assets.sprites import sprite_manager

class Mario(Entity):
    """
    Clase que representa al personaje Mario.
    Hereda de Entity y añade funcionalidad específica del jugador.
    """
    
    def __init__(self, x: float, y: float):
        """
        Inicializa a Mario en la posición especificada.
        
        Args:
            x: Posición X inicial
            y: Posición Y inicial
        """
        super().__init__(x, y, GameSettings.MARIO_WIDTH, GameSettings.MARIO_HEIGHT)
        
        # Estados de Mario
        self.is_on_ground = False
        self.is_running = False
        self.facing_right = True
        self.is_jumping = False
        
        # Configuración de movimiento
        self.speed = GameSettings.MARIO_SPEED
        self.jump_strength = GameSettings.JUMP_STRENGTH
        
        # Animación
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 8  # Frames entre cambios de animación
        
        # Puntuación y vidas
        self.score = 0
        self.lives = 3
        self.coins = 0
        
        # Control de input
        self.input_buffer = 0  # Para mejores controles
        
    def update(self) -> None:
        """Actualiza la lógica de Mario cada frame"""
        self._handle_input()
        self._update_animation()
        self._update_states()
    
    def _handle_input(self) -> None:
        """Maneja la entrada del jugador"""
        # Resetear velocidad horizontal
        self.velocity_x = 0
        
        # Movimiento horizontal
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_A):
            self.velocity_x = -self.speed
            self.facing_right = False
            self.is_running = True
            
            # Velocidad extra si se mantiene presionado el botón de correr
            if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_X):
                self.velocity_x *= 1.5
                
        elif pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.velocity_x = self.speed
            self.facing_right = True
            self.is_running = True
            
            # Velocidad extra si se mantiene presionado el botón de correr
            if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_X):
                self.velocity_x *= 1.5
        else:
            self.is_running = False
        
        # Salto
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP) or 
            pyxel.btnp(pyxel.KEY_W)) and self.is_on_ground:
            self.jump()
    
    def jump(self) -> None:
        """Hace que Mario salte"""
        if self.is_on_ground:
            self.velocity_y = self.jump_strength
            self.is_jumping = True
            self.is_on_ground = False
            # Aquí se podría reproducir el sonido de salto
    
    def _update_animation(self) -> None:
        """Actualiza la animación de Mario"""
        self.animation_timer += 1
        
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            
            # Solo animar si está corriendo en el suelo
            if self.is_running and self.is_on_ground:
                self.animation_frame = (self.animation_frame + 1) % 3
            else:
                self.animation_frame = 0
    
    def _update_states(self) -> None:
        """Actualiza los estados internos de Mario"""
        # Verificar si está saltando o cayendo
        if self.velocity_y < 0:
            self.is_jumping = True
        elif self.velocity_y > 0:
            self.is_jumping = False
    
    def set_on_ground(self, on_ground: bool) -> None:
        """
        Establece si Mario está en el suelo.
        
        Args:
            on_ground: True si está en el suelo
        """
        self.is_on_ground = on_ground
        if on_ground:
            self.is_jumping = False
    
    def take_damage(self) -> bool:
        """
        Mario recibe daño.
        
        Returns:
            True si Mario murió, False si solo perdió una vida
        """
        self.lives -= 1
        
        if self.lives <= 0:
            return True  # Game Over
        
        # Aquí se podría agregar lógica de invencibilidad temporal
        return False
    
    def collect_coin(self) -> None:
        """Mario recoge una moneda"""
        self.coins += 1
        self.score += 100
        
        # Vida extra cada 100 monedas
        if self.coins % 100 == 0:
            self.lives += 1
    
    def add_score(self, points: int) -> None:
        """
        Añade puntos al score de Mario.
        
        Args:
            points: Puntos a añadir
        """
        self.score += points
    
    def draw(self, camera_x: float = 0, camera_y: float = 0) -> None:
        """
        Dibuja a Mario en pantalla.
        
        Args:
            camera_x: Offset de cámara en X
            camera_y: Offset de cámara en Y
        """
        # Posición en pantalla considerando la cámara
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        
        # Solo dibujar si está visible en pantalla
        if (-self.width <= screen_x <= GameSettings.WINDOW_WIDTH and
            -self.height <= screen_y <= GameSettings.WINDOW_HEIGHT):
            
            self._draw_mario_sprite(screen_x, screen_y)
    
    def _draw_mario_sprite(self, x: float, y: float) -> None:
        """
        Dibuja el sprite de Mario basado en su estado actual.
        
        Args:
            x: Posición X en pantalla
            y: Posición Y en pantalla
        """
        # Determinar el tipo de sprite basado en el estado
        if self.is_jumping or not self.is_on_ground:
            sprite_type = 'jump'
        elif self.is_running and self.is_on_ground:
            # Alternar entre frames de caminata
            if self.animation_frame == 0:
                sprite_type = 'idle'
            else:
                sprite_type = 'walk1'
        else:
            sprite_type = 'idle'
        
        # Dibujar el sprite usando el sprite manager
        sprite_manager.draw_mario_sprite(x, y, sprite_type, self.facing_right)
    
    def reset_position(self, x: float, y: float) -> None:
        """
        Resetea la posición y estado de Mario.
        
        Args:
            x: Nueva posición X
            y: Nueva posición Y
        """
        self.set_position(x, y)
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_on_ground = False
        self.is_jumping = False
        self.is_running = False
