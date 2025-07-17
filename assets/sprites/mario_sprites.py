"""
Sprites específicos para el personaje Mario.
Contiene todas las variaciones de sprites de Mario con pixel art.
"""

from .base import SpriteBase
from typing import List

class MarioSprites(SpriteBase):
    """Clase que contiene todos los sprites de Mario"""
    
    def __init__(self):
        """Inicializa los sprites de Mario"""
        super().__init__()
        self._small_mario_right = None
        self._small_mario_left = None
        self._mario_walk1_right = None
        self._mario_walk1_left = None
        # Prepararemos los sprites la primera vez que se necesiten
    
    def get_small_right(self) -> List[int]:
        """Sprite de Mario pequeño mirando a la derecha (idle)"""
        if self._small_mario_right is None:
            self._small_mario_right = [
                0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 7, 7, 6, 7, 0, 0, 0, 0, 0,
                0, 0, 0, 6, 7, 6, 7, 7, 7, 6, 7, 7, 7, 0, 0, 0,
                0, 0, 0, 6, 7, 6, 6, 7, 7, 7, 6, 7, 7, 7, 0, 0,
                0, 0, 0, 6, 6, 7, 7, 7, 7, 6, 6, 6, 6, 0, 0, 0,
                0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 8, 6, 6, 6, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 8, 6, 6, 8, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 0, 0,
                0, 0, 7, 7, 6, 8, 9, 8, 8, 9, 8, 6, 7, 7, 0, 0,
                0, 0, 7, 7, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 0, 0,
                0, 0, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 0, 0,
                0, 0, 0, 0, 8, 8, 8, 0, 0, 8, 8, 8, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0,
            ]
        return self._small_mario_right
    
    def get_small_left(self) -> List[int]:
        """Sprite de Mario pequeño mirando a la izquierda (idle)"""
        if self._small_mario_left is None:
            self._small_mario_left = [
                0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 7, 6, 7, 7, 6, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 7, 7, 7, 6, 7, 7, 7, 6, 7, 6, 0, 0, 0,
                0, 0, 0, 7, 7, 6, 7, 7, 7, 6, 6, 7, 6, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 6, 7, 7, 7, 6, 6, 0, 0, 0,
                0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 6, 6, 6, 8, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 8, 6, 6, 8, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 0, 0,
                0, 0, 7, 7, 6, 8, 9, 8, 8, 9, 8, 6, 7, 7, 0, 0,
                0, 0, 7, 7, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 0, 0,
                0, 0, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 0, 0,
                0, 0, 0, 0, 8, 8, 8, 0, 0, 8, 8, 8, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0,
            ]
        return self._small_mario_left
    
    def get_walk1_right(self) -> List[int]:
        """Sprite de Mario caminando (frame 1) mirando a la derecha"""
        if self._mario_walk1_right is None:
            self._mario_walk1_right = [
                0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 7, 7, 6, 7, 0, 0, 0, 0, 0,
                0, 0, 0, 6, 7, 6, 7, 7, 7, 6, 7, 7, 7, 0, 0, 0,
                0, 0, 0, 6, 7, 6, 6, 7, 7, 7, 6, 7, 7, 7, 0, 0,
                0, 0, 0, 6, 6, 7, 7, 7, 7, 6, 6, 6, 6, 0, 0, 0,
                0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 8, 6, 6, 6, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 8, 6, 6, 8, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 0, 0,
                0, 0, 7, 7, 6, 8, 9, 8, 8, 9, 8, 6, 7, 7, 0, 0,
                0, 0, 7, 7, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 0, 0,
                0, 0, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 0, 0,
                0, 0, 0, 0, 8, 8, 8, 0, 0, 8, 8, 8, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0,
            ]
        return self._mario_walk1_right
    
    def get_walk1_left(self) -> List[int]:
        """Sprite de Mario caminando (frame 1) mirando a la izquierda"""
        if self._mario_walk1_left is None:
            self._mario_walk1_left = [
                0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 8, 8, 8, 8, 8, 8, 8, 8, 8, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 7, 6, 7, 7, 6, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 7, 7, 7, 6, 7, 7, 7, 6, 7, 6, 0, 0, 0,
                0, 0, 0, 7, 7, 6, 7, 7, 7, 6, 6, 7, 6, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 6, 7, 7, 7, 6, 6, 0, 0, 0,
                0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 6, 6, 6, 8, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 8, 6, 6, 8, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 8, 8, 8, 8, 6, 6, 6, 6, 0, 0,
                0, 0, 7, 7, 6, 8, 9, 8, 8, 9, 8, 6, 7, 7, 0, 0,
                0, 0, 7, 7, 7, 8, 8, 8, 8, 8, 8, 7, 7, 7, 0, 0,
                0, 0, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 0, 0,
                0, 0, 0, 0, 8, 8, 8, 0, 0, 8, 8, 8, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0,
            ]
        return self._mario_walk1_left
    
    def get_jump_right(self) -> List[int]:
        """Sprite de Mario saltando mirando a la derecha"""
        # Para el salto usamos el sprite idle por ahora
        return self.get_small_right()
    
    def get_jump_left(self) -> List[int]:
        """Sprite de Mario saltando mirando a la izquierda"""
        # Para el salto usamos el sprite idle por ahora
        return self.get_small_left()
    
    def get_all_sprite_types(self) -> List[str]:
        """Retorna todos los tipos de sprites disponibles"""
        return ['small_right', 'small_left', 'walk1_right', 'walk1_left', 'jump_right', 'jump_left']
    
    def get_sprite_by_name(self, sprite_name: str) -> List[int]:
        """
        Obtiene un sprite por su nombre.
        
        Args:
            sprite_name: Nombre del sprite
            
        Returns:
            Lista de colores del sprite
        """
        sprite_methods = {
            'small_right': self.get_small_right,
            'small_left': self.get_small_left,
            'walk1_right': self.get_walk1_right,
            'walk1_left': self.get_walk1_left,
            'jump_right': self.get_jump_right,
            'jump_left': self.get_jump_left,
        }
        
        if sprite_name in sprite_methods:
            return sprite_methods[sprite_name]()
        else:
            # Retornar sprite por defecto si no se encuentra
            return self.get_small_right()
