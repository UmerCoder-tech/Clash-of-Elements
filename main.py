import pygame
from pygame import mixer
from buttons import AnimatedButton
from spritesheets import animations_zuko, animations_susanoo
from champion import Champion
from gamestate import GameLogic
from selectscreen import CharacterSelectScreen

pygame.init()
mixer.init()

# Bildschirmgröße und Framerate
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

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
    "BLUE": (0, 0, 255),
}

# Schriftarten definieren
fonts = {
    "count_font": pygame.font.Font("Fonts/Orbitron.ttf", 180),
    "score_font": pygame.font.Font("Fonts/Orbitron.ttf", 30),
    "ready_attack_font": pygame.font.Font("Fonts/Oswald.ttf", 16),
    "name_font": pygame.font.Font("Fonts/Oswald.ttf", 28),
    "fight_font": pygame.font.Font("Fonts/Oswald.ttf", 300),
    "berserk_font": pygame.font.Font("Fonts/MetalMania.ttf", 30),
    "winner_font": pygame.font.Font("Fonts/Oswald.ttf", 150),
}

# Hintergrundmusik und Soundeffekte
mixer.music.load("Audio/Ryus Ost.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1, 0.0, 5000)

dragon_slayer_fx = pygame.mixer.Sound("Audio/assets_audio_magic.wav")
dragon_slayer_fx.set_volume(0.5)
katana_fx = pygame.mixer.Sound("Audio/assets_audio_sword.wav")
katana_fx.set_volume(0.5)

# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Fighting Game")
clock = pygame.time.Clock()

# Hintergrundbild laden
bg_image = pygame.image.load("Hintergrund/Fate's Moon.png")

# Profilbilder laden
susanoo_pb = pygame.image.load("Susanoo/susanoo_pb.png")
zuko_pb = pygame.image.load("Zuko/zuko_pb.png")

# Funktion zum Zeichnen
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

def draw_health_bar(health, x, y):
    hb_width = 400
    hb_height = 30
    ratio = health / 100
    pygame.draw.rect(screen, colors["BLACK"], (x - 2, y - 2, hb_width + 4, hb_height + 4))
    pygame.draw.rect(screen, colors["WHITE"], (x, y, hb_width, hb_height))
    pygame.draw.rect(screen, colors["LILA"], (x, y, hb_width * ratio, hb_height))

def draw_mana_bar(mana, x, y):
    mb_width, mb_height = 300, 20
    ratio = mana / 100
    pygame.draw.rect(screen, colors["BLACK"], (x - 2, y - 2, mb_width + 4, mb_height + 4))
    pygame.draw.rect(screen, colors["WHITE"], (x, y, mb_width, mb_height))
    pygame.draw.rect(screen, colors["MIDNIGHT_BLUE"], (x, y, mb_width * ratio, mb_height))
    if mana >= 100:
        text_img = fonts["ready_attack_font"].render("Critical Attack Ready!", True, colors["WHITE"])
        text_rect = text_img.get_rect(center=(x + mb_width // 2, y + mb_height // 2))
        screen.blit(text_img, text_rect)

def draw_fighter_profilepicture(profile_image, x, y):
    frame_width, frame_height = 54, 54
    profile_width, profile_height = 50, 50
    pygame.draw.rect(screen, colors["BLACK"], (x - 2, y - 2, frame_width, frame_height))
    profile_image = pygame.transform.scale(profile_image, (profile_width, profile_height))
    screen.blit(profile_image, (x, y))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_round_wins(player_rounds, x, y):
    for i in range(player_rounds):
        pygame.draw.circle(screen, colors["GOLD"], (x + i * 20, y), 10)





#Muss überarbeitet werden
# Menü-Logik
def main_menu():
    button_image_paths = [
        'Buttons/Start/Start1.png',
        'Buttons/Start/Start2.png',
        'Buttons/Start/Start3.png',
        'Buttons/Start/Start4.png',
        'Buttons/Start/Start5.png'
    ]
    animated_button = AnimatedButton(button_image_paths, SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 37, 150, 75)
    menu_running = True
    while menu_running:
        dt = clock.tick(FPS) / 1000
        screen.fill(colors["BLACK"])
        animated_button.update(dt)
        animated_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if animated_button.is_clicked(event.pos):
                    return True

        pygame.display.update()

# Hauptspiel
def main_game(selected_character):
    fighter_1 = Champion(1, 200, 310, animations_zuko, dragon_slayer_fx if selected_character == "Zuko" else katana_fx)
    fighter_2 = Champion(2, 700, 310, animations_susanoo, katana_fx if selected_character == "Zuko" else dragon_slayer_fx)

    game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return None

        draw_bg()
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)
        draw_mana_bar(fighter_1.mana, 80, 65)
        draw_mana_bar(fighter_2.mana, 618, 65)
        draw_text("ZUKO", fonts["name_font"], colors["RED"], 80, 80)
        draw_text("SUSANOO", fonts["name_font"], colors["BLUE"], 817, 80)
        draw_fighter_profilepicture(zuko_pb, 20, 64)
        draw_fighter_profilepicture(susanoo_pb, 930, 64)
        game_logic.update_countdown()
        game_logic.check_round_status()
        game_logic.draw_round_wins()

        if game_logic.intro_count <= 0:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)
            fighter_1.update()
            fighter_2.update()

        fighter_1.draw(screen)
        fighter_2.draw(screen)
        game_logic.ermittle_winner()
        pygame.display.update()

# Hauptprogramm
if __name__ == "__main__":
    running = True
    game_state = "menu"
    selected_character = None
    while running:
        if game_state == "menu":
            result = main_menu()
            if result is None:
                running = False
            elif result:
                game_state = "character_select"
        elif game_state == "character_select":
            select_screen = CharacterSelectScreen(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
            selected_character = select_screen.run()
            if selected_character:
                game_state = "running"
            else:
                running = False
        elif game_state == "running":
            result = main_game(selected_character)
            if result is None:
                running = False
            else:
                game_state = "menu"

    pygame.quit()
