"""
Mario Bros - Archivo principal del juego
Punto de entrada que inicializa Pyxel y maneja el loop principal del juego.
"""

import pyxel
from scenes.game_scene import GameScene
from config.settings import GameSettings
from assets.sprites import sprite_manager  # Importar para inicializar sprites

class MarioGame:
    """
    Clase principal del juego Mario Bros.
    Maneja la inicialización de Pyxel y el loop principal del juego.
    """
    
    def __init__(self):
        """Inicializa el juego"""
        
        # Configurar Pyxel
        pyxel.init(
            GameSettings.WINDOW_WIDTH,
            GameSettings.WINDOW_HEIGHT,
            title=GameSettings.WINDOW_TITLE,
            fps=GameSettings.FPS
        )
        
        # Inicializar sprites después de Pyxel
        sprite_manager.initialize_sprites()
        
        # Estado del juego
        self.current_scene = None
        self.running = True
        
        # Inicializar escena principal
        self.game_scene = GameScene()
        self.current_scene = self.game_scene
        
        # Ejecutar el juego
        pyxel.run(self.update, self.draw)
    
    def update(self):
        """Actualiza la lógica del juego cada frame"""
        
        # Manejar input global del juego
        if pyxel.btnp(pyxel.KEY_Q) or pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        
        # Actualizar la escena actual
        if self.current_scene:
            self.current_scene.update()
    
    def draw(self):
        """Dibuja el juego cada frame"""
        
        # Dibujar la escena actual
        if self.current_scene:
            self.current_scene.draw()
    
    def change_scene(self, new_scene):
        """
        Cambia a una nueva escena.
        
        Args:
            new_scene: La nueva escena a mostrar
        """
        self.current_scene = new_scene

def main():
    """Función principal que inicia el juego"""
    try:
        # Crear y ejecutar el juego
        game = MarioGame()
    except KeyboardInterrupt:
        print("\n¡Juego terminado por el usuario!")
    except Exception as e:
        print(f"Error durante la ejecución del juego: {e}")
        raise

if __name__ == "__main__":
    main()
