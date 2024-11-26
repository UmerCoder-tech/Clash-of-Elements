
#Muss überarbeitet werden
import pygame
pygame.init()
"""""
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
        self.basim_image = pygame.image.load("Basim/basim_pb.png")
        self.mai_image = pygame.image.load("Mai/mai_pb.png")

        # Optional: Die Bilder skalieren (Größe anpassen)
        self.zuko_image = pygame.transform.scale(self.zuko_image, (150, 150))
        self.susanoo_image = pygame.transform.scale(self.susanoo_image, (150, 150))
        self.basim_image = pygame.transform.scale(self.basim_image, (150,150))

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
                
            
    
    #Liste wird erstellt wo alle charaktere hinzugefügt werden können
    def run(self):
        ausgewählter_charaktere = []
        
        while len(ausgewählter_charaktere) <2:
            self.draw()
            self.handle_events(ausgewählter_charaktere)
            pygame.display.update()
        return ausgewählter_charaktere




        #while self.selecting:
            #self.draw()
            #self.handle_events()
            #pygame.display.update()

        #return self.selected_character

"""

class CharacterSelectScreen:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selecting = True
        self.selected_character = None

        # Bilder für die Charaktere laden
        self.character_images = [
            pygame.transform.scale(pygame.image.load("Zuko/zuko_pb.png"), (150, 150)),
            pygame.transform.scale(pygame.image.load("Susanoo/susanoo_pb.png"), (150, 150)),
            pygame.transform.scale(pygame.image.load("Basim/basim_pb_.png"), (150, 150)),
            pygame.transform.scale(pygame.image.load("Mai/mai_pb.png"), (150, 150)),
        ]

        self.character_names = ["Zuko", "Susanoo", "Basim", "Mai"]

        # Dynamische Anordnung der Charakterbilder
        total_width = len(self.character_images) * 150 + (len(self.character_images) - 1) * 20
        start_x = (self.screen_width - total_width) // 2
        y_position = self.screen_height // 2 - 75

        self.character_positions = []
        self.character_rects = []

        for i, image in enumerate(self.character_images):
            x_position = start_x + i * (150 + 20)
            self.character_positions.append((x_position, y_position))
            self.character_rects.append(pygame.Rect(x_position, y_position, 150, 150))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Hintergrundfarbe Schwarz

        # Charakterbilder und Rahmen zeichnen
        mouse_pos = pygame.mouse.get_pos()
        for i, (image, rect) in enumerate(zip(self.character_images, self.character_rects)):
            self.screen.blit(image, (rect.x, rect.y))
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
                for i, rect in enumerate(self.character_rects):
                    if rect.collidepoint(mouse_pos) and self.character_names[i] not in selected_characters:
                        selected_characters.append(self.character_names[i])
                        print(f"{self.character_names[i]} ausgewählt")


    def run(self):
        selected_characters = []  # Liste für die ausgewählten Charaktere

        while len(selected_characters) < 2:
            self.draw()
            self.handle_events(selected_characters)

        print(f"Ausgewählte Charaktere: {selected_characters}")
        return selected_characters





