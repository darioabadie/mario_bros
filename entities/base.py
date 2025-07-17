"""
Clase base para todas las entidades del juego.
Proporciona funcionalidad común para posición, movimiento y renderizado.
"""

import pyxel
from abc import ABC, abstractmethod
from typing import Tuple, Optional

class Entity(ABC):
    """
    Clase base abstracta para todas las entidades del juego.
    Define la interfaz común que deben implementar todas las entidades.
    """
    
    def __init__(self, x: float, y: float, width: int, height: int):
        """
        Inicializa una entidad básica.
        
        Args:
            x: Posición X inicial
            y: Posición Y inicial  
            width: Ancho de la entidad
            height: Alto de la entidad
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        # Velocidades
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        
        # Estados
        self.active = True
        self.visible = True
        
        # Para detección de colisiones
        self.collision_enabled = True
        
    @property
    def rect(self) -> Tuple[float, float, float, float]:
        """Retorna el rectángulo de colisión (x, y, width, height)"""
        return (self.x, self.y, self.width, self.height)
    
    @property
    def center_x(self) -> float:
        """Retorna la coordenada X del centro de la entidad"""
        return self.x + self.width / 2
    
    @property
    def center_y(self) -> float:
        """Retorna la coordenada Y del centro de la entidad"""
        return self.y + self.height / 2
    
    @property
    def bottom(self) -> float:
        """Retorna la coordenada Y del borde inferior"""
        return self.y + self.height
    
    @property
    def right(self) -> float:
        """Retorna la coordenada X del borde derecho"""
        return self.x + self.width
    
    def move(self, dx: float, dy: float) -> None:
        """
        Mueve la entidad por una cantidad relativa.
        
        Args:
            dx: Desplazamiento en X
            dy: Desplazamiento en Y
        """
        self.x += dx
        self.y += dy
    
    def set_position(self, x: float, y: float) -> None:
        """
        Establece la posición absoluta de la entidad.
        
        Args:
            x: Nueva posición X
            y: Nueva posición Y
        """
        self.x = x
        self.y = y
    
    def check_collision(self, other: 'Entity') -> bool:
        """
        Verifica si esta entidad colisiona con otra.
        
        Args:
            other: La otra entidad para verificar colisión
            
        Returns:
            True si hay colisión, False en caso contrario
        """
        if not (self.collision_enabled and other.collision_enabled):
            return False
            
        return (self.x < other.right and 
                self.right > other.x and
                self.y < other.bottom and 
                self.bottom > other.y)
    
    @abstractmethod
    def update(self) -> None:
        """
        Actualiza la lógica de la entidad cada frame.
        Debe ser implementado por las clases hijas.
        """
        pass
    
    @abstractmethod
    def draw(self, camera_x: float = 0, camera_y: float = 0) -> None:
        """
        Dibuja la entidad en pantalla.
        Debe ser implementado por las clases hijas.
        
        Args:
            camera_x: Offset de cámara en X
            camera_y: Offset de cámara en Y
        """
        pass
    
    def destroy(self) -> None:
        """Marca la entidad para ser eliminada"""
        self.active = False
        self.visible = False
        self.collision_enabled = False
