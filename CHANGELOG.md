# Changelog - Mario Bros Game

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
y este proyecto sigue [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Sistema de sprites modular con carga lazy y cache inteligente
- Clase base `SpriteBase` para todos los sprites del juego
- Módulos específicos para sprites de Mario y Goomba
- Documentación completa del sistema de sprites modular
- Sistema de validación de datos de sprites
- Utilidades para transformación de sprites (flip horizontal)
- Sistema automatizado de changelog con herramientas CLI
- Git hooks para verificación automática de changelog
  - Hook pre-commit que previene commits sin documentar
- Gestión de memoria mejorada para sprites

### Changed
- Refactorizado sistema de sprites de archivo monolítico a arquitectura modular
- Mejorada la organización del código en el directorio `assets/sprites/`
- Interfaz del SpriteManager mantenida para compatibilidad

### Technical Details
- Creado `assets/sprites/base.py` con clase abstracta SpriteBase
- Creado `assets/sprites/manager.py` con SpriteManager mejorado
- Creado `assets/sprites/mario_sprites.py` con sprites específicos de Mario
- Creado `assets/sprites/goomba_sprites.py` con sprites específicos de Goomba
- Eliminado `assets/sprites.py` monolítico
- Creado directorio tools/ con scripts de automatización
  - Scripts para gestión de changelog y instalación de hooks
- Actualizada tipografía con typing hints para mejor desarrollo

## [0.2.0] - 2025-07-17

### Added
- Enemigo Goomba completamente funcional con IA básica
- Sistema de colisiones entre Mario y enemigos
- Mecánica de pisar enemigos para derrotarlos
- Sprites animados para Goomba (normal, caminando, aplastado)
- Sistema de puntuación al derrotar enemigos
- Estados de muerte y aplastado para Goomba
- Detección de colisiones laterales vs. superiores

### Changed
- Mejorado el sistema de física para detectar colisiones más precisas
- Actualizada la lógica de la escena de juego para manejar enemigos

### Technical Details
- Creada clase base `Enemy` en `entities/enemies/base.py`
- Implementada clase `Goomba` en `entities/enemies/goomba.py`
- Agregados métodos de colisión específicos para enemigos
- Integrado sistema de enemigos en la escena principal del juego

## [0.1.0] - 2025-07-17

### Added
- Estructura básica del proyecto con arquitectura modular
- Sistema de configuración centralizado (`config/settings.py`)
- Entidad base para todos los objetos del juego
- Personaje Mario completamente funcional:
  - Movimiento horizontal con aceleración
  - Sistema de salto con física realista
  - Animaciones básicas (idle, caminando)
  - Sprites pixel art 16x16
- Motor de física básico:
  - Gravedad
  - Detección de colisiones AABB
  - Manejo de velocidad y posición
- Sistema de cámara que sigue a Mario
- Escena principal del juego con loop completo
- Controles de teclado (flechas, WASD, espacio para saltar)
- Sistema de sprites inicial (monolítico)
- Interfaz de usuario básica con puntuación
- Modo debug (tecla F1)

### Technical Details
- Inicializado proyecto con Pyxel 2.2.7
- Creada estructura de carpetas modular:
  - `entities/` - Personajes y objetos del juego
  - `physics/` - Motor de física
  - `scenes/` - Escenas del juego
  - `config/` - Configuración
  - `assets/` - Recursos (sprites, audio)
  - `core/` - Sistemas principales (cámara)
- Implementado patrón Entity-Component básico
- Sistema de coordenadas y viewport configurado

---

## Formato de Entradas

Cada versión debe tener:
- **Added**: Nuevas funcionalidades
- **Changed**: Cambios en funcionalidades existentes
- **Deprecated**: Funcionalidades que serán removidas
- **Removed**: Funcionalidades removidas
- **Fixed**: Corrección de bugs
- **Security**: Vulnerabilidades corregidas
- **Technical Details**: Detalles técnicos específicos

## Convenciones de Versionado

- **Major (X.0.0)**: Cambios incompatibles en la API
- **Minor (0.X.0)**: Nuevas funcionalidades compatible hacia atrás
- **Patch (0.0.X)**: Corrección de bugs compatible hacia atrás

## Próximas Versiones Planificadas

### [0.3.0] - Próximo
- Sistema de items y power-ups
- Más tipos de enemigos (Koopa Troopa)
- Sistema de niveles/mapas
- Mejoras en el sistema de audio

### [0.4.0] - Futuro
- Sistema de vidas y game over
- Menú principal
- Sistema de guardado
- Múltiples niveles

### [1.0.0] - Versión Completa
- Juego completo estilo Mario Bros clásico
- Sistema de audio completo
- Múltiples mundos y niveles
- Sistema de power-ups completo
