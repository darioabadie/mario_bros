"""
Visualizador de la paleta de colores de Pyxel.
Muestra todos los colores disponibles con sus números correspondientes.
"""

import pyxel

class ColorPalette:
    """Muestra la paleta de colores de Pyxel"""
    
    def __init__(self):
        pyxel.init(160, 120, title="Pyxel Color Palette")
        pyxel.run(self.update, self.draw)
    
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE) or pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
    
    def draw(self):
        pyxel.cls(0)
        
        # Título
        pyxel.text(5, 5, "Pyxel Color Palette", 7, None)
        pyxel.text(5, 13, "Press ESC to close", 7, None)
        
        # Dibujar cada color con su número
        for i in range(16):
            x = (i % 8) * 20 + 5
            y = (i // 8) * 25 + 25
            
            # Rectángulo de color
            pyxel.rect(x, y, 15, 15, i)
            
            # Número del color
            text_color = 7 if i != 7 else 0  # Blanco sobre oscuro, negro sobre blanco
            pyxel.text(x + 2, y + 18, str(i), text_color, None)
        
        # Información adicional
        pyxel.text(5, 85, "Common Mario colors:", 7, None)
        pyxel.text(5, 93, "4=skin, 5=hair, 8=red, 10=yellow", 7, None)
        pyxel.text(5, 101, "12=blue, 7=white, 0=transparent", 7, None)

if __name__ == "__main__":
    ColorPalette()
