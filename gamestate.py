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

        self.timer = 40  # Startwert des Timers
        self.last_timer_update = pygame.time.get_ticks()  # Zeitpunkt des letzten Updates

        self.berserker_phase = False  # Berserker-Phase beginnt deaktiviert
        self.berserker_display_time = 3000  # Berserker-Nachricht 3 Sekunden anzeigen
        self.berserker_start_time = None  # Zeitpunkt der Aktivierung

      

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

        # Prüfen, ob die Runde vorbei ist
        if not self.round_over:
            # Spieler 1 besiegt
            if not self.fighter_1.alive:
                self.round_wins_fighter_2 += 1
                self.round_over = True
                self.round_start_time = current_time

            # Spieler 2 besiegt
            elif not self.fighter_2.alive:
                self.round_wins_fighter_1 += 1
                self.round_over = True
                self.round_start_time = current_time

            # Timer abgelaufen
            elif self.timer == 0:
                # Vergleiche Lebenspunkte
                if self.fighter_1.health > self.fighter_2.health:
                    self.round_wins_fighter_1 += 1
                elif self.fighter_2.health > self.fighter_1.health:
                    self.round_wins_fighter_2 += 1
                else:
                    print("Unentschieden in dieser Runde!")  # Optional: Unentschieden behandeln
                self.round_over = True
                self.round_start_time = current_time

        # Runden-Cooldown prüfen
        elif current_time - self.round_start_time > self.round_cooldown:
            self.round_over = False
            self.reset_fighters()

    def reset_fighters(self):
        """Setzt die Spieler und den Timer auf ihre Anfangswerte zurück."""
        # Spielerwerte zurücksetzen
        self.fighter_1.health = 100
        self.fighter_1.alive = True
        self.fighter_1.rect.x, self.fighter_1.rect.y = 200, 310

        self.fighter_2.health = 100
        self.fighter_2.alive = True
        self.fighter_2.rect.x, self.fighter_2.rect.y = 700, 310

        # Timer zurücksetzen
        self.timer = 40
        self.last_timer_update = pygame.time.get_ticks()

        # Berserker-Phase und Multiplikator zurücksetzen
        self.berserker_phase = False  # Berserker-Phase deaktivieren
        self.fighter_1.damage_multiplier = 1  # Standard-Schaden
        self.fighter_2.damage_multiplier = 1  # Standard-Schaden

    

    def draw_round_wins(self):
        """Zeichnet die Anzahl der gewonnenen Runden."""
        for i in range(self.round_wins_fighter_1):
            pygame.draw.circle(self.screen, self.colors["GOLD"], (190 + i * 25, 115), 10) #10, größe
        for i in range(self.round_wins_fighter_2):
            pygame.draw.circle(self.screen, self.colors["GOLD"], (760 + i * 25, 115), 10)
            
    
    
    def ermittle_winner(self, end_screen=None):
        # Überprüft, ob ein Spieler drei Runden gewonnen hat, und zeigt den Gewinner an.
        winner = None

        # Überprüfe, ob Spieler 1 gewonnen hat
        if self.round_wins_fighter_1 == 3:
            winner = self.fighter_1.name  # Dynamischer Name von Spieler 1

        # Überprüfe, ob Spieler 2 gewonnen hat
        elif self.round_wins_fighter_2 == 3:
            winner = self.fighter_2.name  # Dynamischer Name von Spieler 2

    # Gewinnertext anzeigen und Endscreen vorbereiten
        if winner:
            if end_screen:
                end_screen.set_winner(winner)  # Gewinnertext an den Endscreen übergeben
            return True  # Es gibt einen Gewinner
    
        return False  # Kein Gewinner
    
    


    def update_timer(self):
        """Aktualisiert den Timer und zeigt ihn auf dem Bildschirm an."""
        # Timer läuft nur, wenn intro_count <= 0 ist
        if self.intro_count <= 0 and self.timer > 0:
            current_time = pygame.time.get_ticks()

            # Aktualisiere den Timer jede Sekunde
            if current_time - self.last_timer_update >= 1000:  # 1000 ms = 1 Sekunde
                self.timer -= 1
                self.last_timer_update = current_time

        # Timer-Text
        timer_text = str(self.timer)
        text_width = self.fonts["score_font"].size(timer_text)[0]

        # Allgemeine Verschiebung nach rechts
        base_x_position = 450  # Ursprünglich 412, jetzt nach rechts verschoben
        x_position = base_x_position + (100 - text_width) // 2  # Zentriere basierend auf Textbreite

        # Timer anzeigen
        self.draw_text(
            timer_text, 
            self.fonts["score_font"], 
            self.colors["LILA"], 
            x_position, 40
        )


        # Timer-Ende

        # Timer-Ende
    
    def check_berserker_phase(self):
        """Aktiviert die Berserker-Phase, wenn der Timer 20 Sekunden erreicht."""
        if self.timer <= 20 and not self.berserker_phase:
            self.berserker_phase = True
            print("Berserker-Phase aktiviert!")  # Debug-Ausgabe
    
    def update_fighter_berserker_state(self):
        """Aktualisiert den Zustand der Berserker-Phase für beide Fighter."""
        if self.berserker_phase:
            self.fighter_1.damage_multiplier = 2
            self.fighter_2.damage_multiplier = 2
        else:
            self.fighter_1.damage_multiplier = 1
            self.fighter_2.damage_multiplier = 1
    
    def check_berserker_phase(self):
        """Aktiviert die Berserker-Phase, wenn der Timer 20 Sekunden erreicht."""
        if self.timer <= 20 and not self.berserker_phase:
            self.berserker_phase = True
            self.berserker_start_time = pygame.time.get_ticks()  # Zeitpunkt speichern
            print("Berserker-Phase aktiviert!")  # Debug-Ausgabe

    def display_berserker_message(self):
        """Zeigt die Berserker-Nachricht für eine bestimmte Zeit an."""
        if self.berserker_start_time:
            elapsed_time = pygame.time.get_ticks() - self.berserker_start_time
            if elapsed_time < self.berserker_display_time:
                self.draw_text(
                    "BERSERKER-PHASE!",
                    self.fonts["berserk_front"],  
                    self.colors["RED"],
                    40, 200
                )
            else:
                self.berserker_start_time = None  # Nachricht nicht mehr anzeigen

    


