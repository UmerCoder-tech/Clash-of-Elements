import pygame

class Champion:
    def __init__(self, player, x, y, animations, sound):
        self.player = player
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.attack_cooldown = 0
        self.health = 100
        self.alive = True
        self.hit = False
        self.flip = False
        self.defending = False  # Zustand für defend
        self.defend_cooldown = 0  # Cooldown für defend
        self.mana = 0
        self.max_mana = 100  # Maximalwert der Mana-Bar
        self.can_special = False  # Gibt an, ob die Spezialattacke verfügbar ist
        self.attack_sound = sound 


        # Animationen
        self.animations = animations
        self.action = "idle"
        self.frame_index = 0
        self.image = self.animations[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()

        # Offset
        self.offset_x = (self.rect.width - self.image.get_width()) // 2
        self.offset_y = (self.rect.height - self.image.get_height()) // 2 - 110

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.update_action("death")
        elif self.hit:
            self.update_action("take_hit")
        elif self.attacking:
            if self.attack_type == 1:
                self.update_action("atk1")
            elif self.attack_type == 2:
                self.update_action("atk2")
            elif self.attack_type == 3:
                self.update_action("atk3")
        elif self.defending:
            self.update_action("defend")  # Verteidigungsanimation
        elif self.jump:
            self.update_action("jump")
        elif self.running:
            self.update_action("run")
        else:
            self.update_action("idle")

        # Animation aktualisieren
        animation_cooldown = 50
        self.image = self.animations[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        # Animation zurücksetzen, wenn sie abgeschlossen ist
        if self.frame_index >= len(self.animations[self.action]):
            if not self.alive:
                self.frame_index = len(self.animations[self.action]) - 1
            else:
                self.frame_index = 0
                if self.action.startswith("atk"):
                    self.attacking = False
                    self.attack_cooldown = 20
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
        SPEED = 10
        GRAVITY = 2
        dx, dy = 0, 0
        self.running = False

        # Angriffscooldown reduzieren
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        # Verteidigungs-Cooldown
        if self.defend_cooldown > 0:
            self.defend_cooldown -= 1

        controls = {
            1: {"left": pygame.K_a, "right": pygame.K_d, "jump": pygame.K_w, "attack1": pygame.K_r, "attack2": pygame.K_t, "attack3": pygame.K_z, "defend": pygame.K_f},
            2: {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "jump": pygame.K_UP, "attack1": pygame.K_u, "attack2": pygame.K_i, "attack3": pygame.K_k, "defend": pygame.K_h}
        }

        key = pygame.key.get_pressed()
        player_controls = controls[self.player]

        if self.alive and not self.attacking:
            if key[player_controls["left"]]:
                dx = -SPEED
                self.running = True
            if key[player_controls["right"]]:
                dx = SPEED
                self.running = True
            if key[player_controls["jump"]] and not self.jump:
                self.vel_y = -30
                self.jump = True
            if key[player_controls["attack1"]] and self.attack_cooldown == 0:
                self.attack(target, attack_type=1)
            if key[player_controls["attack2"]] and self.attack_cooldown == 0:
                self.attack(target, attack_type=2)
            if key[player_controls["attack3"]] and self.can_special:
                self.attack(target, attack_type=3)
                self.mana = 0  # Mana zurücksetzen
                self.can_special = False  # Spezialattacke deaktivieren


            # Verteidigungsaktion
            if key[player_controls["defend"]] and self.defend_cooldown == 0:
                self.defending = True
                self.defend_cooldown = 50  # Cooldown für defend
                self.update_action("defend")
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

    def attack(self, target, attack_type):
        self.attacking = True
        self.attack_sound.play()
        self.attack_type = attack_type
        self.update_action(f"atk{attack_type}")

        attacking_rect = pygame.Rect(
            self.rect.centerx - (3 * self.rect.width if self.flip else 0),
            self.rect.y,
            3 * self.rect.width,
            self.rect.height
        )
        if attacking_rect.colliderect(target.rect):
            if target.defending:
                target.health -= 5  # Reduzierter Schaden bei Verteidigung
            else:
                target.health -= 15 if attack_type == 3 else 10
            target.hit = True

            # Mana aufladen bei erfolgreichem Treffer
            self.mana += self.max_mana / 4  # 1/3 des Maximalwertes
            if self.mana >= self.max_mana:
                self.mana = self.max_mana  # Begrenzung auf Maximalwert
                self.can_special = True  # Spezialattacke freischalten


    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, (self.rect.x + self.offset_x, self.rect.y + self.offset_y))
