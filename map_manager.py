


import pygame

class MapSelectScreen:
    def __init__(self, screen, fonts, colors, maps):
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.maps = maps
        self.running = True
        self.selected_map = None

        # Positionen für die Maps
        self.map_positions = [
            (150, 150),  # Desert
            (400, 150),  # Forest
            (150, 350),  # Volcano
            (400, 350),  # Ocean
        ]

    def draw_maps(self):
        """Zeichnet die Maps und ihre Namen."""
        for i, (map_name, map_data) in enumerate(self.maps.items()):
            x, y = self.map_positions[i]
            scaled_map = pygame.transform.scale(map_data["image"], (200, 150))
            self.screen.blit(scaled_map, (x, y))

            # Map-Namen darunter anzeigen
            text = self.fonts["name_font"].render(map_name, True, self.colors["WHITE"])
            text_rect = text.get_rect(center=(x + 100, y + 170))
            self.screen.blit(text, text_rect)

    def handle_events(self):
        """Verarbeitet die Mausereignisse für die Map-Auswahl."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for i, (map_name, _) in enumerate(self.maps.items()):
                    x, y = self.map_positions[i]
                    map_rect = pygame.Rect(x, y, 200, 150)
                    if map_rect.collidepoint(pos):
                        self.selected_map = map_name
                        self.running = False

    def run(self):
        """Startet den Auswahlbildschirm für die Maps."""
        while self.running:
            self.screen.fill(self.colors["BLACK"])  # Hintergrund zeichnen
            self.draw_maps()  # Maps anzeigen
            self.handle_events()  # Ereignisse verarbeiten
            pygame.display.update()  # Bildschirm aktualisieren
        return self.selected_map




