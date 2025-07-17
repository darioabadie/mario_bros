# 🍄 Goomba - Documentación Completa

## 🎮 ¡Tu primer enemigo está listo!

Acabamos de crear el **Goomba**, el enemigo más icónico de Mario Bros, completamente funcional desde sprites hasta IA.

## 🎨 **Sprite del Goomba**

### Colores utilizados:
- **Color 4 (Marrón)**: Cuerpo principal del Goomba
- **Color 5 (Gris oscuro)**: Ceño fruncido y pies
- **Color 7 (Blanco)**: Ojos
- **Color 0 (Negro)**: Pupilas y transparencias

### Estados visuales:
1. **Normal** - Goomba parado
2. **Caminando** - Pies en posición diferente  
3. **Aplastado** - Sprite comprimido cuando Mario lo pisa

## 🤖 **Sistema de IA del Goomba**

### Comportamiento básico:
```
1. Camina automáticamente de izquierda a derecha
2. Se da la vuelta al llegar a bordes o paredes
3. Detecta colisiones con Mario
4. Puede ser derrotado pisándolo desde arriba
```

### Estados del Goomba:
- **`is_alive`**: Goomba está vivo y activo
- **`is_dying`**: En proceso de muerte (con animación)
- **`squashed`**: Aplastado por Mario (sprite especial)

## ⚔️ **Sistema de Combate**

### Cómo derrotar un Goomba:
1. **Saltar encima** (`stomp`) - Mario debe caer sobre el Goomba
2. **Bola de fuego** (`fireball`) - Para futuras implementaciones
3. **Otros métodos** - Extensible para power-ups

### Detección de colisiones:
```python
def check_mario_collision(self, mario) -> str:
    # Retorna: "stomp", "damage", o "none"
    if mario está cayendo Y mario está arriba:
        return "stomp"  # Mario derrota al Goomba
    else:
        return "damage"  # Mario recibe daño
```

## 🏗️ **Arquitectura del Código**

### Jerarquía de clases:
```
Entity (base.py)
└── Enemy (enemies/base.py)
    └── Goomba (enemies/goomba.py)
```

### Archivos principales:
- **`entities/enemies/base.py`** - Clase base para todos los enemigos
- **`entities/enemies/goomba.py`** - Implementación específica del Goomba
- **`assets/sprites.py`** - Sprites del Goomba (3 estados)
- **`scenes/game_scene.py`** - Lógica de integración en el juego

## 🎯 **Funcionalidades Implementadas**

### ✅ **Movimiento y IA**
- [x] Camina automáticamente de lado a lado
- [x] Se da la vuelta en bordes y paredes
- [x] Velocidad configurable (más lento que Mario)
- [x] Detección de límites del mundo

### ✅ **Animación**
- [x] Alternar entre sprites de "normal" y "caminando"
- [x] Sprite especial cuando está aplastado
- [x] Animación de muerte/desaparición

### ✅ **Combate**
- [x] Detección precisa de colisiones con Mario
- [x] Diferenciación entre "pisar" y "chocar"
- [x] Sistema de puntuación (100 puntos por Goomba)
- [x] Mario rebota al pisar enemigos

### ✅ **Física**
- [x] Afectado por gravedad
- [x] Colisiones con suelo y plataformas
- [x] Mantiene límites del mundo

## 🎮 **Cómo Probar el Goomba**

1. **Ejecuta el juego**: `python main.py`
2. **Encuentra los Goombas**: Hay 3 colocados en el nivel
3. **Interactúa con ellos**:
   - Camina hacia ellos → Mario recibe daño
   - Salta encima → Los derrotas y ganas puntos
4. **Observa las animaciones**: Cambian de sprite al caminar

## 🔧 **Configuraciones del Goomba**

```python
# En goomba.py
self.speed = 0.5              # Velocidad de movimiento
self.score_value = 100        # Puntos que otorga
self.animation_speed = 30     # Frames entre cambios de sprite
self.squash_duration = 30     # Tiempo aplastado antes de desaparecer
```

## 🚀 **Próximas Mejoras Posibles**

### 💡 **Variaciones del Goomba**
- **Goomba Rápido**: Velocidad mayor
- **Goomba Saltarín**: Salta ocasionalmente
- **Paragoomba**: Con paracaídas, cae desde arriba

### 🧠 **IA Mejorada**
- **Detección de Mario**: Acelerar cuando Mario esté cerca
- **Evitar precipicios**: IA más inteligente para bordes
- **Patrullaje**: Caminar entre puntos específicos

### 🎨 **Mejoras Visuales**
- **Más frames de animación**: Caminata más suave
- **Efectos de partículas**: Al ser derrotado
- **Sprites direccionales**: Diferentes para izquierda/derecha

### 🔊 **Audio**
- **Sonido al ser pisado**: Efecto clásico "stomp"
- **Sonido de pasos**: Mientras camina
- **Música de alerta**: Cuando Mario está cerca

## 📊 **Estadísticas del Goomba**

| Propiedad | Valor |
|-----------|-------|
| Velocidad | 0.5 píxeles/frame |
| Puntos | 100 |
| Tamaño | 16x16 píxeles |
| Vida | 1 golpe |
| Tiempo aplastado | 30 frames (0.5 segundos) |

## 🐛 **Solución de Problemas**

**Goomba no se mueve:**
- Verifica que `is_alive = True` en la inicialización
- Confirma que la velocidad no sea 0

**Colisiones extrañas:**
- Revisa que los rectángulos de colisión sean correctos
- Verifica la lógica en `check_mario_collision()`

**Sprites no se ven:**
- Confirma que los sprites estén en el image bank correcto
- Verifica las posiciones en `draw_goomba_sprite()`

## 🌟 **¡Logros Desbloqueados!**

✅ **Primer Enemigo**: Has creado tu primer enemigo funcional
✅ **Sistema de IA**: Implementaste inteligencia artificial básica  
✅ **Detección de Colisiones**: Sistema preciso de interacciones
✅ **Animaciones**: Sprites animados y estados visuales
✅ **Arquitectura Escalable**: Base para crear más enemigos

## 🎯 **Siguiente Paso Sugerido**

¿Qué te gustaría crear ahora?

1. **🐢 Koopa Troopa** - Enemigo que se retrae en su caparazón
2. **🥇 Monedas** - Coleccionables que Mario pueda recoger
3. **🍄 Power-ups** - Super Mario o Fire Mario
4. **🏗️ Plataformas** - Obstáculos sobre los que saltar
5. **🎵 Sistema de Audio** - Sonidos y música

¡Tu Goomba está listo para la acción! 🎮
