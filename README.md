# Mario Bros - Pyxel Game

Un juego de Mario Bros desarrollado en Python usando el motor de juegos Pyxel. Este proyecto está diseñado para ser escalable, fácil de entender y mantener.

## 🚀 Características

- **Movimiento fluido** de Mario con física realista
- **Sistema de cámara** que sigue al jugador
- **Arquitectura modular** para fácil expansión
- **Sistema de física** robusto para colisiones y gravedad
- **Debug mode** para desarrollo y testing

## 🎮 Controles

- **Flechas izquierda/derecha** o **A/D**: Mover Mario
- **Espacio** o **W/Flecha arriba**: Saltar
- **Z/X**: Correr (aumenta la velocidad)
- **P**: Pausar/Despausar
- **R**: Reiniciar nivel (para testing)
- **F1**: Toggle debug info
- **Q/Escape**: Salir del juego

## 📁 Estructura del Proyecto

```
mario_game/
├── main.py                 # Punto de entrada del juego
├── requirements.txt        # Dependencias del proyecto
├── assets/                 # Recursos del juego (sprites, música, sonidos)
│   ├── music/
│   ├── sounds/
│   └── sprites/
├── config/                 # Configuraciones del juego
│   ├── __init__.py
│   └── settings.py         # Configuraciones principales
├── core/                   # Sistemas centrales del juego
│   ├── __init__.py
│   └── camera.py           # Sistema de cámara
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

## 📚 Recursos de Aprendizaje

- [Documentación de Pyxel](https://github.com/kitao/pyxel)
- [Tutoriales de desarrollo de juegos](https://realpython.com/pygame-a-primer/)
- [Patrones de diseño en juegos](https://gameprogrammingpatterns.com/)

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
