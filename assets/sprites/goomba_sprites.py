"""
Sprites específicos para el enemigo Goomba.
Contiene todas las variaciones de sprites de Goomba con pixel art.
"""

from .base import SpriteBase
from typing import List

class GoombaSprites(SpriteBase):
    """Clase que contiene todos los sprites de Goomba"""
    
    def __init__(self):
        """Inicializa los sprites de Goomba"""
        super().__init__()
        self._normal_sprite = None
        self._walk_sprite = None
        self._squashed_sprite = None
        # Prepararemos los sprites la primera vez que se necesiten
    
    def get_normal(self) -> List[int]:
        """Sprite normal de Goomba (idle)"""
        if self._normal_sprite is None:
            self._normal_sprite = [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 0, 15, 0, 6, 6, 6, 6, 0, 15, 0, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 0, 13, 13, 0, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 0, 13, 13, 13, 13, 0, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 6, 13, 13, 13, 13, 6, 6, 6, 6, 0, 0,
                0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]
        return self._normal_sprite
    
    def get_walk(self) -> List[int]:
        """Sprite de Goomba caminando (variación con los pies distintos)"""
        if self._walk_sprite is None:
            self._walk_sprite = [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 0, 15, 0, 6, 6, 6, 6, 0, 15, 0, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 6, 6, 6, 6, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 6, 0, 0, 0, 0, 6, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 6, 0, 0, 0, 13, 13, 0, 0, 0, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 0, 13, 13, 13, 13, 0, 6, 6, 6, 0, 0,
                0, 0, 6, 6, 6, 6, 13, 13, 13, 13, 6, 6, 6, 6, 0, 0,
                0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0,
                0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            ]
        return self._walk_sprite
    
    def get_squashed(self) -> List[int]:
        """Sprite de Goomba aplastado"""
        if self._squashed_sprite is None:
            self._squashed_sprite = [
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0,
                0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0,
                6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
                6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
            ]
        return self._squashed_sprite
    
    def get_angry(self) -> List[int]:
        """Sprite de Goomba enojado (igual al normal por ahora)"""
        return self.get_normal()
    
    def get_all_sprite_types(self) -> List[str]:
        """Retorna todos los tipos de sprites disponibles"""
        return ['normal', 'walk', 'squashed', 'angry']
    
    def get_sprite_by_name(self, sprite_name: str) -> List[int]:
        """
        Obtiene un sprite por su nombre.
        
        Args:
            sprite_name: Nombre del sprite
            
        Returns:
            Lista de colores del sprite
        """
        sprite_methods = {
            'normal': self.get_normal,
            'walk': self.get_walk,
            'squashed': self.get_squashed,
            'angry': self.get_angry,
        }
        
        if sprite_name in sprite_methods:
            return sprite_methods[sprite_name]()
        else:
            # Retornar sprite por defecto si no se encuentra
            return self.get_normal()
    
    def get_animation_frames(self, animation_type: str) -> List[List[int]]:
        """
        Obtiene los frames de una animación específica.
        
        Args:
            animation_type: Tipo de animación ('walk', 'idle', 'death')
            
        Returns:
            Lista de sprites para la animación
        """
        if animation_type == 'walk':
            return [self.get_normal(), self.get_walk()]
        elif animation_type == 'idle':
            return [self.get_normal()]
        elif animation_type == 'death':
            return [self.get_squashed()]
        else:
            return [self.get_normal()]
