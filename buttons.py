
#Muss noch angepasst werden 

import pygame

class AnimatedButton:
    def __init__(self, image_paths, x, y, new_width, new_height, animation_speed=0.1):
        self.frames = [pygame.transform.scale(pygame.image.load(path), (new_width, new_height)) for path in image_paths]
        self.current_frame = 0
        self.animation_speed = animation_speed  # Geschwindigkeit der Animation (Sekunden pro Frame)
        self.time_since_last_frame = 0
        self.x = x
        self.y = y
        self.frame_width = new_width
        self.frame_height = new_height

    def update(self, dt):
        # Aktualisiere die Animation
        self.time_since_last_frame += dt
        if self.time_since_last_frame >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.time_since_last_frame = 0

    def draw(self, screen):
        # Zeichne den aktuellen Frame
        screen.blit(self.frames[self.current_frame], (self.x, self.y))

    def is_clicked(self, mouse_pos):
        # Überprüfe, ob der Button angeklickt wurde
        rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)
        return rect.collidepoint(mouse_pos)
