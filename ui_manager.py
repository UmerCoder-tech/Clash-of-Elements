
import pygame
from character_data import characters
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
        
        #zeichnet die Profilbilder der fighter unter die Healthbars
        """""
        self.character_images = {
            "Zuko": pygame.image.load("Zuko/zuko_pb.png"),
            "Susanoo": pygame.image.load("Susanoo/susanoo_pb.png"),
            "Basim": pygame.image.load("Basim/basim_pb_.png"),
            "Mai": pygame.image.load("Mai/mai_pb.png"),
            
        }
        """

    def set_map(self, map_name):
        """
        Setzt die aktuelle Map basierend auf dem Namen.
        :param map_name: Der Name der Map, die gesetzt werden soll.
        """
        if map_name in self.maps:
            self.current_map = self.maps[map_name]
        



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
        #profile_image = self.character_images.get(character_name)

        # Hole das Profilbild aus dem zentralen characters-Dictionary
        profile_image = characters.get(character_name, {}).get("loaded_profile_picture")

        # Sicherheitscheck: Wenn Bild nicht existiert
        if not profile_image:
            print(f"Fehler: Kein Bild für Charakter {character_name} gefunden.")
            return
    
        frame_width, frame_height = 54, 54
        profile_width, profile_height = 50, 50
        pygame.draw.rect(self.screen, self.colors["BLACK"], (x - 2, y - 2, frame_width, frame_height))  # Rahmen
        profile_image = pygame.transform.scale(profile_image, (profile_width, profile_height))
        self.screen.blit(profile_image, (x, y))

    

    def draw_player_names(self, fighter_1_data, fighter_2_data):
        """
        Zeigt die Namen der Spieler unterhalb der Mana-Balken an.
        Die Namen werden dynamisch zentriert basierend auf ihrer Länge.
        """
        name_font = self.fonts["name_font"]

        # Berechnung der Breite der Namen
        name1_width = name_font.size(fighter_1_data["attributes"]["name"])[0]
        name2_width = name_font.size(fighter_2_data["attributes"]["name"])[0]

        # Dynamische Positionen für die Namen
        #Hier an den Paramtern können die Namen alligned werden
        name1_x = 116 - name1_width // 2  # Zentriere unter Mana-Balken 1
        name2_x = 870 - name2_width // 2  # Zentriere unter Mana-Balken 2

        # Namen zeichnen
        self.draw_text(fighter_1_data["attributes"]["name"], name_font, self.colors["WHITE"], name1_x, 90)  # Y-Offset für Namen
        self.draw_text(fighter_2_data["attributes"]["name"], name_font, self.colors["WHITE"], name2_x, 90)


