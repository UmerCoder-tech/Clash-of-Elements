# Hinweis: Die grundlegende Struktur und Funktionalität der Fighter-Klasse wurde von einem YouTube-Tutorial inspiriert.
# Quelle: [Link zum Tutorial]
#
# Übernommene Elemente:
# - Die Grundidee der Klasse: Verwaltung von Bewegung, Angriffen und Animationen.
# - Basislogik für Animationen und die `update_action`-Methode.
# - Grundlegende Steuerung und Angriffslogik.
#
# Änderungen und Eigenleistung:
# 1. Neue Mechaniken:
#    - Einführung von Verteidigung ("defend") und Spezialangriffen ("atk3") mit Mana-Mechanik.
#    - Berserker-Phase mit Schadensmultiplikator.
#
# 2. Optimierung der Steuerung:
#    - Nutzung eines Dictionaries zur zentralen Definition von Steuerelementen.
#    - Modularisierung der Bewegungslogik (`move_left`, `move_right`), wodurch der Code kürzer und wartbarer wurde.
#
# 3. Verbesserte Lesbarkeit:
#    - Verwendung beschreibender Strings anstelle numerischer Zustände für Animationen.
#    - Umfangreiche Kommentare, um die Logik verständlich zu machen.
#
# 4. Erweiterte Animationen:
#    - Neue Zustände wie "death" und "take_hit" wurden detaillierter behandelt.
#    - Klarere Trennung zwischen finalen und zurücksetzbaren Animationen.



import pygame

class Champion:
    def __init__(self, player, x, y, animations, sound, name, map_data):
        self.player = player
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.health = 10
        self.alive = True
        self.hit = False
        self.flip = False
        self.SPEED = 10  
        self.defending = False  
        self.defend_cooldown = 0  
        self.mana = 0
        self.max_mana = 100  
        self.can_special = False  # Gibt an, ob die Spezialattacke verfügbar ist
        self.attack_sound = sound 
        self.damage_multiplier = 1  # Standardmäßiger Schaden
        self.name = name


        # Animationen
        self.animations = animations
        self.action = "idle"
        self.frame_index = 0
        self.image = self.animations[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()

        # Offset
        self.offset_x = (self.rect.width - self.image.get_width()) // 2 + map_data["offset_x"]       #zentrieren unsere sprites und teilen durch 2, damit diese gleichmäßig verteilt werden auf beiden Seiten
        self.offset_y = (self.rect.height - self.image.get_height()) // 2 + map_data["offset_y"]     # 110 fester wert, der nicht übertroffen werden kann (Boden)

   
  
    
   
    
    # Spezifische Trennung zwischen finalen Animationen (z. B. "death") und Animationen, die zurückgesetzt werden können, sowie 
    
    def update(self):
        if self.health <= 0:  #death muss separat geschehen, da die animation final ist 
            self.health = 0
            self.alive = False
            self.update_action("death")
        else:

        # Mapping für andere nicht-finale Aktionen mit ihren Zuständen
            action_mapping = {
                "take_hit": self.hit,
                "atk1": self.attacking and self.attack_type == 1,
                "atk2": self.attacking and self.attack_type == 2,
                "atk3": self.attacking and self.attack_type == 3,
                "defend": self.defending,
                "jump": self.jump,
                "run": self.running,
                "idle": True  # Default-Aktion
            }

            for action, condition in action_mapping.items():    #iteration der key-value paare, die je nach Boolean-Wert geupdatet werden soll 
                if condition:
                    self.update_action(action)
                    break  # Aktion gefunden, weitere Prüfung abbrechen

        # Animation aktualisieren
        animation_cooldown = 50
        self.image = self.animations[self.action][self.frame_index]    #aktuelle frame der Animation auf Basis der Action
        if pygame.time.get_ticks() - self.update_time > animation_cooldown: #wenn 50ms vergangen sind, 
            self.frame_index += 1                                           #soll der nächste Frame abgespeilt werden
            self.update_time = pygame.time.get_ticks()

        # Animation zurücksetzen, wenn sie abgeschlossen ist
        if self.frame_index >= len(self.animations[self.action]):
            if not self.alive:
                self.frame_index = len(self.animations[self.action]) - 1   #finales frame, wenn tot
            else:
                self.frame_index = 0                                        #anderseits wird bei frame 0 wieder begonnen
                if self.action.startswith("atk"):
                    self.attacking = False
                    self.attack_cooldown = 20           #zusätzlich ein cooldown für attack
                if self.action == "take_hit":
                    self.hit = False
                if self.action == "defend":
                    self.defending = False  # Beende den Verteidigungszustand

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

        
    
   
    def move(self, screen_width, screen_height, target):
        GRAVITY = 2
        dx, dy = 0, 0
        self.running = False  

        # Angriffscooldown reduzieren
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Verteidigungs-Cooldown
        if self.defend_cooldown > 0:
            self.defend_cooldown -= 1


        # Zentralisierung der Steuerung mithilfe eines Dictionaries 
        controls = {
            1: {"left": pygame.K_a, "right": pygame.K_d, "jump": pygame.K_w, "attack1": pygame.K_r, "attack2": pygame.K_t, "attack3": pygame.K_z, "defend": pygame.K_f},
            2: {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "jump": pygame.K_UP, "attack1": pygame.K_u, "attack2": pygame.K_i, "attack3": pygame.K_k, "defend": pygame.K_h}
        }

        key = pygame.key.get_pressed()
        player_controls = controls[self.player]

        if self.alive and not self.attacking:
            if key[player_controls["left"]]:
                dx += self.move_left()
            if key[player_controls["right"]]:
                dx += self.move_right()
            if key[player_controls["jump"]]:
                self.perform_jump()
            if key[player_controls["attack1"]]:
                self.attack1(target)
            if key[player_controls["attack2"]]:
                self.attack2(target)
            if key[player_controls["attack3"]]:
                self.special_attack(target)
            if key[player_controls["defend"]]:
                self.defend()
                return  # Verteidigung unterbricht andere Aktionen

        self.vel_y += GRAVITY
        dy += self.vel_y

        # Spieler innerhalb des Bildschirms halten
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            dy = screen_height - 110 - self.rect.bottom
            self.jump = False

        self.rect.x += dx
        self.rect.y += dy

        # Richtung anpassen
        self.flip = target.rect.centerx < self.rect.centerx
    
    def move_left(self):
        dx = -self.SPEED
        self.running = True
        return dx

    def move_right(self):
        dx = self.SPEED
        self.running = True
        return dx

    def perform_jump(self):
        if not self.jump:  # Attribut bleibt gleich
            self.vel_y = -30
            self.jump = True

    def attack1(self, target):
        if self.attack_cooldown == 0:
            self.perform_attack(target, attack_type=1)

    def attack2(self, target):
        if self.attack_cooldown == 0:
            self.perform_attack(target, attack_type=2)

    def special_attack(self, target):
        if self.can_special:
            self.perform_attack(target, attack_type=3)
            self.mana = 0  # Mana zurücksetzen
            self.can_special = False  # Spezialattacke deaktivieren

    def defend(self):
        if self.defend_cooldown == 0:
            self.defending = True
            self.defend_cooldown = 50  # Cooldown für defend
            self.update_action("defend")

    
    def perform_attack(self, target, attack_type):
        self.attacking = True
        self.attack_sound.play()  
        self.attack_type = attack_type
        self.update_action(f"atk{attack_type}")

        attacking_rect = pygame.Rect(
            self.rect.centerx - (3 * self.rect.width if self.flip else 0), #Anrgiffsrechteck, das je nach True/False von Flip entweder vom Zentrum startet oder negativ verschoben wird
            self.rect.y,
            3 * self.rect.width,
            self.rect.height
        )
        if attacking_rect.colliderect(target.rect):
            if target.defending:
                target.health -= (5 * self.damage_multiplier)  # Reduzierter Schaden bei Verteidigung
            else:
                target.health -= (15 * self.damage_multiplier) if attack_type == 3 else (10 * self.damage_multiplier)
            target.hit = True

            # Mana aufladen bei erfolgreichem Treffer
            self.mana += self.max_mana / 4  # 1/4 des Maximalwertes
            if self.mana >= self.max_mana:
                self.mana = self.max_mana  
                self.can_special = True  # Spezialattacke freischalten


    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)     #  Self.flip je nach boolischem Wert horzontal geflipped, aber niemals Vertikal
        surface.blit(flipped_image, (self.rect.x + self.offset_x, self.rect.y + self.offset_y))  # Bild soll an der angegebenen Position gezeichnet werden