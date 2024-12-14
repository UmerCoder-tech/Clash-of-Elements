
import pygame
from selectscreen import CharacterSelectScreen
from endscreen import EndScreen
from map_manager import MapSelectScreen

class GameManager:
    def __init__(self, screen, fonts, colors, maps,):
        self.running = True
        self.game_state = "menu"
        self.selected_character = None
        self.selected_map = None  # Initialisiere Map
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        #self.end_screen = EndScreen(screen, fonts, colors)
        self.game_logic = None
        self.maps = maps
        self.music_playing = False


        # Pass reset_game_state to EndScreen
        #self.end_screen = EndScreen(screen, fonts, colors)
    
    def play_music(self, music_path):
    #tartet die Musik, falls sie nicht läuft.
        if not self.music_playing:
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0, 5000)
            self.music_playing = True

    def stop_music(self):
        """Stoppt die Musik."""
        if self.music_playing:
            pygame.mixer.music.stop()
            self.music_playing = False

    
    def reset_game_state(self):
        """Setzt den Zustand des Spiels zurück."""
        self.game_state = "menu"
        self.selected_character = None
        self.selected_map = None
        pygame.mixer.music.stop()  # Stoppt die aktuelle Musik

    
    def run_main_menu(self, main_menu):
        result = main_menu()
        if result is None:
            self.running = False
        elif result:
            self.game_state = "character_select"

    def run_character_select(self):
        select_screen = CharacterSelectScreen(self.screen, self.screen.get_width(), self.screen.get_height())
        self.selected_character = select_screen.run()
        if self.selected_character:
            self.game_state = "map_select"
        else:
            self.running = False

    
    def run_map_select(self):
        map_screen = MapSelectScreen(self.screen, self.fonts, self.colors, self.maps)
        selected_map = map_screen.run()  # Zeige Map-Auswahlbildschirm an und warte auf Auswahl
        if selected_map:
            self.selected_map = selected_map
            pygame.mixer.music.load(self.maps[selected_map]["music"])  # Musik der Map laden
            pygame.mixer.music.play(-1)  # Musik abspielen
            self.game_state = "running"  # Spielstatus auf "running" setzen
        else:
            self.running = False  # Spiel beenden, wenn keine Map ausgewählt wurde

    


    def run_end_screen(self):
        restart = self.end_screen.run()
        if restart == "restart" and self.game_logic:
            self.game_state = "character_select"

    





