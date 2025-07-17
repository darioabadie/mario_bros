"""
Gestor principal de sprites modular.
Maneja la carga lazy y renderizado de sprites organizados por entidad.
"""

import pyxel
from typing import Dict, Any, Optional

class SpriteManager:
    """
    Gestor principal de sprites con carga lazy y organización modular.
    """
    
    def __init__(self):
        """Inicializa el gestor de sprites"""
        self.sprites_initialized = False
        self.loaded_sprite_sets: Dict[str, Any] = {}
        
        # Posiciones en el image bank para cada conjunto de sprites
        self.sprite_positions = {
            'mario': {'x': 0, 'y': 0},      # Mario en fila 0
            'goomba': {'x': 0, 'y': 16},    # Goomba en fila 1
            'koopa': {'x': 0, 'y': 32},     # Koopa en fila 2 (futuro)
            'items': {'x': 0, 'y': 48},     # Items en fila 3 (futuro)
        }
        
        # Cache de sprites ya dibujados en el image bank
        self.drawn_sprites: Dict[str, bool] = {}
    
    def initialize_sprites(self):
        """Inicializa el sistema de sprites después de que Pyxel esté listo"""
        if not self.sprites_initialized:
            # No cargar todos los sprites inmediatamente
            # Solo marcar como inicializado
            self.sprites_initialized = True
    
    def _load_sprite_set(self, sprite_set_name: str) -> None:
        """
        Carga un conjunto específico de sprites.
        
        Args:
            sprite_set_name: Nombre del conjunto ('mario', 'goomba', etc.)
        """
        if sprite_set_name in self.loaded_sprite_sets:
            return  # Ya cargado
            
        if sprite_set_name == 'mario':
            from .mario_sprites import MarioSprites
            self.loaded_sprite_sets['mario'] = MarioSprites()
            self._draw_mario_sprites()
            
        elif sprite_set_name == 'goomba':
            from .goomba_sprites import GoombaSprites  
            self.loaded_sprite_sets['goomba'] = GoombaSprites()
            self._draw_goomba_sprites()
            
        # Futuras expansiones aquí...
        
    def _draw_mario_sprites(self) -> None:
        """Dibuja los sprites de Mario en el image bank"""
        if 'mario_drawn' in self.drawn_sprites:
            return
            
        mario_sprites = self.loaded_sprite_sets['mario']
        pos = self.sprite_positions['mario']
        
        # Dibujar cada sprite de Mario
        self._draw_sprite_to_bank(pos['x'], pos['y'], mario_sprites.get_small_right())
        self._draw_sprite_to_bank(pos['x'] + 16, pos['y'], mario_sprites.get_small_left())
        self._draw_sprite_to_bank(pos['x'] + 32, pos['y'], mario_sprites.get_walk1_right())
        self._draw_sprite_to_bank(pos['x'] + 48, pos['y'], mario_sprites.get_walk1_left())
        
        self.drawn_sprites['mario_drawn'] = True
    
    def _draw_goomba_sprites(self) -> None:
        """Dibuja los sprites de Goomba en el image bank"""
        if 'goomba_drawn' in self.drawn_sprites:
            return
            
        goomba_sprites = self.loaded_sprite_sets['goomba']
        pos = self.sprite_positions['goomba']
        
        # Dibujar cada sprite de Goomba
        self._draw_sprite_to_bank(pos['x'], pos['y'], goomba_sprites.get_normal())
        self._draw_sprite_to_bank(pos['x'] + 16, pos['y'], goomba_sprites.get_walk())
        self._draw_sprite_to_bank(pos['x'] + 32, pos['y'], goomba_sprites.get_squashed())
        
        self.drawn_sprites['goomba_drawn'] = True
    
    def _draw_sprite_to_bank(self, x: int, y: int, sprite_data: list) -> None:
        """
        Dibuja un sprite en el image bank de Pyxel.
        
        Args:
            x: Posición X en el image bank
            y: Posición Y en el image bank
            sprite_data: Lista de colores del sprite (16x16)
        """
        for i, color in enumerate(sprite_data):
            px = x + (i % 16)
            py = y + (i // 16)
            if color != 0:  # 0 es transparente
                pyxel.images[0].pset(px, py, color)
    
    def draw_mario_sprite(self, x: float, y: float, sprite_type: str, facing_right: bool = True) -> None:
        """
        Dibuja un sprite de Mario. Carga los sprites si es necesario.
        
        Args:
            x: Posición X en pantalla
            y: Posición Y en pantalla
            sprite_type: Tipo de sprite ('idle', 'walk1', 'walk2', 'jump')
            facing_right: True si Mario mira a la derecha
        """
        # Cargar sprites de Mario si no están cargados
        if 'mario' not in self.loaded_sprite_sets:
            self._load_sprite_set('mario')
        
        # Determinar posición del sprite
        base_pos = self.sprite_positions['mario']
        sprite_x = base_pos['x']
        
        if sprite_type == 'idle':
            sprite_x += 0 if facing_right else 16
        elif sprite_type in ['walk1', 'walk2']:
            sprite_x += 32 if facing_right else 48
        elif sprite_type == 'jump':
            sprite_x += 0 if facing_right else 16  # Usar idle para salto
        
        # Dibujar el sprite
        pyxel.blt(
            int(x), int(y),
            0,  # Image bank 0
            sprite_x, base_pos['y'],
            16, 16,  # Tamaño 16x16
            0  # Color transparente
        )
    
    def draw_goomba_sprite(self, x: float, y: float, sprite_type: str = 'normal') -> None:
        """
        Dibuja un sprite de Goomba. Carga los sprites si es necesario.
        
        Args:
            x: Posición X en pantalla
            y: Posición Y en pantalla
            sprite_type: Tipo de sprite ('normal', 'walk', 'squashed')
        """
        # Cargar sprites de Goomba si no están cargados
        if 'goomba' not in self.loaded_sprite_sets:
            self._load_sprite_set('goomba')
        
        # Determinar posición del sprite
        base_pos = self.sprite_positions['goomba']
        sprite_x = base_pos['x']
        
        if sprite_type == 'normal':
            sprite_x += 0
        elif sprite_type == 'walk':
            sprite_x += 16
        elif sprite_type == 'squashed':
            sprite_x += 32
        
        # Dibujar el sprite
        pyxel.blt(
            int(x), int(y),
            0,  # Image bank 0
            sprite_x, base_pos['y'],
            16, 16,  # Tamaño 16x16
            0  # Color transparente
        )
    
    def unload_sprite_set(self, sprite_set_name: str) -> None:
        """
        Descarga un conjunto de sprites para liberar memoria.
        
        Args:
            sprite_set_name: Nombre del conjunto a descargar
        """
        if sprite_set_name in self.loaded_sprite_sets:
            del self.loaded_sprite_sets[sprite_set_name]
            
        # Remover del cache de sprites dibujados
        cache_key = f"{sprite_set_name}_drawn"
        if cache_key in self.drawn_sprites:
            del self.drawn_sprites[cache_key]
    
    def get_loaded_sprite_sets(self) -> list:
        """Retorna la lista de conjuntos de sprites cargados"""
        return list(self.loaded_sprite_sets.keys())
    
    def get_memory_usage(self) -> dict:
        """Retorna información sobre el uso de memoria de sprites"""
        return {
            'loaded_sets': len(self.loaded_sprite_sets),
            'drawn_sprites': len(self.drawn_sprites),
            'sprite_sets': list(self.loaded_sprite_sets.keys())
        }

# Instancia global del gestor
sprite_manager = SpriteManager()
