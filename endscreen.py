
import pygame

class EndScreen:
    def __init__(self, screen, fonts, colors, game_manager):
        """
        Initialisiert den Endbildschirm.

        Args:
            screen (pygame.Surface): Das Hauptanzeigefenster.
            fonts (dict): Eine Sammlung von Schriftarten.
            colors (dict): Eine Sammlung von Farben.
            game_manager (GameManager): Die Instanz des Spielmanagers.
        """
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.winner = None
        self.running = False
        self.game_manager = game_manager

        # Lade Button-Bilder
        self.restart_button_image = pygame.image.load("ButtonRed/pngegg.png")
        self.replay_button_image = pygame.image.load("ButtonRed/pngegg.png")

        # Skalieren der Button-Bilder (optional)
        self.restart_button_image = pygame.transform.scale(self.restart_button_image, (200, 50))
        self.replay_button_image = pygame.transform.scale(self.replay_button_image, (200, 50))

        # Definiere Positionen der Buttons
        self.restart_button_rect = self.restart_button_image.get_rect(center=(self.screen.get_width() // 2, 450))
        self.replay_button_rect = self.replay_button_image.get_rect(center=(self.screen.get_width() // 2, 550))

    def set_winner(self, winner):
        """
        Setzt den Gewinner und aktiviert den Endbildschirm.

        Args:
            winner (str): Der Name des Gewinners.
        """
        self.winner = winner
        self.running = True

    def draw_transparent_end_screen(self):
        """
        Zeichnet den transparenten Endscreen mit dem Gewinnertext und Buttons.
        Gibt die Rechtecke der Buttons für die Kollisionserkennung zurück.
        """
        # Erstelle eine transparente Oberfläche
        transparent_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 150))  # Schwarz mit 150 Alpha (halbtransparent)

        # Zeichne die transparente Fläche auf den Hauptbildschirm
        self.screen.blit(transparent_surface, (0, 0))
        
        # Gewinnertext zentrieren
        if self.winner:
            winner_text = f"{self.winner} WINS!"
            rendered_text = self.fonts["winner_font"].render(winner_text, True, self.colors["GOLD"])
        
            # Zentrierte Position berechnen
            text_width = rendered_text.get_width()
            text_height = rendered_text.get_height()
            x = (self.screen.get_width() - text_width) // 2
            y = (self.screen.get_height() - text_height) // 2

            # Text zeichnen
            self.screen.blit(rendered_text, (x, y))
        
        # Zeichne Buttons
        self.screen.blit(self.restart_button_image, self.restart_button_rect)
        self.screen.blit(self.replay_button_image, self.replay_button_rect)

        # Beschrifte Buttons
        restart_text = self.fonts["name_font"].render("Restart", True, self.colors["WHITE"])
        replay_text = self.fonts["name_font"].render("Replay", True, self.colors["WHITE"])

        # Text auf die Buttons zentrieren
        restart_text_rect = restart_text.get_rect(center=self.restart_button_rect.center)
        replay_text_rect = replay_text.get_rect(center=self.replay_button_rect.center)

        # Text zeichnen
        self.screen.blit(restart_text, restart_text_rect)
        self.screen.blit(replay_text, replay_text_rect)

        # Rückgabe der Rechtecke
        return self.restart_button_rect, self.replay_button_rect

    def run(self):
        """
        Zeigt den transparenten Endscreen an und wartet auf Benutzeraktionen.

        Returns:
            str: "restart", wenn der Neustart-Button geklickt wird.
            str: "replay", wenn die Wiederholen-Schaltfläche geklickt wird.
        """
        while self.running:
            # Zeichne den transparenten Endscreen
            restart_button_rect, replay_button_rect = self.draw_transparent_end_screen()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_button_rect.collidepoint(event.pos):
                        self.running = False  # Beende den Endscreen
                        self.game_manager.reset_game_state()  # Setze den Spielzustand zurück
                        return "restart"  # Neustartsignal
                    if replay_button_rect.collidepoint(event.pos):
                        self.running = False  # Beende den Endscreen
                        return "replay"  # Wiederholen-Signal
