import pygame

class GameLogic:
    def __init__(self, fighter_1, fighter_2, fonts, colors, screen, draw_text):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.fonts = fonts
        self.colors = colors
        self.screen = screen
        self.intro_count = 4
        self.last_count_update = pygame.time.get_ticks()
        self.round_over = False
        self.round_start_time = None
        self.round_cooldown = 3000  # 3 Sekunden Cooldown
        self.draw_text = draw_text  # Injected Dependency
        # Neue Attribute für Rundengewinne
        self.round_wins_fighter_1 = 0
        self.round_wins_fighter_2 = 0
      

    def update_countdown(self):
        """Aktualisiert den Countdown und zeigt ihn an."""
        current_time = pygame.time.get_ticks()
        if self.intro_count > 1:
            self.draw_text(str(self.intro_count - 1), self.fonts["count_font"], self.colors["LILA"], 440, 200)
            if (current_time - self.last_count_update) >= 1000:
                self.intro_count -= 1
                self.last_count_update = current_time
        elif self.intro_count == 1:
            self.draw_text("Fight!", self.fonts["fight_font"], self.colors["LILA"], 200, 50)
            if (current_time - self.last_count_update) >= 1000:
                self.intro_count -= 1
                self.last_count_update = current_time

    def check_round_status(self):
        """Überprüft, ob die Runde vorbei ist und aktualisiert den Status."""
        current_time = pygame.time.get_ticks()
        if not self.round_over:
            if not self.fighter_1.alive:
                self.round_wins_fighter_2 += 1
                self.round_over = True
                self.round_start_time = current_time
            elif not self.fighter_2.alive:
                self.round_wins_fighter_1 += 1
                self.round_over = True
                self.round_start_time = current_time
        else:
            if current_time - self.round_start_time > self.round_cooldown:
                self.round_over = False
                self.reset_fighters()

    def reset_fighters(self):
        """Setzt die Spieler auf ihre Anfangswerte zurück."""
        self.fighter_1.health = 10
        self.fighter_1.alive = True
        self.fighter_1.rect.x, self.fighter_1.rect.y = 200, 310

        self.fighter_2.health = 10
        self.fighter_2.alive = True
        self.fighter_2.rect.x, self.fighter_2.rect.y = 700, 310
    

    def draw_round_wins(self):
        """Zeichnet die Anzahl der gewonnenen Runden."""
        for i in range(self.round_wins_fighter_1):
            pygame.draw.circle(self.screen, self.colors["GOLD"], (160 + i * 20, 102), 10)
        for i in range(self.round_wins_fighter_2):
            pygame.draw.circle(self.screen, self.colors["GOLD"], (760 + i * 20, 102), 10)
            
    
    
    def ermittle_winner(self,):
        """Zeigt den Gewinner zentriert auf dem Bildschirm an."""
        winner = None
        if self.round_wins_fighter_1 == 3 or self.round_wins_fighter_2 == 3:
            if self.round_wins_fighter_1 == 3:
                winner = "Zuko"
                self.draw_text(f"{winner} wins!!!", self.fonts["winner_font"], self.colors["LILA"], 230, 60)
            elif self.round_wins_fighter_2 == 3:
                winner = "Susanoo"
                self.draw_text(f"{winner} wins!!!", self.fonts["winner_font"], self.colors["LILA"], 100, 60)

        

    
    
            

            

