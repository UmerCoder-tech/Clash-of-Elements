import pygame 
pygame.init()

# Farben
colors = {
    "LILA": (128, 0, 128),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "MIDNIGHT_BLUE": (25, 25, 112),
    "SILBER": (192, 192, 192),
    "GOLD": (255, 215, 0),
    "DUNKEL_GRÜN": (0, 100, 0),
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255)
}



# Schriften
fonts = {
    "count_font": pygame.font.Font("Fonts/Orbitron.ttf", 180),
    "score_font": pygame.font.Font("Fonts/Orbitron.ttf", 100),
    "ready_attack_font": pygame.font.Font("Fonts/Oswald.ttf", 16),
    "name_font": pygame.font.Font("Fonts/Oswald.ttf", 28),
    "fight_font": pygame.font.Font("Fonts/Oswald.ttf", 300),
    "berserk_front": pygame.font.Font("Fonts/MetalMania.ttf", 120),
    "winner_font": pygame.font.Font("Fonts/Oswald.ttf", 150),
    "button_font": pygame.font.Font(None, 36),  # Schriftart für den Button
    "select_font": pygame.font.Font("Fonts/VT323-Regular.ttf", 120)

}


maps = {
        "Field of Fate": {
            "image": pygame.image.load("Hintergrund/Fate's Moon.png"),
            "music": "Audio/Ryus Ost.mp3",
            "offset_x": 10,
            "offset_y": -100,
        },
        "Buddha's Monastery": {
            "image": pygame.image.load("Hintergrund/Buddha_Monisstery.png"),
            "music": "Audio/BuddhaMUSIC.mp3",
            "offset_x": 20,
            "offset_y": -90,   #-120
        },
        "Castillo": {
            "image": pygame.image.load("Hintergrund/castle.png"),
            "music": "Audio/VegaSOUND.mp3",
            "offset_x": 5,
            "offset_y": -90,
        },
        "Emperor's Castle": {
            "image": pygame.image.load("Hintergrund/susuki_castle.png"),
            "music": "Audio/SuzukiMUSIC.mp3",
            "offset_x": 15,
            "offset_y": -110,
        },
    }


