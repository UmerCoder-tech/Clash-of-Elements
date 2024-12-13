
import pygame

class UIManager:
    def __init__(self, screen, fonts, colors, draw_text,maps):
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.draw_text = draw_text
        self.maps = maps
        self.current_map = None
        
        
        # Ressourcen zentral laden
        #self.bg_image = pygame.image.load("Hintergrund/Fate's Moon.png")
        self.current_map = None
        
        self.character_images = {
            "Zuko": pygame.image.load("Zuko/zuko_pb.png"),
            "Susanoo": pygame.image.load("Susanoo/susanoo_pb.png"),
            "Basim": pygame.image.load("Basim/basim_pb_.png"),
            "Mai": pygame.image.load("Mai/mai_pb.png"),
        }

    def set_map(self, map_name):
        """
        Setzt die aktuelle Map basierend auf dem Namen.
        :param map_name: Der Name der Map, die gesetzt werden soll.
        """
        if map_name in self.maps:
            self.current_map = self.maps[map_name]
        else:
            print(f"Fehler: Map '{map_name}' existiert nicht.")
        

    def draw_bg(self):
        """Zeichnet den Hintergrund."""
        scaled_bg = pygame.transform.scale(self.bg_image, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(scaled_bg, (0, 0))

    def draw_health_bar(self, health, x, y):
        hb_width = 400
        hb_height = 30
        ratio = health / 100
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, hb_width + 4, hb_height + 4))  # Rahmen
        pygame.draw.rect(self.screen, self.colors["WHITE"], (x, y, hb_width, hb_height))  # Hintergrund
        pygame.draw.rect(self.screen, self.colors["LILA"], (x, y, hb_width * ratio, hb_height))  # Lebensbalken

    def draw_mana_bar(self, mana, x, y):
        mb_width = 300
        mb_height = 20
        ratio = mana / 100
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, mb_width + 4, mb_height + 4))  # Rahmen
        pygame.draw.rect(self.screen, self.colors["WHITE"], (x, y, mb_width, mb_height))  # Hintergrund
        pygame.draw.rect(self.screen, self.colors["MIDNIGHT_BLUE"], (x, y, mb_width * ratio, mb_height))  # Manabalken

        if mana >= 100:
            self.draw_text(
                "Critical Attack Ready!", 
                self.fonts["ready_attack_font"], 
                self.colors["WHITE"], 
                x + mb_width // 2 - 50, 
                y + mb_height // 2 - 10
            )

    def draw_champion_profilepicture(self, character_name, x, y):
        #Zeichnet das Profilbild des ausgewählten Charakters.
        profile_image = self.character_images.get(character_name)

        # Sicherheitscheck: Wenn Bild nicht existiert
        if not profile_image:
            print(f"Fehler: Kein Bild für Charakter {character_name} gefunden.")
            return
    
        frame_width, frame_height = 54, 54
        profile_width, profile_height = 50, 50
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, frame_width, frame_height))  # Rahmen
        profile_image = pygame.transform.scale(profile_image, (profile_width, profile_height))
        self.screen.blit(profile_image, (x, y))
    
    """""
    def draw_champion_name(self, character_name, x, y):
        #Zeichnet den Namen eines Charakters unterhalb der Healthbar.
        name_font = self.fonts["name_font"]
        name_color = self.colors["WHITE"]
        # Text zeichnen
        name_text = name_font.render(character_name, True, name_color)
        name_rect = name_text.get_rect(center=(x + 180, y + 50))  # x + 200 zentriert den Namen unter einer 400px-Healthbar
        self.screen.blit(name_text, name_rect)
    """

