"""
Escena principal del juego donde ocurre la acción.
Maneja la lógica del gameplay, entidades y renderizado.
"""

import pyxel
from typing import List
from entities.player import Mario
from entities.base import Entity
from entities.enemies.goomba import Goomba
from physics.engine import PhysicsEngine
from core.camera import Camera
from config.settings import GameSettings, LevelSettings

class GameScene:
    """
    Escena principal donde se desarrolla el juego.
    Coordina todas las entidades, física y renderizado.
    """
    
    def __init__(self):
        """Inicializa la escena del juego"""
        
        # Sistemas principales
        self.physics_engine = PhysicsEngine()
        self.camera = Camera()
        
        # Entidades
        self.mario = Mario(50, LevelSettings.GROUND_Y - GameSettings.MARIO_HEIGHT)
        self.entities: List[Entity] = []
        self.platforms: List[Entity] = []
        self.enemies: List[Goomba] = []  # Lista específica para enemigos
        
        # Estado del juego
        self.paused = False
        self.game_over = False
        self.level_complete = False
        
        # Configuración del nivel actual
        self.ground_y = LevelSettings.GROUND_Y
        
        # Debug info
        self.show_debug = False
        
        self._create_test_level()
    
    def _create_test_level(self) -> None:
        """Crea un nivel de prueba simple para testear el sistema"""
        # Crear algunos Goombas de prueba
        goomba1 = Goomba(200, LevelSettings.GROUND_Y - GameSettings.MARIO_HEIGHT)
        goomba2 = Goomba(350, LevelSettings.GROUND_Y - GameSettings.MARIO_HEIGHT)
        goomba3 = Goomba(500, LevelSettings.GROUND_Y - GameSettings.MARIO_HEIGHT)
        
        self.add_enemy(goomba1)
        self.add_enemy(goomba2)
        self.add_enemy(goomba3)
    
    def update(self) -> None:
        """Actualiza la lógica de la escena cada frame"""
        
        # Manejar input global
        self._handle_global_input()
        
        if self.paused or self.game_over:
            return
        
        # Actualizar Mario
        self.mario.update()
        
        # Aplicar física a Mario
        self._apply_physics_to_mario()
        
        # Actualizar enemigos
        self._update_enemies()
        
        # Verificar colisiones entre Mario y enemigos
        self._check_mario_enemy_collisions()
        
        # Actualizar otras entidades
        for entity in self.entities[:]:  # Copia para poder eliminar durante iteración
            if entity.active:
                entity.update()
            else:
                self.entities.remove(entity)
        
        # Actualizar cámara para seguir a Mario
        self.camera.follow_target(self.mario.x, self.mario.y)
        
        # Verificar condiciones de game over
        self._check_game_over()
    
    def _handle_global_input(self) -> None:
        """Maneja input que afecta toda la escena"""
        
        # Pausar/despausar
        if pyxel.btnp(pyxel.KEY_P):
            self.paused = not self.paused
        
        # Toggle debug info
        if pyxel.btnp(pyxel.KEY_F1):
            self.show_debug = not self.show_debug
        
        # Restart (para testing)
        if pyxel.btnp(pyxel.KEY_R):
            self._restart_level()
    
    def _apply_physics_to_mario(self) -> None:
        """Aplica física específicamente a Mario"""
        
        # Aplicar gravedad
        self.physics_engine.apply_gravity(self.mario)
        
        # Actualizar posición
        self.physics_engine.update_position(self.mario)
        
        # Verificar colisión con el suelo
        mario_on_ground = self.physics_engine.check_ground_collision(self.mario, self.ground_y)
        
        # Verificar colisiones con plataformas
        mario_on_platform = self.physics_engine.check_platform_collision(self.mario, self.platforms)
        
        # Actualizar estado de Mario
        self.mario.set_on_ground(mario_on_ground or mario_on_platform)
        
        # Mantener a Mario dentro de los límites del nivel
        self.physics_engine.keep_in_bounds(
            self.mario, 
            min_x=0, 
            max_x=LevelSettings.LEVEL_WIDTH,
            max_y=GameSettings.WINDOW_HEIGHT + 50  # Permitir caer un poco fuera de pantalla
        )
    
    def _check_game_over(self) -> None:
        """Verifica condiciones de game over"""
        
        # Mario cayó fuera del nivel
        if self.mario.y > GameSettings.WINDOW_HEIGHT + 50:
            if self.mario.take_damage():
                self.game_over = True
            else:
                self._restart_mario_position()
    
    def _restart_mario_position(self) -> None:
        """Reinicia la posición de Mario al inicio del nivel"""
        self.mario.reset_position(50, LevelSettings.GROUND_Y - GameSettings.MARIO_HEIGHT)
    
    def _restart_level(self) -> None:
        """Reinicia completamente el nivel"""
        self.mario.reset_position(50, LevelSettings.GROUND_Y - GameSettings.MARIO_HEIGHT)
        self.mario.lives = 3
        self.mario.score = 0
        self.mario.coins = 0
        self.camera.set_position(0, 0)
        self.game_over = False
        self.level_complete = False
        self.paused = False
        
        # Reiniciar enemigos
        for enemy in self.enemies:
            enemy.destroy()
        self.enemies.clear()
        
        # Limpiar entidades muertas
        self.entities = [e for e in self.entities if e.active]
        
        # Recrear nivel
        self._create_test_level()
    
    def draw(self) -> None:
        """Dibuja toda la escena"""
        
        # Limpiar pantalla
        pyxel.cls(GameSettings.COLOR_SKY)
        
        # Dibujar fondo y nivel
        self._draw_level()
        
        # Dibujar entidades
        for entity in self.entities:
            if entity.visible:
                entity.draw(self.camera.x, self.camera.y)
        
        # Dibujar enemigos (ya están en entities, pero por claridad)
        # Los enemigos ya se dibujan en el loop anterior
        
        # Dibujar Mario (siempre al final para que esté encima)
        self.mario.draw(self.camera.x, self.camera.y)
        
        # Dibujar UI
        self._draw_ui()
        
        # Dibujar información de debug si está activada
        if self.show_debug:
            self._draw_debug_info()
        
        # Dibujar overlays (pausa, game over)
        self._draw_overlays()
    
    def _draw_level(self) -> None:
        """Dibuja el nivel estático (suelo, pipes, etc.)"""
        
        # Dibujar el suelo
        ground_screen_y = self.ground_y - self.camera.y
        
        if ground_screen_y < GameSettings.WINDOW_HEIGHT:
            pyxel.rect(
                0, 
                max(0, ground_screen_y),
                GameSettings.WINDOW_WIDTH,
                GameSettings.WINDOW_HEIGHT - max(0, ground_screen_y),
                GameSettings.COLOR_GROUND
            )
    
    def _draw_ui(self) -> None:
        """Dibuja la interfaz de usuario (score, vidas, etc.)"""
        
        # Score
        pyxel.text(8, 8, f"SCORE: {self.mario.score:06d}", GameSettings.COLOR_TEXT, None)
        
        # Vidas
        pyxel.text(8, 16, f"LIVES: {self.mario.lives}", GameSettings.COLOR_TEXT, None)
        
        # Monedas
        pyxel.text(8, 24, f"COINS: {self.mario.coins:03d}", GameSettings.COLOR_TEXT, None)
    
    def _draw_debug_info(self) -> None:
        """Dibuja información de debug"""
        
        debug_y = GameSettings.WINDOW_HEIGHT - 40
        
        # Posición de Mario
        pyxel.text(8, debug_y, f"Mario: ({self.mario.x:.1f}, {self.mario.y:.1f})", GameSettings.COLOR_TEXT, None)
        
        # Velocidad de Mario
        pyxel.text(8, debug_y + 8, f"Vel: ({self.mario.velocity_x:.1f}, {self.mario.velocity_y:.1f})", GameSettings.COLOR_TEXT, None)
        
        # Estado de Mario
        pyxel.text(8, debug_y + 16, f"Ground: {self.mario.is_on_ground} Jump: {self.mario.is_jumping}", GameSettings.COLOR_TEXT, None)
        
        # Posición de cámara
        pyxel.text(8, debug_y + 24, f"Camera: ({self.camera.x:.1f}, {self.camera.y:.1f})", GameSettings.COLOR_TEXT, None)
    
    def _draw_overlays(self) -> None:
        """Dibuja overlays como pausa o game over"""
        
        if self.paused:
            # Fondo semi-transparente
            pyxel.rect(0, 0, GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT, GameSettings.COLOR_BLACK)
            
            # Texto de pausa
            text = "PAUSED"
            text_x = (GameSettings.WINDOW_WIDTH - len(text) * 4) // 2
            text_y = GameSettings.WINDOW_HEIGHT // 2
            pyxel.text(text_x, text_y, text, GameSettings.COLOR_TEXT, None)
            
            pyxel.text(text_x - 20, text_y + 16, "Press P to continue", GameSettings.COLOR_TEXT, None)
        
        elif self.game_over:
            # Fondo semi-transparente
            pyxel.rect(0, 0, GameSettings.WINDOW_WIDTH, GameSettings.WINDOW_HEIGHT, GameSettings.COLOR_BLACK)
            
            # Texto de game over
            text = "GAME OVER"
            text_x = (GameSettings.WINDOW_WIDTH - len(text) * 4) // 2
            text_y = GameSettings.WINDOW_HEIGHT // 2
            pyxel.text(text_x, text_y, text, GameSettings.COLOR_TEXT, None)
            
            pyxel.text(text_x - 16, text_y + 16, "Press R to restart", GameSettings.COLOR_TEXT, None)
    
    def add_entity(self, entity: Entity) -> None:
        """
        Añade una entidad a la escena.
        
        Args:
            entity: La entidad a añadir
        """
        self.entities.append(entity)
    
    def add_platform(self, platform: Entity) -> None:
        """
        Añade una plataforma a la escena.
        
        Args:
            platform: La plataforma a añadir
        """
        self.platforms.append(platform)
        self.add_entity(platform)
    
    def add_enemy(self, enemy: Goomba) -> None:
        """
        Añade un enemigo a la escena.
        
        Args:
            enemy: El enemigo a añadir
        """
        self.enemies.append(enemy)
        self.add_entity(enemy)
    
    def _update_enemies(self) -> None:
        """Actualiza todos los enemigos"""
        for enemy in self.enemies[:]:  # Copia para poder eliminar durante iteración
            if enemy.active:
                enemy.update()
                
                # Aplicar física al enemigo
                self._apply_physics_to_enemy(enemy)
                
                # Verificar si debería darse la vuelta
                if enemy.should_turn_around(self.ground_y):
                    enemy.turn_around()
            else:
                self.enemies.remove(enemy)
                if enemy in self.entities:
                    self.entities.remove(enemy)
    
    def _apply_physics_to_enemy(self, enemy: Goomba) -> None:
        """
        Aplica física a un enemigo específico.
        
        Args:
            enemy: El enemigo al que aplicar física
        """
        # Aplicar gravedad
        self.physics_engine.apply_gravity(enemy)
        
        # Actualizar posición
        self.physics_engine.update_position(enemy)
        
        # Verificar colisión con el suelo
        self.physics_engine.check_ground_collision(enemy, self.ground_y)
        
        # Verificar colisiones con plataformas
        self.physics_engine.check_platform_collision(enemy, self.platforms)
        
        # Mantener al enemigo dentro de los límites del nivel
        self.physics_engine.keep_in_bounds(
            enemy,
            min_x=-50,  # Permitir que salga un poco de pantalla
            max_x=LevelSettings.LEVEL_WIDTH + 50,
            max_y=GameSettings.WINDOW_HEIGHT + 100
        )
    
    def _check_mario_enemy_collisions(self) -> None:
        """Verifica colisiones entre Mario y todos los enemigos"""
        for enemy in self.enemies:
            if not enemy.active or not enemy.is_alive:
                continue
                
            collision_type = enemy.check_mario_collision(self.mario)
            
            if collision_type == "stomp":
                # Mario pisó al enemigo
                enemy.take_damage("stomp")
                self.mario.add_score(enemy.score_value)
                
                # Hacer que Mario rebote un poco
                self.mario.velocity_y = -4
                
            elif collision_type == "damage":
                # Mario recibe daño del enemigo
                if self.mario.take_damage():
                    self.game_over = True
                else:
                    self._restart_mario_position()
