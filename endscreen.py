
import pygame

class EndScreen:
    def __init__(self, screen, fonts, colors):
        
        #Initialisiert den Endbildschirm.
        
        #Args:
            #screen (pygame.Surface): Das Hauptanzeigefenster.
            #fonts (dict): Eine Sammlung von Schriftarten.
            #colors (dict): Eine Sammlung von Farben.
        
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.winner = None
        self.running = True

    def set_winner(self, winner):
        
        #Setzt den Gewinner und aktiviert den Endbildschirm.
        
        #Args:
            #winner (str): Der Name des Gewinners.
        
        self.winner = winner


    #gehört zum prototyp Transparenter endscreen zeile 30 bis 41
    def draw_transparent_end_screen(self):
        transparent_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 150))

        self.screen.blit(transparent_surface, (0, 0))
    
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

        # Neustart-Schaltfläche zeichnen (optional)
        button_rect = pygame.Rect(self.screen.get_width() // 2 - 100, 400, 200, 50)
        pygame.draw.rect(self.screen, self.colors["WHITE"], button_rect)
        button_text = self.fonts["name_font"].render("Restart", True, self.colors["BLACK"])
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.screen.blit(button_text, button_text_rect)

        return button_rect



    def run(self):
    
    #Zeigt den transparenten Endscreen an und wartet auf Benutzeraktionen.
    
    #Returns:
        #str: "restart", wenn der Neustart-Button geklickt wird.
    
        while self.running:
            # Zeichne den transparenten Endscreen
            button_rect = self.draw_transparent_end_screen()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        self.running = False
                        return "restart"  # Neustartsignal
