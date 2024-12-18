import pygame
from buttons import Button  # Stelle sicher, dass die Button-Klasse importiert ist

class ButtonManager:
    def __init__(self, screen, fonts, colors, bg_image_path = None):
        """
        Initialisiert den ButtonManager.
        :param screen: Das Pygame-Hauptfenster.
        :param fonts: Dictionary mit Schriftarten.
        :param colors: Dictionary mit Farben.
        """
        self.screen = screen
        self.fonts = fonts
        self.colors = colors
        self.buttons = {}  # Speichert alle Buttons
        self.bg_image = None #Hntergrund unsere main_menus 



        # Lade Hintergrundbild, falls ein Pfad angegeben ist
        if bg_image_path:
            self.bg_image = pygame.image.load(bg_image_path) #Dahinter steckt der übergebene Pfad unseres Hintergrundbilds
            self.bg_image = pygame.transform.scale(self.bg_image, (screen.get_width(), screen.get_height())) #Das bild wird an die größe des Fensters angepasst 


    def create_buttons(self, screen_width, screen_height):
    #Die Start und Quit Buttons werden hier erzeugt und gesetzt 
        button_width = 350
        button_height = 80
        start_button_x = screen_width // 2 - button_width // 2
        start_button_y = screen_height // 2+ 45
        quit_button_x = screen_width // 2 - button_width // 2
        quit_button_y = screen_height // 2 + 125

        # Start-Button erstellen
        self.buttons["start"] = Button(
            image_path="ButtonRed/pngegg.png",
            x=start_button_x,
            y=start_button_y,
            new_width=button_width,
            new_height=button_height,
            text="Start",
            font=self.fonts["button_font"],
            text_color=self.colors["WHITE"]
        )

        # Quit-Button erstellen
        self.buttons["quit"] = Button(
            image_path="ButtonRed/pngegg.png",
            x=quit_button_x,
            y=quit_button_y,
            new_width=button_width,
            new_height=button_height,
            text="Quit",
            font=self.fonts["button_font"],
            text_color=self.colors["WHITE"]
        )

    def draw_buttons(self):
        """Zeichnet die Buttons auf dem Bildschirm."""
        if self.bg_image:
            self.screen.blit(self.bg_image, (0, 0)) #Bei dieswr if-Anweisung wird ein das hinterlegte Hintergrundbild gezeichnet


        for button in self.buttons.values(): #zeichnet alle buttons
            button.draw(self.screen) 
        

    def get_buttons(self):
        """Gibt das Button-Dictionary zurück."""
        return self.buttons #gibt es Dict. Buttons wieder kann an mehreren stellen verwendet werden
