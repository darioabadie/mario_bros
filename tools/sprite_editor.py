"""
Editor de sprites para el juego Mario Bros.
Herramienta para crear y editar sprites usando el editor integrado de Pyxel.
"""

import pyxel

class SpriteEditor:
    """
    Editor de sprites que permite crear y editar sprites usando Pyxel.
    """
    
    def __init__(self):
        """Inicializa el editor de sprites"""
        
        # Inicializar Pyxel para el editor
        pyxel.init(256, 256, title="Mario Sprite Editor")
        
        # Crear algunos sprites de ejemplo
        self._create_example_sprites()
        
        # Abrir el editor de recursos de Pyxel
        print("Abriendo el editor de sprites de Pyxel...")
        print("Instrucciones:")
        print("- Usa el mouse para dibujar en la sección de imágenes")
        print("- Los sprites de Mario están en las posiciones (0,0), (16,0), (32,0), (48,0)")
        print("- Cada sprite es de 16x16 píxeles")
        print("- Presiona Ctrl+S para guardar como archivo .pyxres")
        print("- Presiona Escape para cerrar el editor")
        
        # Ejecutar el editor
        pyxel.run(self.update, self.draw)
    
    def _create_example_sprites(self):
        """Crea sprites de ejemplo para editar"""
        
        # Mario básico en rojo (color 8)
        mario_basic = [
            # Cabeza y gorra
            [0,0,0,8,8,8,8,8,8,0,0,0,0,0,0,0],
            [0,0,8,8,8,8,8,8,8,8,8,0,0,0,0,0],
            [0,0,8,4,4,4,8,4,0,4,0,0,0,0,0,0],
            [0,8,4,8,4,4,4,4,4,4,4,4,4,0,0,0],
            # Cara
            [0,8,4,8,8,4,4,4,4,4,4,4,4,0,0,0],
            [0,8,8,4,4,4,4,4,4,4,4,4,0,0,0,0],
            [0,0,4,4,4,4,4,4,4,4,4,0,0,0,0,0],
            [0,0,0,5,5,8,5,5,5,0,0,0,0,0,0,0],
            # Cuerpo
            [0,0,5,5,5,8,5,5,8,5,5,5,0,0,0,0],
            [0,5,5,5,5,8,8,8,8,5,5,5,5,0,0,0],
            [0,4,4,5,8,10,8,8,8,8,5,4,4,0,0,0],
            [0,4,4,4,8,8,8,8,8,8,4,4,4,0,0,0],
            # Piernas
            [0,4,4,8,8,8,8,8,8,8,8,4,4,0,0,0],
            [0,0,0,8,8,8,0,0,8,8,8,0,0,0,0,0],
            [0,0,5,5,5,0,0,0,0,5,5,5,0,0,0,0],
            [0,5,5,5,5,0,0,0,0,5,5,5,5,0,0,0]
        ]
        
        # Dibujar el sprite básico en la posición (0,0)
        for y in range(16):
            for x in range(16):
                color = mario_basic[y][x]
                if color != 0:
                    pyxel.image(0).pset(x, y, color)
    
    def update(self):
        """Actualiza el editor"""
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
    
    def draw(self):
        """Dibuja el editor"""
        pyxel.cls(1)  # Fondo azul oscuro
        
        # Título
        pyxel.text(10, 10, "Mario Sprite Editor", 7, None)
        pyxel.text(10, 20, "Press SPACE to open Resource Editor", 7, None)
        pyxel.text(10, 30, "Press ESC to quit", 7, None)
        
        # Mostrar los sprites actuales
        pyxel.blt(10, 50, 0, 0, 0, 16, 16, 0)    # Mario derecha
        pyxel.blt(30, 50, 0, 16, 0, 16, 16, 0)   # Mario izquierda
        pyxel.blt(50, 50, 0, 32, 0, 16, 16, 0)   # Mario walk derecha
        pyxel.blt(70, 50, 0, 48, 0, 16, 16, 0)   # Mario walk izquierda
        
        # Etiquetas
        pyxel.text(10, 70, "Right", 7, None)
        pyxel.text(30, 70, "Left", 7, None)
        pyxel.text(50, 70, "Walk R", 7, None)
        pyxel.text(70, 70, "Walk L", 7, None)
        
        # Abrir editor de recursos con SPACE
        if pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.show()


def create_sprite_template():
    """
    Crea un archivo de plantilla para sprites de Mario.
    Útil para entender la estructura de colores.
    """
    
    template = """
# Plantilla de Sprite de Mario (16x16)
# Colores disponibles en Pyxel:
# 0 = Transparente/Negro
# 1 = Azul oscuro
# 2 = Púrpura
# 3 = Verde oscuro  
# 4 = Marrón (piel de Mario)
# 5 = Gris oscuro (bigote, cabello)
# 6 = Gris claro
# 7 = Blanco
# 8 = Rojo (gorra, overol de Mario)
# 9 = Naranja
# 10 = Amarillo (botones)
# 11 = Verde claro
# 12 = Azul claro (cielo)
# 13 = Gris medio
# 14 = Rosa
# 15 = Beige

# Ejemplo de sprite de Mario (usar números de arriba):
mario_sprite = [
    [0,0,0,8,8,8,8,8,8,0,0,0,0,0,0,0],  # Fila 0
    [0,0,8,8,8,8,8,8,8,8,8,0,0,0,0,0],  # Fila 1
    [0,0,8,4,4,4,8,4,0,4,0,0,0,0,0,0],  # Fila 2
    # ... continuar hasta fila 15
]

# Para usar este sprite en el juego:
# 1. Copia el array de colores
# 2. Pégalo en assets/sprites.py
# 3. Añádelo a la función _create_mario_sprites()
# 4. Úsalo en draw_mario_sprite()
"""
    
    with open("/Users/darioabadie/deployr/mario_game/sprite_template.txt", "w") as f:
        f.write(template)
    
    print("Plantilla de sprite creada en: sprite_template.txt")


if __name__ == "__main__":
    print("¿Qué quieres hacer?")
    print("1. Abrir editor visual de sprites")
    print("2. Crear plantilla de texto para sprites")
    
    choice = input("Selecciona (1 o 2): ")
    
    if choice == "1":
        editor = SpriteEditor()
    elif choice == "2":
        create_sprite_template()
    else:
        print("Opción no válida")
