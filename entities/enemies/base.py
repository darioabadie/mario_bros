"""
Clase base para todos los enemigos del juego.
Proporciona funcionalidad común para IA, movimiento y comportamiento.
"""

from abc import ABC, abstractmethod
from entities.base import Entity
from config.settings import GameSettings

class Enemy(Entity):
    """
    Clase base para todos los enemigos.
    Hereda de Entity y añade comportamiento específico de enemigos.
    """
    
    def __init__(self, x: float, y: float, width: int, height: int):
        """
        Inicializa un enemigo básico.
        
        Args:
            x: Posición X inicial
            y: Posición Y inicial
            width: Ancho del enemigo
            height: Alto del enemigo
        """
        super().__init__(x, y, width, height)
        
        # Estados específicos de enemigos
        self.is_alive = True
        self.is_dying = False
        self.death_timer = 0
        self.death_duration = 60  # Frames que dura la animación de muerte
        
        # Movimiento básico
        self.speed = 1.0
        self.moving_left = True
        
        # Puntos que otorga al ser derrotado
        self.score_value = 100
        
        # Para detectar bordes y paredes
        self.turn_on_edge = True
        self.turn_on_wall = True
        
    def update(self) -> None:
        """Actualiza la lógica del enemigo cada frame"""
        if not self.active:
            return
            
        if self.is_dying:
            self._update_death()
        elif self.is_alive:
            self._update_ai()
            self._update_movement()
    
    def _update_ai(self) -> None:
        """
        Actualiza la inteligencia artificial del enemigo.
        Implementación básica: caminar de lado a lado.
        """
        # Movimiento horizontal básico
        if self.moving_left:
            self.velocity_x = -self.speed
        else:
            self.velocity_x = self.speed
    
    def _update_movement(self) -> None:
        """Actualiza el movimiento del enemigo"""
        # Este método puede ser sobrescrito por enemigos específicos
        pass
    
    def _update_death(self) -> None:
        """Actualiza la animación de muerte"""
        self.death_timer += 1
        
        # Hacer que el enemigo se desvanezca gradualmente
        if self.death_timer >= self.death_duration:
            self.destroy()
    
    def take_damage(self, damage_source: str = "unknown") -> bool:
        """
        El enemigo recibe daño.
        
        Args:
            damage_source: Fuente del daño ("stomp", "fireball", etc.)
            
        Returns:
            True si el enemigo murió, False si sobrevivió
        """
        if not self.is_alive or self.is_dying:
            return False
            
        # La mayoría de enemigos básicos mueren de un golpe
        self.kill(damage_source)
        return True
    
    def kill(self, kill_method: str = "unknown") -> None:
        """
        Mata al enemigo.
        
        Args:
            kill_method: Método de muerte ("stomp", "fireball", etc.)
        """
        if not self.is_alive:
            return
            
        self.is_alive = False
        self.is_dying = True
        self.death_timer = 0
        self.velocity_x = 0
        self.velocity_y = 0
        
        # Desactivar colisiones durante la muerte
        self.collision_enabled = False
    
    def turn_around(self) -> None:
        """Hace que el enemigo se dé la vuelta"""
        self.moving_left = not self.moving_left
        
    def is_on_edge(self, ground_y: float, edge_detection_distance: float = 20) -> bool:
        """
        Verifica si el enemigo está en el borde de una plataforma.
        
        Args:
            ground_y: Altura del suelo
            edge_detection_distance: Distancia hacia adelante para detectar bordes
            
        Returns:
            True si está en un borde
        """
        # Punto de verificación hacia adelante
        check_x = self.x + edge_detection_distance if not self.moving_left else self.x - edge_detection_distance
        
        # Verificar si hay suelo hacia adelante
        # Esta es una implementación simple; en un juego más complejo
        # verificarías contra las plataformas reales
        return self.bottom >= ground_y and check_x < 0 or check_x > GameSettings.WINDOW_WIDTH
    
    def should_turn_around(self, ground_y: float, platforms=None) -> bool:
        """
        Determina si el enemigo debería darse la vuelta.
        
        Args:
            ground_y: Altura del suelo
            platforms: Lista de plataformas (opcional)
            
        Returns:
            True si debería darse la vuelta
        """
        # Girar en bordes
        if self.turn_on_edge and self.is_on_edge(ground_y):
            return True
            
        # Girar en los límites del mundo
        if self.x <= 0 or self.right >= GameSettings.WINDOW_WIDTH * 2:  # Mundo más amplio
            return True
            
        return False
    
    @abstractmethod
    def get_sprite_type(self) -> str:
        """
        Retorna el tipo de sprite actual para el enemigo.
        Debe ser implementado por cada enemigo específico.
        
        Returns:
            String que identifica el sprite a usar
        """
        pass
