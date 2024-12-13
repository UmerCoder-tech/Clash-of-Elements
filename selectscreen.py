"""""
#Muss überarbeitet werden
import pygame
pygame.init()

class CharacterSelectScreen:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selecting = True

        
        # Charaktere mit Bildern laden
        self.characters = {
            "Zuko": {
                "profil_bild": pygame.transform.scale(pygame.image.load("Zuko/zuko_pb.png"), (150, 150)),
            },
            "Susanoo": {
                "profil_bild": pygame.transform.scale(pygame.image.load("Susanoo/susanoo_pb.png"), (150, 150)),
            },
            "Basim": {
                "profil_bild": pygame.transform.scale(pygame.image.load("Basim/basim_pb_.png"), (150, 150)),
            },
            "Mai": {
                "profil_bild": pygame.transform.scale(pygame.image.load("Mai/mai_pb.png"), (150, 150)),
            },
        }
        
        # Positionen und Rechtecke als Dictionaries initialisieren
        self.character_positions = {}
        self.character_rects = {}

        # Dynamische Anordnung der Charakterbilder
        total_width = len(self.characters) * 150 + (len(self.characters) - 1) * 20
        start_x = (self.screen_width - total_width) // 2
        y_position = self.screen_height // 2 - 75

        for i, (name, data) in enumerate(self.characters.items()):
            x_position = start_x + i * (150 + 20)
            self.character_positions[name] = (x_position, y_position)
            self.character_rects[name] = pygame.Rect(x_position, y_position, 150, 150)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Hintergrundfarbe Schwarz

        # Charakterbilder und Rahmen zeichnen
        mouse_pos = pygame.mouse.get_pos()
        for name, data in self.characters.items():
            rect = self.character_rects[name]
            self.screen.blit(data["profil_bild"], (rect.x, rect.y))
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (128, 0, 128), rect, 3)  # Rahmen zeichnen

        pygame.display.update()

    def handle_events(self, selected_characters):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for name, rect in self.character_rects.items():
                    if rect.collidepoint(mouse_pos) and name not in selected_characters:
                        selected_characters.append(name)
                        print(f"{name} ausgewählt")

    def run(self):
        selected_characters = []  # Liste für die ausgewählten Charaktere

        while len(selected_characters) < 2:
            self.draw()
            self.handle_events(selected_characters)

        print(f"Ausgewählte Charaktere: {selected_characters}")
        return selected_characters


        

        

import pygame

pygame.init()


class CharacterSelectScreen:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selecting = True

        # Charaktere mit Bildern laden
        self.characters = {
            "Zuko": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Zuko/zuko_pb.png"), (150, 150)
                ),
            },
            "Susanoo": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Susanoo/susanoo_pb.png"), (150, 150)
                ),
            },
            "Basim": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Basim/basim_pb_.png"), (150, 150)
                ),
            },
            "Mai": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Mai/mai_pb.png"), (150, 150)
                ),
            },
        }

        # Positionen und Rechtecke als Dictionaries initialisieren
        self.character_positions = {}
        self.character_rects = {}

        # Dynamische Anordnung der Charakterbilder
        total_width = len(self.characters) * 150 + (len(self.characters) - 1) * 20
        start_x = (self.screen_width - total_width) // 2
        y_position = self.screen_height // 2 - 75

        for i, (name, data) in enumerate(self.characters.items()):
            x_position = start_x + i * (150 + 20)
            self.character_positions[name] = (x_position, y_position)
            self.character_rects[name] = pygame.Rect(x_position, y_position, 150, 150)

        # Schrift für die Labels
        self.font = pygame.font.Font(None, 36)

    def draw(self, selected_characters):
        self.screen.fill((0, 0, 0))  # Hintergrundfarbe Schwarz

        # Charakterbilder und Rahmen zeichnen
        mouse_pos = pygame.mouse.get_pos()
        for i, (name, data) in enumerate(self.characters.items()):
            rect = self.character_rects[name]
            self.screen.blit(data["profil_bild"], (rect.x, rect.y))

            # Hover-Effekt
            if rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, (128, 0, 128), rect, 3)

            # Spieler 1 und Spieler 2 Auswahl anzeigen
            if name in selected_characters:
                color = (0, 0, 255) if selected_characters.index(name) == 0 else (255, 0, 0)
                pygame.draw.rect(self.screen, color, rect, 5)  # Rahmenfarbe
                label = "P1" if selected_characters.index(name) == 0 else "P2"
                text = self.font.render(label, True, color)
                self.screen.blit(text, (rect.right - 40, rect.top + 10))

        pygame.display.update()

    def handle_events(self, selected_characters):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for name, rect in self.character_rects.items():
                    if rect.collidepoint(mouse_pos) and name not in selected_characters:
                        selected_characters.append(name)
                        print(f"{name} ausgewählt")

    def run(self):
        selected_characters = []  # Liste für die ausgewählten Charaktere

        while len(selected_characters) < 2:
            self.draw(selected_characters)
            self.handle_events(selected_characters)

        print(f"Ausgewählte Charaktere: {selected_characters}")
        return selected_characters


# Beispiel zum Testen
if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Charakterauswahl")
    select_screen = CharacterSelectScreen(screen, 800, 600)
    selected = select_screen.run()
    print(f"Endgültige Auswahl: {selected}")
    pygame.quit()

"""

import pygame
import time

pygame.init()

class CharacterSelectScreen:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selecting = True

        # Charaktere mit Bildern laden
        self.characters = {
            "Zuko": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Zuko/zuko_pb.png"), (100, 100)
                ),
            },
            "Susanoo": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Susanoo/susanoo_pb.png"), (100, 100)
                ),
            },
            "Basim": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Basim/basim_pb_.png"), (100, 100)
                ),
            },
            "Mai": {
                "profil_bild": pygame.transform.scale(
                    pygame.image.load("Mai/mai_pb.png"), (100, 100)
                ),
            },
        }

        # Positionen und Rechtecke als Dictionaries initialisieren
        self.character_positions = {}
        self.character_rects = {}

        # Dynamische Anordnung der Charakterbilder (klein und nach oben verschoben)
        total_width = len(self.characters) * 120 + (len(self.characters) - 1) * 20
        start_x = (self.screen_width - total_width) // 2
        y_position = self.screen_height // 4  # Nach oben verschoben

        for i, (name, data) in enumerate(self.characters.items()):
            x_position = start_x + i * (100 + 20)
            self.character_positions[name] = (x_position, y_position)
            self.character_rects[name] = pygame.Rect(x_position, y_position, 100, 100)

        # Schrift für die Labels
        self.font = pygame.font.Font(None, 36)

    def draw(self, selected_characters):
        self.screen.fill((0, 0, 0))  # Hintergrundfarbe Schwarz

        # Charakterbilder zeichnen
        for name, data in self.characters.items():
            rect = self.character_rects[name]
            self.screen.blit(data["profil_bild"], (rect.x, rect.y))

            # Raster und "P1"/"P2" anzeigen
            if name in selected_characters:
                if selected_characters.index(name) == 0:  # Spieler 1
                    pygame.draw.rect(self.screen, (0, 0, 255), rect, 5)  # Blauer Rahmen
                    label = self.font.render("P1", True, (0, 0, 255))
                    self.screen.blit(label, (rect.right - 30, rect.top + 5))
                elif selected_characters.index(name) == 1:  # Spieler 2
                    pygame.draw.rect(self.screen, (255, 0, 0), rect, 5)  # Roter Rahmen
                    label = self.font.render("P2", True, (255, 0, 0))
                    self.screen.blit(label, (rect.right - 30, rect.top + 5))

        # Ausgewählte Charaktere groß anzeigen
        if len(selected_characters) > 0:
            left_char = self.characters[selected_characters[0]]
            left_image = pygame.transform.scale(left_char["profil_bild"], (200, 200))
            self.screen.blit(left_image, (50, self.screen_height // 2))

        if len(selected_characters) > 1:
            right_char = self.characters[selected_characters[1]]
            right_image = pygame.transform.scale(right_char["profil_bild"], (200, 200))
            self.screen.blit(right_image, (self.screen_width - 250, self.screen_height // 2))

        pygame.display.update()

    def handle_events(self, selected_characters):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for name, rect in self.character_rects.items():
                    if rect.collidepoint(mouse_pos) and name not in selected_characters:
                        selected_characters.append(name)
                        print(f"{name} ausgewählt")

    def run(self):
        selected_characters = []  # Liste für die ausgewählten Charaktere

        pygame.mixer.music.load("Audio/Ryus Ost.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1, 0.0, 5000)

        while len(selected_characters) < 2:
            self.draw(selected_characters)
            self.handle_events(selected_characters)

        # Verbleiben auf dem Screen für 3 Sekunden
        self.draw(selected_characters)  # Finales Zeichnen
        pygame.display.update()
        time.sleep(3)
        
        pygame.mixer.music.stop()

        print(f"Ausgewählte Charaktere: {selected_characters}")
        return selected_characters

"""""
# Beispiel zum Testen
if __name__ == "__main__":
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Charakterauswahl")
    select_screen = CharacterSelectScreen(screen, 800, 600)
    selected = select_screen.run()
    print(f"Endgültige Auswahl: {selected}")
    pygame.quit()
"""