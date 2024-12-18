import pygame
import time
from character_data import characters
from ressource import fonts

pygame.init()

class CharacterSelectScreen:
    def __init__(self, screen, screen_width, screen_height, fonts):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selecting = True #zustand ob noch ausgewählt wird
        self.characters = characters #import: character dict. aius character_data.py
        # Charaktere mit Bildern laden
        #Dictionary anpassung soll der main zugegriffen werden selbe logik wie bei den spritesheets
        # Im Konstruktor hinzufügen:
        self.fonts = fonts  # Fonts-Dictionary übernehmen
        self.vs_image = pygame.image.load("images/Versus.png")
        self.vs_image = pygame.transform.scale(self.vs_image, (250, 250))  # Skalieren falls nötig

        # Positionen und Rechtecke als Dictionaries initialisieren
        self.character_positions = {} #speichert x und y posis. der Charaktere
        self.character_profile_box = {} #speichert rechtecke für die Kollisionsprüfung der Pb's
 
        #Schrift für die Raster(P1,P2)
        self.font = pygame.font.Font(None, 36)
        
        # Dynamische Anordnung der Charakterbilder (oben mittig)
        image_width = 100  #Breite eines Bildes
        spacing = 20  #Abstand zwischen den Bildern

        #Berechne die gesamte Breite aller Bilder und Abstände
        total_width = len(self.characters) * image_width + (len(self.characters) - 1) * spacing

        #Berechne die Startposition (zentriert oben auf dem Bildschirm)
        start_x = (self.screen_width - total_width) // 2
        y_position = self.screen_height // 4  # Position nach oben verschoben (1/6 des Bildschirms) #6

        #Charakterpositionen und Rechtecke berechnen
        for i, (name, data) in enumerate(self.characters.items()):
            x_position = start_x + i * (image_width + spacing)
            self.character_positions[name] = (x_position, y_position)
            self.character_profile_box[name] = pygame.Rect(x_position, y_position, image_width, image_width)


    def draw_raster(self, selected_characters):   #diese draw funktion in draw_raster umändern
        self.screen.fill((0, 0, 0))  # Hintergrundfarbe Schwarz
        title_text = fonts["select_font"].render("CHOOSE YOUR FIGHTERS", True, ("RED"))  # Weißer Text
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 50))  # Zentriert oben
        self.screen.blit(title_text, title_rect)  # Zeige den Text auf dem Bildschirm an


        # Charakterbilder zeichnen
        for name, data in self.characters.items():
            rect = self.character_profile_box[name]
            self.screen.blit(data["loaded_profile_picture"], (rect.x, rect.y))

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
            left_image = pygame.transform.scale(left_char["loaded_profile_picture"], (200, 200))
            self.screen.blit(left_image, (50, self.screen_height // 2))

            # VS-Bild zwischen den großen Profilbildern anzeigen
            vs_x = (self.screen_width // 2) - (self.vs_image.get_width() // 2)  # Zentriert in der Mitte
            vs_y = self.screen_height // 2  # Gleiche Y-Position wie die großen Bilder
            self.screen.blit(self.vs_image, (vs_x, vs_y))

        if len(selected_characters) > 1:
            right_char = self.characters[selected_characters[1]]
            right_image = pygame.transform.scale(right_char["loaded_profile_picture"], (200, 200))
            self.screen.blit(right_image, (self.screen_width - 250, self.screen_height // 2))


        pygame.display.update()
    #Handlet die Mousebutton eingaben der Mauszeiger den innerhalb des Rahmens erkannt wird
    def handle_events(self, selected_characters):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for name, rect in self.character_profile_box.items():
                    if rect.collidepoint(mouse_pos) and name not in selected_characters:
                        selected_characters.append(name)
                        #print(f"{name} ausgewählt")

    
    def run(self):
        selected_characters = []  # Liste für die ausgewählten Charaktere

        while len(selected_characters) < 2:
            self.draw_raster(selected_characters)
            self.handle_events(selected_characters)

        # Verbleiben auf dem Screen für 3 Sekunden
        self.draw_raster(selected_characters)  # Finales Zeichnen
        pygame.display.update()
        time.sleep(3) #für 3000ms noch bleiben
        
        #pygame.mixer.music.stop()

        print(f"Ausgewählte Charaktere: {selected_characters}")
        return selected_characters

