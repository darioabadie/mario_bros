"""
Sistema de cámara para seguir al jugador y mostrar el mundo del juego.
"""

from config.settings import GameSettings, LevelSettings

class Camera:
    """
    Cámara del juego que sigue al jugador y maneja el viewport.
    """
    
    def __init__(self):
        """Inicializa la cámara"""
        self.x = 0
        self.y = 0
        
        # Configuración de seguimiento
        self.target_x = 0
        self.target_y = 0
        self.follow_speed = LevelSettings.CAMERA_SPEED
        self.offset_x = LevelSettings.CAMERA_OFFSET_X
        
        # Límites del mundo
        self.min_x = 0
        self.max_x = LevelSettings.LEVEL_WIDTH - GameSettings.WINDOW_WIDTH
        self.min_y = 0
        self.max_y = LevelSettings.LEVEL_HEIGHT - GameSettings.WINDOW_HEIGHT
        
        # Suavizado de movimiento
        self.smooth_follow = True
        
    def follow_target(self, target_x: float, target_y: float) -> None:
        """
        Hace que la cámara siga un objetivo (generalmente Mario).
        
        Args:
            target_x: Posición X del objetivo
            target_y: Posición Y del objetivo
        """
        # Calcular posición objetivo de la cámara
        self.target_x = target_x - self.offset_x
        self.target_y = target_y - GameSettings.WINDOW_HEIGHT // 2
        
        # Aplicar límites del mundo
        self.target_x = max(self.min_x, min(self.target_x, self.max_x))
        self.target_y = max(self.min_y, min(self.target_y, self.max_y))
        
        if self.smooth_follow:
            # Movimiento suave hacia el objetivo
            self.x += (self.target_x - self.x) * 0.1
            self.y += (self.target_y - self.y) * 0.1
        else:
            # Movimiento directo
            self.x = self.target_x
            self.y = self.target_y
    
    def set_position(self, x: float, y: float) -> None:
        """
        Establece la posición directa de la cámara.
        
        Args:
            x: Posición X
            y: Posición Y
        """
        self.x = max(self.min_x, min(x, self.max_x))
        self.y = max(self.min_y, min(y, self.max_y))
    
    def set_bounds(self, min_x: float, max_x: float, min_y: float, max_y: float) -> None:
        """
        Establece los límites de movimiento de la cámara.
        
        Args:
            min_x: Límite izquierdo
            max_x: Límite derecho
            min_y: Límite superior
            max_y: Límite inferior
        """
        self.min_x = min_x
        self.max_x = max_x - GameSettings.WINDOW_WIDTH
        self.min_y = min_y
        self.max_y = max_y - GameSettings.WINDOW_HEIGHT
    
    def world_to_screen(self, world_x: float, world_y: float) -> tuple:
        """
        Convierte coordenadas del mundo a coordenadas de pantalla.
        
        Args:
            world_x: Coordenada X en el mundo
            world_y: Coordenada Y en el mundo
            
        Returns:
            Tuple con las coordenadas de pantalla (screen_x, screen_y)
        """
        return (world_x - self.x, world_y - self.y)
    
    def screen_to_world(self, screen_x: float, screen_y: float) -> tuple:
        """
        Convierte coordenadas de pantalla a coordenadas del mundo.
        
        Args:
            screen_x: Coordenada X en pantalla
            screen_y: Coordenada Y en pantalla
            
        Returns:
            Tuple con las coordenadas del mundo (world_x, world_y)
        """
        return (screen_x + self.x, screen_y + self.y)
    
    def is_visible(self, x: float, y: float, width: float, height: float) -> bool:
        """
        Verifica si un rectángulo es visible en la pantalla.
        
        Args:
            x: Posición X del rectángulo
            y: Posición Y del rectángulo
            width: Ancho del rectángulo
            height: Alto del rectángulo
            
        Returns:
            True si el rectángulo es visible
        """
        return (x + width > self.x and 
                x < self.x + GameSettings.WINDOW_WIDTH and
                y + height > self.y and 
                y < self.y + GameSettings.WINDOW_HEIGHT)
    
    def shake(self, intensity: float, duration: int) -> None:
        """
        Aplica un efecto de sacudida a la cámara.
        
        Args:
            intensity: Intensidad de la sacudida
            duration: Duración en frames
        """
        # Esta funcionalidad se puede implementar más tarde
        # para efectos especiales como explosiones
        pass
