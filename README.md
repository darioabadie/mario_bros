# 🍄 Mario Bros Game - Pyxel

Un juego estilo Mario Bros clásico desarrollado en Python usando Pyxel, creado con fines educativos para aprender desarrollo de videojuegos.

## 🎮 Características Actuales

- ✅ **Personaje Mario**: Movimiento, salto y animaciones
- ✅ **Enemigo Goomba**: IA básica, colisiones y mecánica de pisar
- ✅ **Sistema de Física**: Gravedad, colisiones AABB
- ✅ **Cámara**: Seguimiento suave de Mario
- ✅ **Sprites**: Sistema modular con pixel art 16x16
- ✅ **Controles**: Teclado (flechas, WASD, espacio)
- ✅ **UI**: Puntuación y modo debug (F1)
- ✅ **Changelog**: Sistema automatizado de documentación

## 🎮 Controles

- **Flechas izquierda/derecha** o **A/D**: Mover Mario
- **Espacio** o **W/Flecha arriba**: Saltar
- **Z/X**: Correr (aumenta la velocidad)
- **F1**: Toggle debug info
- **Q/Escape**: Salir del juego

## 🏗️ Arquitectura del Proyecto

```
mario_game/
├── main.py                 # Punto de entrada del juego
├── requirements.txt        # Dependencias del proyecto
├── CHANGELOG.md           # Historial de cambios
├── config/                 # Configuración del juego
│   ├── __init__.py
│   └── settings.py        # Configuraciones centralizadas
├── entities/              # Personajes y objetos del juego
│   ├── __init__.py
│   ├── base.py           # Clase base Entity
│   ├── player.py         # Clase Mario
│   ├── enemies/          # Enemigos
│   │   ├── __init__.py
│   │   ├── base.py       # Clase base Enemy
│   │   └── goomba.py     # Enemigo Goomba
│   ├── collectibles/     # Items coleccionables (futuro)
│   └── platforms/        # Plataformas (futuro)
├── physics/              # Motor de física
│   ├── __init__.py
│   └── engine.py         # PhysicsEngine y CollisionDetector
├── core/                 # Sistemas principales
│   ├── __init__.py
│   └── camera.py         # Sistema de cámara
├── scenes/               # Escenas del juego
│   ├── __init__.py
│   └── game_scene.py     # Escena principal
├── assets/               # Recursos del juego
│   └── sprites/          # Sistema de sprites modular
│       ├── __init__.py
│       ├── base.py       # Clase base para sprites
│       ├── manager.py    # Gestor principal de sprites
│       ├── mario_sprites.py   # Sprites de Mario
│       └── goomba_sprites.py  # Sprites de Goomba
├── tools/                # Herramientas de desarrollo
│   ├── changelog.py      # Gestión de changelog
│   └── install-hooks.sh  # Instalación de git hooks
└── docs/                 # Documentación
    └── CHANGELOG_GUIDE.md # Guía del sistema de changelog
```

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/darioabadie/mario_bros.git
cd mario_bros

# Crear entorno virtual (recomendado)
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar el Juego
```bash
python main.py
```

## 🛠️ Desarrollo

### Sistema de Changelog

Este proyecto utiliza un sistema automatizado de changelog:

```bash
# Agregar un cambio
python tools/changelog.py add Added "Nueva funcionalidad"

# Ver cambios pendientes
python tools/changelog.py show

# Crear release
python tools/changelog.py release 0.3.0

# Instalar git hooks (verificación automática)
./tools/install-hooks.sh
```

Ver [guía completa del changelog](docs/CHANGELOG_GUIDE.md) para más detalles.

### Contribuir

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Documenta** tus cambios en el changelog (`python tools/changelog.py add Added "..."`)
4. **Commit** tus cambios (`git commit -m 'feat: agregar nueva funcionalidad'`)
5. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
6. **Abre** un Pull Request

### Estándares de Código

- **Python**: Seguir PEP 8
- **Commits**: Usar [Conventional Commits](https://www.conventionalcommits.org/)
- **Documentación**: Docstrings en español para funciones y clases
- **Changelog**: Documentar todos los cambios antes del commit

## 🎨 Sistema de Sprites

El juego utiliza un sistema modular de sprites con:

- **Carga Lazy**: Sprites se cargan solo cuando se necesitan
- **Cache Inteligente**: Evita redibujar sprites ya cargados
- **Organización por Entidad**: Cada personaje tiene su módulo de sprites
- **Pixel Art 16x16**: Estilo retro clásico

Ver [documentación completa](assets/sprites/README.md) del sistema de sprites.
├── entities/               # Todas las entidades del juego
│   ├── __init__.py
│   ├── base.py             # Clase base para entidades
│   ├── player.py           # Mario (jugador)
│   ├── collectibles/       # Monedas, power-ups, etc.
│   ├── enemies/            # Goombas, Koopas, etc.
│   └── platforms/          # Plataformas y obstáculos
├── physics/                # Motor de física
│   ├── __init__.py
│   └── engine.py           # Motor de física y colisiones
├── scenes/                 # Diferentes escenas del juego
│   ├── __init__.py
│   └── game_scene.py       # Escena principal del juego
├── levels/                 # Datos de niveles
│   ├── __init__.py
│   └── data/               # Archivos de configuración de niveles
├── audio/                  # Sistema de audio
│   └── __init__.py
└── ui/                     # Interfaz de usuario
    └── __init__.py
```

## 🛠️ Instalación y Ejecución

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clona o descarga el proyecto
2. Navega al directorio del proyecto:
   ```bash
   cd mario_game
   ```

3. Crea un entorno virtual (recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   # o
   .venv\\Scripts\\activate  # En Windows
   ```

4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

### Ejecución

```bash
python main.py
```

## 🏗️ Arquitectura del Código

### Principios de Diseño

1. **Modularidad**: Cada sistema está en su propio módulo para facilitar el mantenimiento
2. **Escalabilidad**: Fácil agregar nuevas entidades, niveles y características
3. **Separación de responsabilidades**: Cada clase tiene una responsabilidad específica
4. **Reutilización**: Clases base que pueden ser extendidas para nuevas funcionalidades

### Componentes Principales

#### Entity System
- **Entity**: Clase base abstracta para todas las entidades del juego
- **Mario**: Clase del jugador con controles y lógica específica
- Fácil extensión para enemigos, coleccionables, etc.

#### Physics Engine
- **PhysicsEngine**: Maneja gravedad, colisiones y movimiento
- **CollisionDetector**: Utilitarios para detección de colisiones
- Sistema robusto y reutilizable

#### Camera System
- **Camera**: Seguimiento suave del jugador
- Límites configurables del mundo del juego
- Conversión entre coordenadas de mundo y pantalla

#### Scene Management
- **GameScene**: Escena principal donde ocurre el gameplay
- Fácil expansión para menús, game over, etc.

## 🎯 Estado Actual

### ✅ Implementado
- [x] Sistema básico de entidades
- [x] Movimiento y salto de Mario
- [x] Sistema de física (gravedad, colisiones con suelo)
- [x] Sistema de cámara que sigue al jugador
- [x] UI básica (score, vidas, monedas)
- [x] Controles fluidos y responsivos
- [x] Sistema de pausa
- [x] Debug mode

### 🚧 Próximas Características
- [ ] Sprites y animaciones
- [ ] Plataformas y obstáculos
- [ ] Enemigos (Goombas, Koopas)
- [ ] Coleccionables (monedas, power-ups)
- [ ] Sistema de audio
- [ ] Múltiples niveles
- [ ] Menú principal
- [ ] Sistema de power-ups (Super Mario, Fire Mario)

## 🔧 Configuración

Las configuraciones principales se encuentran en `config/settings.py`:

- **GameSettings**: Configuraciones generales (ventana, colores, física)
- **LevelSettings**: Configuraciones específicas de niveles
- **AudioSettings**: Configuraciones de audio

## 🐛 Debug Mode

Presiona **F1** durante el juego para activar el modo debug que muestra:
- Posición y velocidad de Mario
- Estado del jugador (en suelo, saltando)
- Posición de la cámara
- Información útil para desarrollo

## 🤝 Contribución

Este proyecto está diseñado para ser educativo y fácil de extender. Algunas áreas donde puedes contribuir:

1. **Nuevas entidades**: Crear enemigos, power-ups, obstáculos
2. **Niveles**: Diseñar nuevos niveles y mecánicas
3. **Audio**: Implementar música y efectos de sonido
4. **Gráficos**: Crear sprites y animaciones
5. **Características**: Nuevas mecánicas de gameplay

## 🎯 Roadmap

### Version 0.3.0 (Próxima)
- [ ] Sistema de items y power-ups
- [ ] Enemigo Koopa Troopa  
- [ ] Sistema de niveles/mapas
- [ ] Mejoras en audio

### Version 0.4.0
- [ ] Sistema de vidas y game over
- [ ] Menú principal
- [ ] Sistema de guardado
- [ ] Múltiples niveles

### Version 1.0.0 (Objetivo Final)  
- [ ] Juego completo estilo Mario Bros clásico
- [ ] Sistema de audio completo
- [ ] Múltiples mundos
- [ ] Sistema de power-ups completo

## 📚 Recursos de Aprendizaje

Este proyecto está diseñado como herramienta educativa. Conceptos cubiertos:

- **Programación Orientada a Objetos**: Herencia, polimorfismo, encapsulación
- **Patrones de Diseño**: Entity-Component, Singleton, Observer  
- **Arquitectura de Software**: Separación de responsabilidades, módulos
- **Desarrollo de Juegos**: Game loop, física, colisiones, sprites
- **Herramientas de Desarrollo**: Git hooks, changelog, testing

**Recursos adicionales:**
- [Documentación de Pyxel](https://github.com/kitao/pyxel)
- [Tutoriales de desarrollo de juegos](https://realpython.com/pygame-a-primer/)
- [Patrones de diseño en juegos](https://gameprogrammingpatterns.com/)

## 🤝 Contacto

- **Autor**: Dario Abadie
- **GitHub**: [@darioabadie](https://github.com/darioabadie)
- **Proyecto**: [mario_bros](https://github.com/darioabadie/mario_bros)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

---

¡Diviértete desarrollando y jugando! 🎮✨
