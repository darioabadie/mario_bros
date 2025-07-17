"""
Sistema de física para el juego Mario Bros.
Maneja gravedad, colisiones y movimiento de entidades.
"""

from typing import List, Tuple, Optional
from entities.base import Entity
from config.settings import GameSettings

class PhysicsEngine:
    """
    Motor de física del juego.
    Maneja gravedad, colisiones y restricciones de movimiento.
    """
    
    def __init__(self):
        self.gravity = GameSettings.GRAVITY
        self.max_fall_speed = GameSettings.MAX_FALL_SPEED
        
    def apply_gravity(self, entity: Entity) -> None:
        """
        Aplica gravedad a una entidad.
        
        Args:
            entity: La entidad a la que aplicar gravedad
        """
        entity.velocity_y += self.gravity
        
        # Limitar velocidad máxima de caída
        if entity.velocity_y > self.max_fall_speed:
            entity.velocity_y = self.max_fall_speed
    
    def update_position(self, entity: Entity) -> None:
        """
        Actualiza la posición de una entidad basada en su velocidad.
        
        Args:
            entity: La entidad a actualizar
        """
        entity.x += entity.velocity_x
        entity.y += entity.velocity_y
    
    def check_ground_collision(self, entity: Entity, ground_y: float) -> bool:
        """
        Verifica y resuelve colisión con el suelo.
        
        Args:
            entity: La entidad a verificar
            ground_y: Altura del suelo
            
        Returns:
            True si la entidad está en el suelo
        """
        if entity.bottom >= ground_y:
            entity.y = ground_y - entity.height
            if entity.velocity_y > 0:
                entity.velocity_y = 0
            return True
        return False
    
    def check_platform_collision(self, entity: Entity, platforms: List[Entity]) -> bool:
        """
        Verifica y resuelve colisiones con plataformas.
        
        Args:
            entity: La entidad a verificar
            platforms: Lista de plataformas
            
        Returns:
            True si la entidad está sobre una plataforma
        """
        on_platform = False
        
        for platform in platforms:
            if not platform.active:
                continue
                
            if entity.check_collision(platform):
                # Colisión desde arriba (aterrizaje)
                if (entity.velocity_y >= 0 and 
                    entity.y < platform.y):
                    entity.y = platform.y - entity.height
                    entity.velocity_y = 0
                    on_platform = True
                
                # Colisión desde abajo (golpe de cabeza)
                elif (entity.velocity_y < 0 and 
                      entity.bottom > platform.bottom):
                    entity.y = platform.bottom
                    entity.velocity_y = 0
                
                # Colisión lateral
                elif entity.velocity_x != 0:
                    if entity.velocity_x > 0:  # Moviendo a la derecha
                        entity.x = platform.x - entity.width
                    else:  # Moviendo a la izquierda
                        entity.x = platform.right
                    entity.velocity_x = 0
        
        return on_platform
    
    def keep_in_bounds(self, entity: Entity, 
                      min_x: float = 0, max_x: float = float('inf'),
                      min_y: float = -float('inf'), max_y: float = float('inf')) -> None:
        """
        Mantiene una entidad dentro de los límites especificados.
        
        Args:
            entity: La entidad a restringir
            min_x: Límite izquierdo
            max_x: Límite derecho  
            min_y: Límite superior
            max_y: Límite inferior
        """
        # Límites horizontales
        if entity.x < min_x:
            entity.x = min_x
            entity.velocity_x = 0
        elif entity.right > max_x:
            entity.x = max_x - entity.width
            entity.velocity_x = 0
        
        # Límites verticales
        if entity.y < min_y:
            entity.y = min_y
            entity.velocity_y = 0
        elif entity.bottom > max_y:
            entity.y = max_y - entity.height
            entity.velocity_y = 0

class CollisionDetector:
    """
    Detector de colisiones para diferentes tipos de entidades.
    """
    
    @staticmethod
    def rect_collision(rect1: Tuple[float, float, float, float], 
                      rect2: Tuple[float, float, float, float]) -> bool:
        """
        Detecta colisión entre dos rectángulos.
        
        Args:
            rect1: (x, y, width, height) del primer rectángulo
            rect2: (x, y, width, height) del segundo rectángulo
            
        Returns:
            True si hay colisión
        """
        x1, y1, w1, h1 = rect1
        x2, y2, w2, h2 = rect2
        
        return (x1 < x2 + w2 and 
                x1 + w1 > x2 and
                y1 < y2 + h2 and 
                y1 + h1 > y2)
    
    @staticmethod
    def point_in_rect(point: Tuple[float, float], 
                     rect: Tuple[float, float, float, float]) -> bool:
        """
        Verifica si un punto está dentro de un rectángulo.
        
        Args:
            point: (x, y) del punto
            rect: (x, y, width, height) del rectángulo
            
        Returns:
            True si el punto está dentro del rectángulo
        """
        px, py = point
        rx, ry, rw, rh = rect
        
        return (rx <= px <= rx + rw and 
                ry <= py <= ry + rh)
