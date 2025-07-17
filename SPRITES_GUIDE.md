# Guía de Creación de Sprites para Mario Bros

## 🎨 ¡Hemos creado tu primer sprite de Mario!

Tu juego ahora incluye sprites pixelados de Mario que se ven como el personaje clásico. Aquí tienes todo lo que necesitas saber para personalizarlos.

## 🎮 Lo que ya funciona

✅ **Mario con sprite real** - Ya no es un rectángulo simple
✅ **Animación de caminata** - Mario cambia de sprite al moverse  
✅ **Dirección automática** - Sprites diferentes para izquierda y derecha
✅ **Sistema escalable** - Fácil agregar más sprites

## 🌈 Paleta de Colores de Pyxel

Los sprites usan la paleta fija de Pyxel (16 colores):

```
0  = Transparente/Negro
1  = Azul oscuro      
2  = Púrpura          
3  = Verde oscuro     
4  = Marrón (piel)    ← Perfecto para Mario
5  = Gris oscuro      ← Bigote y cabello
6  = Gris claro       
7  = Blanco           ← Detalles
8  = Rojo             ← Gorra y overol de Mario
9  = Naranja          
10 = Amarillo         ← Botones de Mario
11 = Verde claro      
12 = Azul claro       ← Perfecto para cielo
13 = Gris medio       
14 = Rosa             
15 = Beige            
```

## 🛠️ Herramientas Incluidas

### 1. Visualizador de Colores
```bash
python tools/color_palette.py
```
Te muestra todos los colores disponibles con sus números.

### 2. Editor de Sprites (próximamente)
```bash
python tools/sprite_editor.py
```
Editor visual para crear sprites más fácilmente.

## 📝 Cómo Crear Sprites Personalizados

### Método 1: Editar en Código

1. **Abre** `assets/sprites.py`
2. **Encuentra** las listas como `mario_small_right`
3. **Modifica** los números para cambiar colores
4. **Cada número** representa un píxel del sprite 16x16

Ejemplo de modificación:
```python
# Cambiar el color de la gorra de rojo (8) a azul (12)
mario_small_right = [
    0,0,0,0,0,12,12,12,12,12,12,0,0,0,0,0,  # Era 8, ahora 12
    # ... resto del sprite
]
```

### Método 2: Usando Template

1. **Ejecuta** el generador de plantilla:
   ```bash
   python tools/sprite_editor.py
   # Selecciona opción 2
   ```

2. **Edita** el archivo `sprite_template.txt` generado

3. **Copia** tu sprite al archivo `assets/sprites.py`

### Método 3: Pixel por Pixel

Para mayor control, puedes pensar en el sprite como una cuadrícula de 16x16:

```
Fila 0:  [0,0,0,8,8,8,8,8,8,0,0,0,0,0,0,0]
Fila 1:  [0,0,8,8,8,8,8,8,8,8,8,0,0,0,0,0]
Fila 2:  [0,0,8,4,4,4,8,4,0,4,0,0,0,0,0,0]
...
Fila 15: [0,5,5,5,5,0,0,0,0,5,5,5,5,0,0,0]
```

## 🚀 Sprites Disponibles Actualmente

1. **mario_small_right** - Mario parado mirando derecha
2. **mario_small_left** - Mario parado mirando izquierda  
3. **mario_walk1_right** - Mario caminando derecha
4. **mario_walk1_left** - Mario caminando izquierda

## 🎯 Ideas para Nuevos Sprites

### Para Mario:
- 🏃 **Mario corriendo** (posición más dinámica)
- ⬆️ **Mario saltando** (brazos arriba)
- 🍄 **Super Mario** (más alto, 16x24)
- 🔥 **Fire Mario** (colores blancos y rojos)
- 💀 **Mario muriendo** (sprite de caída)

### Para otros personajes:
- 🍄 **Goomba** (enemigo básico)
- 🐢 **Koopa** (tortuga enemiga)
- 🥇 **Monedas** (sprite animado)
- 🍄 **Power-ups** (hongos, flores)

## 📚 Estructura de Archivos de Sprites

```
assets/
├── sprites.py              # Todos los sprites en código
└── (futuros archivos .pyxres para sprites complejos)

tools/
├── color_palette.py        # Visualiza colores disponibles
├── sprite_editor.py        # Editor visual (en desarrollo)
└── sprite_template.txt     # Plantilla generada
```

## 🔧 Modificación Avanzada

### Agregar un Nuevo Sprite

1. **Crea** el array de colores en `_create_mario_sprites()`
2. **Dibújalo** en el image bank con `_draw_sprite_to_bank()`
3. **Úsalo** en `draw_mario_sprite()` agregando un nuevo tipo

Ejemplo:
```python
# En _create_mario_sprites():
mario_super = [
    # ... tu sprite de 16x24 aquí
]
self._draw_sprite_to_bank(64, 0, mario_super)

# En draw_mario_sprite():
elif sprite_type == 'super':
    sprite_x = 64
```

### Agregar Animaciones

Para animaciones más suaves, puedes crear múltiples frames:

```python
mario_walk1_right = [...]  # Frame 1
mario_walk2_right = [...]  # Frame 2  
mario_walk3_right = [...]  # Frame 3
```

## 🎨 Consejos de Diseño

1. **Contraste**: Usa colores que contrasten para que los detalles se vean
2. **Consistencia**: Mantén la misma paleta para todo el personaje
3. **Simplicidad**: En 16x16 píxeles, menos es más
4. **Referencias**: Mira sprites del Mario original para inspiración

## 🐛 Solución de Problemas

**Sprite no se ve:**
- Verifica que no uses color 0 donde no quieres transparencia
- Asegúrate de que la posición en el image bank sea correcta

**Colores extraños:**
- Revisa que uses números del 0-15 solamente
- Consulta la paleta con `python tools/color_palette.py`

**Sprite deformado:**
- Confirma que tu array tenga exactamente 256 elementos (16x16)
- Verifica que cada fila tenga 16 elementos

## 🌟 ¡Tu turno!

¡Ahora tienes todas las herramientas para crear sprites increíbles para tu Mario Bros! Experimenta con diferentes colores, poses y animaciones. ¡La creatividad es el límite!

¿Qué sprite vas a crear primero? 🎮
