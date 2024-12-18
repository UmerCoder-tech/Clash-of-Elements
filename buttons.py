# Hinweis: Die grundlegende Struktur und Funktionalität der buttons.py wurde von einem Youtube Video hergeleitet.
# Quelle: [https://www.youtube.com/watch?v=G8MYGDf_9ho]
#
# Übernommene Elemente:
# -collide logik: maus mit button
# -Methode für Draw: Buttons werden gezeichnet
#
# Änderungen und Eigenleistung:
# 1. Neue Mechaniken:
#    - Code aus dem Video wurde für unser spiel angepasst.



import pygame

class Button:
    def __init__(self, image_path, x, y, new_width, new_height, text="", font=None, text_color=(255, 255, 255)):
        # Lade das Button-Bild und skaliere es
        self.image = pygame.transform.scale(pygame.image.load(image_path), (new_width, new_height))
        self.x = x
        self.y = y
        self.width = new_width
        self.height = new_height
        self.text = text
        self.font = font
        self.text_color = text_color

    def draw(self, screen):
        # Zeichne den Button
        screen.blit(self.image, (self.x, self.y))
        
        # Render den Text
        if self.text and self.font:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
            screen.blit(text_surface, text_rect)


    def is_clicked(self, mouse_pos):
        # Überprüfe, ob der Button angeklickt wurde
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect.collidepoint(mouse_pos)
