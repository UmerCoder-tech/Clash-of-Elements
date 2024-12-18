
"""""
import pygame
from buttons import Button

class MainMenu:
    def __init__(self, screen, fonts, colors, clock, game_manager, bg_image, FPS):
        
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.clock = clock
        self.game_manager = game_manager
        self.bg_image = bg_image
        self.FPS = FPS

        # Button-Positionen und Größen
        self.button_width = 200
        self.button_height = 80
        self.start_button_x = self.screen.get_width() // 2 - self.button_width // 2
        self.start_button_y = self.screen.get_height() // 2 - self.button_height - 40
        self.quit_button_x = self.screen.get_width() // 2 - self.button_width // 2
        self.quit_button_y = self.screen.get_height() // 2 + 40

        # Buttons erstellen
        self.start_button = Button(
            image_path="ButtonRed/pngegg.png",
            x=self.start_button_x,
            y=self.start_button_y,
            new_width=self.button_width,
            new_height=self.button_height,
            text="Start",
            font=self.fonts["button_font"],
            text_color=self.colors["WHITE"]
        )

        self.quit_button = Button(
            image_path="ButtonRed/pngegg.png",
            x=self.quit_button_x,
            y=self.quit_button_y,
            new_width=self.button_width,
            new_height=self.button_height,
            text="Quit",
            font=self.fonts["button_font"],
            text_color=self.colors["WHITE"]
        )

    def run(self):
        
        menu_running = True

        while menu_running:
            dt = self.clock.tick(self.FPS) / 1000  # Delta-Zeit
            self.screen.fill(self.colors["BLACK"])

            # Hintergrund zeichnen
            scaled_bg = pygame.transform.scale(self.bg_image, (self.screen.get_width(), self.screen.get_height()))
            self.screen.blit(scaled_bg, (0, 0))

            # Buttons zeichnen
            self.start_button.draw(self.screen)
            self.quit_button.draw(self.screen)

            # Ereignisse verarbeiten
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_manager.running = False
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.start_button.is_clicked(event.pos):
                        self.game_manager.game_state = "character_select"
                        menu_running = False  # Hauptmenü verlassen
                    if self.quit_button.is_clicked(event.pos):
                        pygame.quit()
                        exit()

            pygame.display.update()
            self.clock.tick(self.FPS)
"""