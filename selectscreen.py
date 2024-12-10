
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




