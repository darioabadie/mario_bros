# Sistema de Sprites Modular - Mario Bros Game

## Descripción General

El sistema de sprites ha sido completamente refactorizado de un archivo monolítico (`assets/sprites.py`) a una arquitectura modular organizada en el directorio `assets/sprites/`. Esta modularización mejora la mantenibilidad, escalabilidad y organización del código.

## Estructura del Nuevo Sistema

```
assets/sprites/
├── __init__.py          # Exporta sprite_manager
├── base.py              # Clase base SpriteBase para todos los sprites
├── manager.py           # SpriteManager principal con carga lazy
├── mario_sprites.py     # Sprites específicos de Mario
└── goomba_sprites.py    # Sprites específicos de Goomba
```

## Componentes Principales

### 1. SpriteManager (`manager.py`)

**Funcionalidades:**
- **Carga Lazy**: Los sprites se cargan solo cuando se necesitan
- **Organización por Entidad**: Cada conjunto de sprites tiene su propio módulo
- **Cache Inteligente**: Evita redibujar sprites ya cargados en el image bank
- **Gestión de Memoria**: Permite descargar conjuntos de sprites no utilizados

**Métodos Principales:**
```python
sprite_manager.draw_mario_sprite(x, y, sprite_type, facing_right)
sprite_manager.draw_goomba_sprite(x, y, sprite_type)
sprite_manager.unload_sprite_set('mario')  # Liberar memoria
sprite_manager.get_memory_usage()          # Información de uso
```

### 2. SpriteBase (`base.py`)

**Características:**
- Clase base abstracta para todos los sprites
- Funcionalidades compartidas: cache, validación, transformaciones
- Interfaz consistente para todos los sprites
- Utilidades como `flip_sprite_horizontal()` y `validate_sprite_data()`

### 3. Sprites Específicos

#### MarioSprites (`mario_sprites.py`)
```python
# Sprites disponibles:
- get_small_right()      # Mario idle derecha
- get_small_left()       # Mario idle izquierda  
- get_walk1_right()      # Mario caminando derecha
- get_walk1_left()       # Mario caminando izquierda
- get_jump_right()       # Mario saltando derecha
- get_jump_left()        # Mario saltando izquierda
```

#### GoombaSprites (`goomba_sprites.py`)
```python
# Sprites disponibles:
- get_normal()           # Goomba normal
- get_walk()             # Goomba caminando
- get_squashed()         # Goomba aplastado
- get_angry()            # Goomba enojado
```

## Ventajas del Nuevo Sistema

### 🎯 **Escalabilidad**
- Fácil agregar nuevos personajes/enemigos sin modificar archivos existentes
- Cada entidad tiene su propio módulo de sprites independiente

### 🚀 **Performance**
- Carga lazy: solo carga sprites cuando se necesitan
- Cache inteligente evita operaciones redundantes
- Posibilidad de descargar sprites no utilizados

### 🧹 **Mantenibilidad**
- Separación clara de responsabilidades
- Archivos más pequeños y enfocados
- Fácil localizar y modificar sprites específicos

### 🔧 **Flexibilidad**
- Interfaz consistente a través de SpriteBase
- Fácil extensión para nuevas funcionalidades
- Validación automática de datos de sprites

## Uso en el Código

### Antes (Sistema Monolítico):
```python
from assets.sprites import sprite_manager
sprite_manager.draw_mario_sprite(x, y, 'idle', True)
```

### Ahora (Sistema Modular):
```python
from assets.sprites import sprite_manager
sprite_manager.draw_mario_sprite(x, y, 'idle', True)  # ¡La interfaz es la misma!
```

**El cambio es transparente para el código existente**, pero ahora el sistema interno es mucho más organizado.

## Agregar Nuevos Sprites

### Para una nueva entidad (ej: Koopa):

1. **Crear módulo de sprites:**
```python
# assets/sprites/koopa_sprites.py
from .base import SpriteBase

class KoopaSprites(SpriteBase):
    def get_all_sprite_types(self):
        return ['normal', 'shell', 'walk']
    
    def get_sprite_by_name(self, sprite_name):
        # Implementar sprites específicos
        pass
```

2. **Actualizar el SpriteManager:**
```python
# En manager.py, agregar:
elif sprite_set_name == 'koopa':
    from .koopa_sprites import KoopaSprites
    self.loaded_sprite_sets['koopa'] = KoopaSprites()
    self._draw_koopa_sprites()
```

3. **Agregar métodos de dibujo:**
```python
def draw_koopa_sprite(self, x, y, sprite_type):
    # Implementar lógica de dibujo
    pass
```

## Configuración de Posiciones

Los sprites se organizan en el image bank de Pyxel por filas:
- **Fila 0 (y=0)**: Sprites de Mario
- **Fila 1 (y=16)**: Sprites de Goomba  
- **Fila 2 (y=32)**: Reservado para Koopa
- **Fila 3 (y=48)**: Reservado para items

## Próximas Mejoras

1. **Sistema de Animaciones**: Crear un `AnimationManager` para manejar secuencias
2. **Sprites de Items**: Agregar módulo para monedas, power-ups, etc.
3. **Compresión**: Implementar compresión de datos de sprites
4. **Editor Visual**: Tool para crear/editar sprites visualmente
5. **Paleta de Colores**: Sistema centralizado de manejo de colores

## Impacto en el Performance

- **Memoria**: Reducción del uso de memoria mediante carga lazy
- **Carga Inicial**: Más rápida al no cargar todos los sprites inmediatamente  
- **Runtime**: Cache elimina operaciones de dibujo redundantes
- **Escalabilidad**: El sistema escala mejor con más entidades

---

Este sistema modular proporciona una base sólida para el crecimiento futuro del juego, manteniendo el código organizado y eficiente.
