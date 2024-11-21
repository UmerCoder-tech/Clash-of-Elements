import pygame

pygame.init()

class CharacterSelectScreen:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selecting = True
        self.selected_character = None

        # Bilder für die Charaktere laden
        self.zuko_image = pygame.image.load("Zuko/zuko_pb.png")
        self.susanoo_image = pygame.image.load("Susanoo/susanoo_pb.png")

        # Optional: Die Bilder skalieren (Größe anpassen)
        self.zuko_image = pygame.transform.scale(self.zuko_image, (150, 150))
        self.susanoo_image = pygame.transform.scale(self.susanoo_image, (150, 150))

        # Positionen für die Charakterbilder
        self.zuko_pos = (self.screen_width // 4 - 75, self.screen_height // 2 - 75)
        self.susanoo_pos = (3 * self.screen_width // 4 - 75, self.screen_height // 2 - 75)

        # Rechtecke für die Interaktion definieren
        self.zuko_rect = pygame.Rect(self.zuko_pos[0], self.zuko_pos[1], 150, 150)
        self.susanoo_rect = pygame.Rect(self.susanoo_pos[0], self.susanoo_pos[1], 150, 150)

    def draw(self):
        # Hintergrundfarbe oder Bild
        self.screen.fill((0, 0, 0))  # Farbe Schwarz

        # Charakterbilder zeichnen
        self.screen.blit(self.zuko_image, self.zuko_pos)
        self.screen.blit(self.susanoo_image, self.susanoo_pos)

        # Mausposition für Hover-Effekte überprüfen
        mouse_pos = pygame.mouse.get_pos()
        if self.zuko_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (128, 0, 128), self.zuko_rect, 3)  # Rahmen zeichnen
        elif self.susanoo_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, (128, 0, 128), self.susanoo_rect, 3)  # Rahmen zeichnen

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.zuko_rect.collidepoint(mouse_pos):
                    self.selected_character = "Zuko"
                    self.selecting = False
                elif self.susanoo_rect.collidepoint(mouse_pos):
                    self.selected_character = "Susanoo"
                    self.selecting = False

    def run(self):
        while self.selecting:
            self.draw()
            self.handle_events()
            pygame.display.update()

        return self.selected_character

