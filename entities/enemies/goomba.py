"""
Goomba - El enemigo más básico de Mario Bros.
Camina de lado a lado y puede ser derrotado pisándolo.
"""

import pyxel
from entities.enemies.base import Enemy
from assets.sprites import sprite_manager
from config.settings import GameSettings

class Goomba(Enemy):
    """
    Goomba - Enemigo básico que camina de lado a lado.
    Puede ser derrotado pisándolo desde arriba.
    """
    
    def __init__(self, x: float, y: float):
        """
        Inicializa un Goomba en la posición especificada.
        
        Args:
            x: Posición X inicial
            y: Posición Y inicial
        """
        super().__init__(x, y, GameSettings.MARIO_WIDTH, GameSettings.MARIO_HEIGHT)
        
        # Configuración específica del Goomba
        self.speed = 0.5  # Más lento que Mario
        self.score_value = 100
        
        # Animación
        self.animation_timer = 0
        self.animation_speed = 30  # Cambiar sprite cada 30 frames
        self.animation_frame = 0
        
        # Estados específicos del Goomba
        self.squashed = False
        self.squash_timer = 0
        self.squash_duration = 30  # Frames que permanece aplastado antes de desaparecer
        
    def update(self) -> None:
        """Actualiza la lógica del Goomba cada frame"""
        if not self.active:
            return
            
        if self.squashed:
            self._update_squashed()
        elif self.is_dying:
            self._update_death()
        elif self.is_alive:
            self._update_ai()
            self._update_animation()
    
    def _update_ai(self) -> None:
        """Actualiza la IA del Goomba"""
        # Llamar a la IA base (movimiento lateral)
        super()._update_ai()
        
        # Aquí podríamos agregar comportamiento específico del Goomba
        # Por ejemplo, detectar a Mario y acelerar hacia él
    
    def _update_animation(self) -> None:
        """Actualiza la animación del Goomba"""
        self.animation_timer += 1
        
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % 2  # Alternar entre 2 frames
    
    def _update_squashed(self) -> None:
        """Actualiza el estado de Goomba aplastado"""
        self.squash_timer += 1
        
        if self.squash_timer >= self.squash_duration:
            self.destroy()
    
    def get_sprite_type(self) -> str:
        """Retorna el tipo de sprite actual del Goomba"""
        if self.squashed:
            return 'squashed'
        elif self.is_dying:
            return 'normal'  # Usar sprite normal durante muerte
        else:
            # Alternar entre normal y walk para animación
            return 'normal' if self.animation_frame == 0 else 'walk'
    
    def take_damage(self, damage_source: str = "unknown") -> bool:
        """
        El Goomba recibe daño.
        
        Args:
            damage_source: Fuente del daño
            
        Returns:
            True si el Goomba murió
        """
        if not self.is_alive or self.squashed:
            return False
            
        if damage_source == "stomp":
            # Mario pisó al Goomba
            self.squash()
            return True
        elif damage_source == "fireball":
            # Bola de fuego (para futuras implementaciones)
            self.kill("fireball")
            return True
        else:
            # Otros tipos de daño
            self.kill(damage_source)
            return True
    
    def squash(self) -> None:
        """Aplasta al Goomba (cuando Mario lo pisa)"""
        if self.squashed or not self.is_alive:
            return
            
        self.squashed = True
        self.is_alive = False
        self.squash_timer = 0
        self.velocity_x = 0
        self.velocity_y = 0
        
        # Reducir la altura del Goomba aplastado
        self.height = 8
        self.y += 8  # Ajustar posición para que permanezca en el suelo
        
        # Desactivar colisiones
        self.collision_enabled = False
    
    def check_mario_collision(self, mario) -> str:
        """
        Verifica colisión con Mario y determina el tipo.
        
        Args:
            mario: Instancia del jugador Mario
            
        Returns:
            String indicando el tipo de colisión: "stomp", "damage", "none"
        """
        if not self.check_collision(mario):
            return "none"
            
        if not self.is_alive or self.squashed:
            return "none"
        
        # Verificar si Mario está cayendo sobre el Goomba
        if (mario.velocity_y > 0 and  # Mario está cayendo
            mario.y < self.y and      # Mario está arriba del Goomba
            abs(mario.center_x - self.center_x) < self.width * 0.7):  # Centrado horizontalmente
            return "stomp"
        else:
            # Colisión lateral - Mario recibe daño
            return "damage"
    
    def turn_around(self) -> None:
        """Hace que el Goomba se dé la vuelta"""
        super().turn_around()
        
        # Aquí podríamos agregar efectos específicos del Goomba al girarse
        # como sonidos o partículas
    
    def draw(self, camera_x: float = 0, camera_y: float = 0) -> None:
        """
        Dibuja el Goomba en pantalla.
        
        Args:
            camera_x: Offset de cámara en X
            camera_y: Offset de cámara en Y
        """
        if not self.visible:
            return
            
        # Posición en pantalla considerando la cámara
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y
        
        # Solo dibujar si está visible en pantalla
        if (-self.width <= screen_x <= GameSettings.WINDOW_WIDTH and
            -self.height <= screen_y <= GameSettings.WINDOW_HEIGHT):
            
            # Obtener el tipo de sprite actual
            sprite_type = self.get_sprite_type()
            
            # Dibujar usando el sprite manager
            sprite_manager.draw_goomba_sprite(screen_x, screen_y, sprite_type)
    
    def respawn(self, x: float, y: float) -> None:
        """
        Reaparece el Goomba en una nueva posición (para reutilización).
        
        Args:
            x: Nueva posición X
            y: Nueva posición Y
        """
        self.set_position(x, y)
        self.is_alive = True
        self.is_dying = False
        self.squashed = False
        self.active = True
        self.visible = True
        self.collision_enabled = True
        self.velocity_x = 0
        self.velocity_y = 0
        self.death_timer = 0
        self.squash_timer = 0
        self.animation_timer = 0
        self.animation_frame = 0
        self.height = GameSettings.MARIO_HEIGHT  # Restaurar altura original
