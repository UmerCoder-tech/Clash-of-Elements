# Hinweis: Die grundlegende Struktur und Funktionalität des endscreen wurde von einem Youtube Video hergeleitet.
# Quellen: [https://www.youtube.com/watch?v=G8MYGDf_9ho], [https://www.youtube.com/watch?v=ndtFoWWBAoE], [https://www.youtube.com/watch?v=jyrP0dDGqgY]
#
# Übernommene Elemente:
# - Die Grundidee der Klasse: Erzeugt den endscreen mit buttons,winner_text und besitzt eine reset funktion
# - Die Text erstellug wurde Teils übernommen jedoch auf das spiel selber angepasst
# - run() wurde größtenteils selber erstellt auch teils aus bestehenden run() methoden aus anderen klassen übernommen
# - mouse collide aus dem video entnommen



import pygame

class EndScreen:
    def __init__(self, screen, fonts, colors, game_manager):
        
        #Initialisiert den Endbildschirm.

        
        #screen (pygame.Surface): Das Hauptanzeigefenster.
        #fonts (dict): Eine Sammlung von Schriftarten.
        #colors (dict): Eine Sammlung von Farben.
        #game_manager (GameManager): Die Instanz des Spielmanagers.
        
        self.screen = screen #hauptfesnter
        self.fonts = fonts
        self.colors = colors
        self.winner = None #speichert den namen des siegers
        self.running = False
        self.game_manager = game_manager

        #Button bilder werden geladen
        self.restart_button_image = pygame.image.load("ButtonRed/pngegg.png")
        self.replay_button_image = pygame.image.load("ButtonRed/pngegg.png")

        #skalieren der button images
        self.restart_button_image = pygame.transform.scale(self.restart_button_image, (200, 50))
        self.replay_button_image = pygame.transform.scale(self.replay_button_image, (200, 50))

        #Posi. der Buttons
        self.restart_button_rect = self.restart_button_image.get_rect(center=(self.screen.get_width() // 2, 480)) #2, 450
        self.replay_button_rect = self.replay_button_image.get_rect(center=(self.screen.get_width() // 2, 550))

    #setzt den Gewinner Text und aktiviert den Endscreen
    def set_winner(self, winner):
    
        self.winner = winner #gewinner Text wird gesetzt bzw.: Zuko
        self.running = True #endscreen wird aktiv und die schleife run() wird ausgeführt


    def draw_end_screen(self):
        
        # Erstelle eine transparente Oberfläche
        transparent_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        transparent_surface.fill((0, 0, 0, 150))  # Schwarz mit 150 Alpha (halbtransparent)

        #Zeichne die transparente Fläche auf den Hauptbildschirm
        self.screen.blit(transparent_surface, (0, 0))
        
        #Zeigt den gewinner text auf dem Endscreen oberhalb der buttons mittig an 
        if self.winner:
            winner_text = f"YOU WON!"
            rendered_text = self.fonts["winner_font"].render(winner_text, True, self.colors["GOLD"])
        
            # Zentrierte Position berechnen
            text_width = rendered_text.get_width()
            text_height = rendered_text.get_height()
            x = (self.screen.get_width() - text_width) // 2
            y = (self.screen.get_height() - text_height) // 2

            # Text zeichnen
            self.screen.blit(rendered_text, (x, y))
        
        #Zeichnet die Buttons
        self.screen.blit(self.restart_button_image, self.restart_button_rect)
        self.screen.blit(self.replay_button_image, self.replay_button_rect)

        #Button beschriftung
        restart_text = self.fonts["name_font"].render("Restart", True, self.colors["WHITE"])
        replay_text = self.fonts["name_font"].render("Replay", True, self.colors["WHITE"])

        #Text zentrierung auf den buttons
        restart_text_rect = restart_text.get_rect(center=self.restart_button_rect.center)
        replay_text_rect = replay_text.get_rect(center=self.replay_button_rect.center)

        #Text zeichnen
        self.screen.blit(restart_text, restart_text_rect)
        self.screen.blit(replay_text, replay_text_rect)

        #Rückgabe der Rechtecke
        return self.restart_button_rect, self.replay_button_rect



    def run(self):
        while self.running:
            # Zeichne den transparenten Endscreen
            restart_button_rect, replay_button_rect = self.draw_end_screen()

            pygame.display.update()
            #Diese for schleife beendet das spiel mit einem klick auf das rote x
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN: #prüft ob mouse button gedrückt wurde
                    if restart_button_rect.collidepoint(event.pos): #prüft ob mit der mouse innerhalb des rect. gedrückt wurde
                        self.running = False  #Beende den Endscreen
                        self.game_manager.reset_game_state()  #Setzt den Spielzustand zurück
                        return "restart"  #Runde wird durch restart neu gestratet
                    if replay_button_rect.collidepoint(event.pos):
                        self.running = False  #Beende den Endscreen
                        return "replay"  #Ganzes spiel wird neu gestartet
