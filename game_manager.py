import pygame
from selectscreen import CharacterSelectScreen
from endscreen import EndScreen


class GameManager:
    def __init__(self, screen, fonts, colors):
        self.running = True
        self.game_state = "menu"
        self.selected_character = None
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.end_screen = EndScreen(screen, fonts, colors)
        self.game_logic = None

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
            self.game_state = "running"
        else:
            self.running = False

    def run_end_screen(self):
        restart = self.end_screen.run()
        if restart == "restart" and self.game_logic:
            self.game_logic.reset_fighters()  # Setze die Spielstände zurück
            self.game_state = "character_select"


