import pygame
from pygame import mixer
from buttons import AnimatedButton
from spritesheets import animations_zuko, animations_susanoo, animations_basim, animations_mai
from champion import Champion
from gamestate import GameLogic
from selectscreen import CharacterSelectScreen
from ui_manager import UIManager

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
    "score_font": pygame.font.Font("Fonts/Orbitron.ttf", 100),
    "ready_attack_font": pygame.font.Font("Fonts/Oswald.ttf", 16),
    "name_font": pygame.font.Font("Fonts/Oswald.ttf", 28),
    "fight_font": pygame.font.Font("Fonts/Oswald.ttf", 300),
    "berserk_front": pygame.font.Font("Fonts/MetalMania.ttf", 120),
    "winner_font": pygame.font.Font("Fonts/Oswald.ttf", 150),
}


def draw_text(text, font, text_col, x, y):
    # text: Der anzuzeigende Text (String).
    # font: Das pygame.font.Font-Objekt, das den Schriftstil und die Größe definiert.
    # text_col: Die Farbe des Textes als RGB-Tupel, z. B. (255, 255, 255) für Weiß.
    # x, y: Die Koordinaten, an denen der Text auf dem Bildschirm gezeichnet wird.

    img = font.render(text, True, text_col)  # Render den Text als Bild (antialiasing=True, text_col für die Farbe).
    screen.blit(img, (x, y))  # Zeichne das Bild an die gewünschte Position auf dem Bildschirm.

bg_image = pygame.image.load("Hintergrund/Fate's Moon.png")
# Funktion zum Zeichnen
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))


# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Fighting Game")
clock = pygame.time.Clock()

# Jetzt die Spritesheets importieren
#from spritesheets import animations_zuko, animations_susanoo
#from testfighter import Fighter
#from gamestate import GameLogic
#from ui_manager import UIManager



# Spieler erstellen
fighter_1 = Champion(1, 200, 310, animations_zuko, dragon_slayer_fx)  # Spieler 1
fighter_2 = Champion(2, 700, 310, animations_susanoo, katana__fx)  # Spieler 2

# Initialisierung der Spiel-Logik
game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)
ui_manager = UIManager(screen, fonts, colors, draw_text)




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










#Es muss noch die das main_game mit dem intigrierten select menü in die Hauptschleife intigriert werden




"""""
def main_game(selected_character):
# Hauptspiel-Schleife
    fighter_1 = Champion(1, 200, 310, animations_zuko, dragon_slayer_fx if selected_character == "Zuko" else katana__fx)
    fighter_2 = Champion(2, 700, 310, animations_susanoo, katana__fx if selected_character == "Zuko" else dragon_slayer_fx)

    game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)

    run = True
    while run:
        clock.tick(FPS)

    # Ereignisse abfragen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_bg()

        ui_manager.draw_bg()
        ui_manager.draw_fighter_profilepicture(1, 20, 64)  # Spieler 1 (Zuko)
        ui_manager.draw_fighter_profilepicture(2, 930, 64)  # Spieler 2 (Susanoo)



        # Lebensbalken zeichnen
        ui_manager.draw_health_bar(fighter_1.health, 20, 20)
        ui_manager.draw_health_bar(fighter_2.health, 580, 20)
    


        #Manabalken
        ui_manager.draw_mana_bar(fighter_1.mana, 80, 65)
        ui_manager.draw_mana_bar(fighter_2.mana, 618, 65)

        #namen der spieler
        draw_text("ZUKO",fonts["name_font"], colors["RED"], 80, 80)
        draw_text("SUSANOO",fonts["name_font"], colors["BLUE"], 817, 80)


    

        # Countdown aktualisieren
        game_logic.update_countdown()

        # Timer aktualisieren und anzeigen (startet erst nach Countdown)
        game_logic.update_timer()

        game_logic.check_berserker_phase()
        game_logic.update_fighter_berserker_state()

        # Berserker-Nachricht anzeigen
        game_logic.display_berserker_message()

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

        game_logic.update_timer()
        pygame.display.update()
    return None
"""


def main_game(selected_characters):
    print(f"Spiel gestartet mit: {selected_characters}")  # Debugging
    
    # Positionen auf dem Bildschirm
    left_position = (200, 310)
    right_position = (700, 310)
    
    # Charakter-Animationen basierend auf der Auswahl
    animations = {
        "Zuko": animations_zuko,
        "Susanoo": animations_susanoo,
        "Basim": animations_basim,
        "Mai": animations_mai
    }

    # Soundeffekte für die Charaktere (optional)
    sounds = {
        "Zuko": dragon_slayer_fx,
        "Susanoo": katana__fx,
        "Basim": dragon_slayer_fx,  # Beispiel
        "Mai": katana__fx,          # Beispiel
    }

    # Charaktere initialisieren
    fighter_1 = Champion(1, left_position[0], left_position[1], animations[selected_characters[0]], sounds[selected_characters[0]])
    fighter_2 = Champion(2, right_position[0], right_position[1], animations[selected_characters[1]], sounds[selected_characters[1]])
    # Spiel-Logik initialisieren
    game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)

    run = True
    while run:
        clock.tick(FPS)

        # Ereignisse verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Hintergrund zeichnen
        draw_bg()

        ui_manager.draw_bg()
        ui_manager.draw_champion_profilepicture(1, 20, 64)  # Spieler 1 (Zuko)
        ui_manager.draw_champion_profilepicture(2, 930, 64)  # Spieler 2 (Susanoo)



        # Lebensbalken zeichnen
        ui_manager.draw_health_bar(fighter_1.health, 20, 20)
        ui_manager.draw_health_bar(fighter_2.health, 580, 20)

        ui_manager.draw_champion_profilepicture(selected_characters[0], 20, 60)  # Links
        ui_manager.draw_champion_profilepicture(selected_characters[1], 930, 60)  # Rechts

        #Manabalken
        ui_manager.draw_mana_bar(fighter_1.mana, 80, 65)
        ui_manager.draw_mana_bar(fighter_2.mana, 618, 65)

        #namen der spieler
        ui_manager.draw_champion_name(selected_characters[0], 20, 60)  # Name links
        ui_manager.draw_champion_name(selected_characters[1], 580, 60)  # Name rechts

    

        # Countdown aktualisieren
        game_logic.update_countdown()

        # Timer aktualisieren und anzeigen (startet erst nach Countdown)
        game_logic.update_timer()

        game_logic.check_berserker_phase()
        game_logic.update_fighter_berserker_state()

        # Berserker-Nachricht anzeigen
        game_logic.display_berserker_message()

        # Runde prüfen
        game_logic.check_round_status()

        # Rundengewinne zeichnen
        game_logic.draw_round_wins()

        # Spieler zeichnen und aktualisieren
        if game_logic.intro_count <= 0:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)
            fighter_1.update()
            fighter_2.update()

        fighter_1.draw(screen)
        fighter_2.draw(screen)

        game_logic.ermittle_winner()

        # Spiel-Logik aktualisieren
        game_logic.update_countdown()
        game_logic.check_round_status()
        game_logic.draw_round_wins()

        pygame.display.update()

    return None



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
    pygame.display.update()

pygame.quit()
exit()




