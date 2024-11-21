import pygame
from pygame import mixer


# Initialisiere Pygame
pygame.init()
mixer.init()

main_theme = pygame.mixer.music.load("Audio/Ryus Ost.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

dragon_slayer_fx = pygame.mixer.Sound("Audio/assets_audio_magic.wav")
dragon_slayer_fx.set_volume(0.5)
katana__fx = pygame.mixer.Sound("Audio/assets_audio_sword.wav")
katana__fx.set_volume(0.5)

# Bildschirmgröße und Framerate
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

# Farben

colors = {
    "LILA": (128, 0, 128),
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "MIDNIGHT_BLUE": (25, 25, 112),  # RGB für Mitternachtsblau
    "SILBER": (192, 192, 192),
    "GOLD": (255, 215, 0),
    "DUNKEL_GRÜN": (0, 100, 0),
    "RED": (255, 0, 0),
    "BLUE":(0, 0, 255)
}




#define fonts
fonts = {
    "count_font": pygame.font.Font("Fonts/Orbitron.ttf", 180),
    "score_font": pygame.font.Font("Fonts/Orbitron.ttf", 30),
    "ready_attack_font": pygame.font.Font("Fonts/Oswald.ttf", 16),
    "name_font": pygame.font.Font("Fonts/Oswald.ttf", 28),
    "fight_font": pygame.font.Font("Fonts/Oswald.ttf", 300),
    "berserk_front": pygame.font.Font("Fonts/MetalMania.ttf", 30),
    "winner_font": pygame.font.Font("Fonts/Oswald.ttf", 150),
}


#define game variables 
intro_count = 4
last_count_update = pygame.time.get_ticks()     #muss ins loop






def draw_text(text, font, text_col, x, y):
    # text: Der anzuzeigende Text (String).
    # font: Das pygame.font.Font-Objekt, das den Schriftstil und die Größe definiert.
    # text_col: Die Farbe des Textes als RGB-Tupel, z. B. (255, 255, 255) für Weiß.
    # x, y: Die Koordinaten, an denen der Text auf dem Bildschirm gezeichnet wird.

    img = font.render(text, True, text_col)  # Render den Text als Bild (antialiasing=True, text_col für die Farbe).
    screen.blit(img, (x, y))  # Zeichne das Bild an die gewünschte Position auf dem Bildschirm.



# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Fighting Game")
clock = pygame.time.Clock()

# Jetzt die Spritesheets importieren
from spritesheets import animations_zuko, animations_susanoo
from testfighter import Fighter
from gamestate import GameLogic

# Hintergrundbild laden
bg_image = pygame.image.load("Hintergrund/Fate's Moon.png")

# Spieler erstellen
fighter_1 = Fighter(1, 200, 310, animations_zuko, dragon_slayer_fx)  # Spieler 1
fighter_2 = Fighter(2, 700, 310, animations_susanoo, katana__fx)  # Spieler 2

# Initialisierung der Spiel-Logik
game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)







# Profilbilder laden
susanoo_pb = pygame.image.load("Susanoo/susanoo_pb.png")
zuko_pb = pygame.image.load("Zuko/zuko_pb.png")

# Funktion zum Zeichnen des Hintergrunds
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Funktion zum Zeichnen der Lebensbalken
def draw_health_bar(health, x, y):
    hb_width = 400
    hb_height = 30
    ratio = health / 100
    pygame.draw.rect(screen, colors["BLACK"], (x - 2, y - 2, hb_width + 4, hb_height + 4))  # Rahmen
    pygame.draw.rect(screen, colors["WHITE"], (x, y, hb_width, hb_height))  # Hintergrund
    pygame.draw.rect(screen, colors["LILA"], (x, y, hb_width * ratio, hb_height))  # Lebensbalken

def draw_mana_bar(mana, x, y):
    mb_width = 300
    mb_height = 20
    ratio = mana / 100
    pygame.draw.rect(screen, colors["BLACK"], (x - 2, y - 2, mb_width + 4, mb_height + 4))  # Rahmen
    pygame.draw.rect(screen, colors["WHITE"], (x, y, mb_width, mb_height))  # Hintergrund
    pygame.draw.rect(screen, colors["MIDNIGHT_BLUE"], (x, y, mb_width * ratio, mb_height))  # Manabalken

    if mana >= 100:
        text_img = fonts["ready_attack_font"].render("Critical Attack Ready!", True, colors["WHITE"])
        text_rect = text_img.get_rect(center=(x + mb_width // 2, y + mb_height // 2))       #chatgpt
        screen.blit(text_img, text_rect)




# Funktion zum Zeichnen der Profilbilder
def draw_fighter_profilepicture(profile_image, x, y):
    frame_width, frame_height = 54, 54
    profile_width, profile_height = 50, 50
    pygame.draw.rect(screen, colors["BLACK"], (x - 2, y - 2, frame_width, frame_height))  # Rahmen
    profile_image = pygame.transform.scale(profile_image, (profile_width, profile_height))
    screen.blit(profile_image, (x, y))

def draw_round_wins(player_rounds, x, y):
    for i in range(player_rounds):
        pygame.draw.circle(screen, colors["GOLD"], (x + i * 20, y), 10)





    
    



round_over = False
round_cooldown = 3000  # 2 Sekunden Cooldown
round_start_time = None
game_over_cooldown = 2000  # Cooldown in Millisekunden (2 Sekunden)




# Hauptspiel-Schleife
run = True
while run:
    clock.tick(FPS)

    # Ereignisse abfragen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Hintergrund zeichnen
    draw_bg()

    # Lebensbalken zeichnen
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #Manabalken
    draw_mana_bar(fighter_1.mana, 80, 65)
    draw_mana_bar(fighter_2.mana, 618, 65)

    #namen der spieler
    draw_text("ZUKO",fonts["name_font"], colors["RED"], 80, 80)
    draw_text("SUSANOO",fonts["name_font"], colors["BLUE"], 817, 80)



    # Profilbilder zeichnen
    draw_fighter_profilepicture(zuko_pb, 20, 64)  # Zuko
    draw_fighter_profilepicture(susanoo_pb, 930, 64)  # Susanoo

    # Countdown aktualisieren
    game_logic.update_countdown()

    # Runde prüfen
    game_logic.check_round_status()

    # Rundengewinne zeichnen
    game_logic.draw_round_wins()

    # Spieler-Updates und Zeichnen
    if game_logic.intro_count <= 0:
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)
        fighter_1.update()
        fighter_2.update()

            

    fighter_1.update()
    fighter_2.update()

    # Spieler zeichnen
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    game_logic.ermittle_winner()
           

    # Bildschirm aktualisieren
    pygame.display.update()

# Pygame beenden
pygame.quit()

