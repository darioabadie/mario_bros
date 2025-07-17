"""
Clase base para todos los sprites del juego.
Define la interfaz común y funcionalidades compartidas.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

class SpriteBase(ABC):
    """
    Clase base abstracta para todos los sprites del juego.
    Define métodos que todas las clases de sprites deben implementar.
    """
    
    def __init__(self):
        """Inicializa la clase base de sprites"""
        self._sprites_cache: Dict[str, List[int]] = {}
        self._initialized = False
    
    @abstractmethod
    def get_all_sprite_types(self) -> List[str]:
        """
        Retorna todos los tipos de sprites disponibles.
        
        Returns:
            Lista de nombres de sprites disponibles
        """
        pass
    
    @abstractmethod
    def get_sprite_by_name(self, sprite_name: str) -> List[int]:
        """
        Obtiene un sprite por su nombre.
        
        Args:
            sprite_name: Nombre del sprite
            
        Returns:
            Lista de colores del sprite (16x16 = 256 elementos)
        """
        pass
    
    def get_sprite_dimensions(self) -> tuple:
        """
        Retorna las dimensiones de los sprites.
        Por defecto 16x16 pixels.
        
        Returns:
            Tupla (ancho, alto) en pixels
        """
        return (16, 16)
    
    def get_transparent_color(self) -> int:
        """
        Retorna el índice del color transparente.
        
        Returns:
            Índice del color transparente (por defecto 0)
        """
        return 0
    
    def cache_sprite(self, sprite_name: str, sprite_data: List[int]) -> None:
        """
        Cachea un sprite para evitar recrearlo múltiples veces.
        
        Args:
            sprite_name: Nombre del sprite
            sprite_data: Datos del sprite
        """
        self._sprites_cache[sprite_name] = sprite_data.copy()
    
    def get_cached_sprite(self, sprite_name: str) -> List[int]:
        """
        Obtiene un sprite del cache.
        
        Args:
            sprite_name: Nombre del sprite
            
        Returns:
            Datos del sprite o lista vacía si no está cacheado
        """
        return self._sprites_cache.get(sprite_name, [])
    
    def is_sprite_cached(self, sprite_name: str) -> bool:
        """
        Verifica si un sprite está en cache.
        
        Args:
            sprite_name: Nombre del sprite
            
        Returns:
            True si está cacheado
        """
        return sprite_name in self._sprites_cache
    
    def clear_cache(self) -> None:
        """Limpia el cache de sprites"""
        self._sprites_cache.clear()
    
    def get_cache_size(self) -> int:
        """
        Retorna el número de sprites en cache.
        
        Returns:
            Número de sprites cacheados
        """
        return len(self._sprites_cache)
    
    def validate_sprite_data(self, sprite_data: List[int]) -> bool:
        """
        Valida que los datos del sprite sean correctos.
        
        Args:
            sprite_data: Datos del sprite a validar
            
        Returns:
            True si los datos son válidos
        """
        width, height = self.get_sprite_dimensions()
        expected_length = width * height
        
        if len(sprite_data) != expected_length:
            return False
            
        # Verificar que todos los valores sean números enteros válidos (0-15 para colores Pyxel)
        for color in sprite_data:
            if not isinstance(color, int) or color < 0 or color > 15:
                return False
                
        return True
    
    def flip_sprite_horizontal(self, sprite_data: List[int]) -> List[int]:
        """
        Voltea un sprite horizontalmente.
        
        Args:
            sprite_data: Datos del sprite original
            
        Returns:
            Datos del sprite volteado
        """
        width, height = self.get_sprite_dimensions()
        flipped = []
        
        for y in range(height):
            row_start = y * width
            row = sprite_data[row_start:row_start + width]
            flipped.extend(reversed(row))
            
        return flipped
    
    def create_empty_sprite(self, fill_color: int = 0) -> List[int]:
        """
        Crea un sprite vacío.
        
        Args:
            fill_color: Color para llenar el sprite (por defecto transparente)
            
        Returns:
            Datos del sprite vacío
        """
        width, height = self.get_sprite_dimensions()
        return [fill_color] * (width * height)
    
    def get_memory_usage(self) -> Dict[str, Any]:
        """
        Retorna información sobre el uso de memoria.
        
        Returns:
            Diccionario con información de memoria
        """
        return {
            'cached_sprites': len(self._sprites_cache),
            'sprite_names': list(self._sprites_cache.keys()),
            'estimated_bytes': len(self._sprites_cache) * 256 * 4,  # 4 bytes por int aproximadamente
        }
