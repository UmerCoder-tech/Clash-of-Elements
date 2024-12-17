


import pygame

class MapSelectScreen:
    def __init__(self, screen, fonts, colors, maps):
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.maps = maps #dict mit allen maps
        self.running = True
        self.selected_map = None #die map die der benutzer auswählt welche dann auf true gesetzt wird

        # Positionen für die Maps
        self.map_positions = [
            (270, 150),  #Field od Fate  #150,150
            (520, 150),  #Buddha's Monestery
            (270, 350),  #castillo
            (520, 350),  #Emperor's Castle
        ]

        

    #unsichtbares Raster
    def draw_maps(self):
        #Hier werden die maps gezeichnet und die dazugehörigen namen
        for i, (map_name, map_data) in enumerate(self.maps.items()):
            x, y = self.map_positions[i]
            scaled_map = pygame.transform.scale(map_data["image"], (200, 150))
            self.screen.blit(scaled_map, (x, y))

            #Map namen darunter anzeigen
            text = self.fonts["name_font"].render(map_name, True, self.colors["RED"])
            text_rect = text.get_rect(center=(x + 100, y + 170))
            self.screen.blit(text, text_rect) #zeichnet namen auf dem bildschirm



    def handle_events(self):
        #Verabeitet die Mausereignisse
        for event in pygame.event.get(): #Nochmal schauen wieso die Quit funktion macht
            #Wenn der Benutzer das fenster über das rote x schließt werden alle prozesse beendet
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:    #prüft ob der benutzer eine mousetaste gedrückt hat
                pos = event.pos
                for i, (map_name, _) in enumerate(self.maps.items()):
                    x, y = self.map_positions[i]
                    map_rect = pygame.Rect(x, y, 200, 150)
                    if map_rect.collidepoint(pos): #prüft ob der Mausklick innerhalb des unsichtbaren rechtecks liegt
                        self.selected_map = map_name
                        self.running = False

    def run(self):
        #startet den screen damit er läuft und steuert ihn
        while self.running:
            self.screen.fill(self.colors["BLACK"])  # Hintergrund zeichnen
            self.draw_maps()  #zeigt die maps an und ihre Namen
            self.handle_events()  #verarbeitet die Mouseereignisse und prüft ob eine map ausgewählt wurde
            pygame.display.update()  #Aktualisiert Bildschirm um die änderung anzuzeigen in dem fall ausgewählt map
        return self.selected_map #gibt die ausgewählte map zurück




