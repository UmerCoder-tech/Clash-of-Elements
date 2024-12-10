
import pygame
from pygame import mixer
from game_manager import GameManager
from buttons import AnimatedButton
from spritesheets import animations_zuko, animations_susanoo, animations_basim, animations_mai
from champion import Champion
from gamestate import GameLogic
from selectscreen import CharacterSelectScreen
from ui_manager import UIManager
from endscreen import EndScreen

# Initialisiere Pygame
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
}

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

# Hintergrund
bg_image = pygame.image.load("Hintergrund/Fate's Moon.png")
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Soundeffekte
dragon_slayer_fx = pygame.mixer.Sound("Audio/assets_audio_magic.wav")
dragon_slayer_fx.set_volume(0.5)
katana__fx = pygame.mixer.Sound("Audio/assets_audio_sword.wav")
katana__fx.set_volume(0.5)

# UI-Manager und Endbildschirm
ui_manager = UIManager(screen, fonts, colors, draw_text)
end_screen = EndScreen(screen, fonts, colors)


def main_game(selected_characters):
    print(f"Spiel gestartet mit: {selected_characters}")
    
    # Charakterdaten
    characters = {
        "Zuko": {
            "animations": animations_zuko,
            "sound": dragon_slayer_fx,
            "attributes": {
                "name": "Zuko",
                "profile_picture": "path/to/zuko_profile.png"
            }
        },
        "Susanoo": {
            "animations": animations_susanoo,
            "sound": katana__fx,
            "attributes": {
                "name": "Susanoo",
                "profile_picture": "path/to/susanoo_profile.png"
            }
        },
        "Basim": {
            "animations": animations_basim,
            "sound": dragon_slayer_fx,
            "attributes": {
                "name": "Basim",
                "profile_picture": "path/to/basim_profile.png"
            }
        },
        "Mai": {
            "animations": animations_mai,
            "sound": katana__fx,
            "attributes": {
                "name": "Mai",
                "profile_picture": "path/to/mai_profile.png"
            }
        },
    }

    # Erstelle Champion-Objekte für beide Spieler
    fighter_1_data = characters[selected_characters[0]]
    fighter_2_data = characters[selected_characters[1]]

    fighter_1 = Champion(
        1,  # Spieler 1 ID
        200,  # X-Position
        310,  # Y-Position
        fighter_1_data["animations"],
        fighter_1_data["sound"],
        fighter_1_data["attributes"]["name"]
    )

    fighter_2 = Champion(
        2,  # Spieler 2 ID
        700,  # X-Position
        310,  # Y-Position
        fighter_2_data["animations"],
        fighter_2_data["sound"],
        fighter_2_data["attributes"]["name"]
    )

    # Spiel-Logik initialisieren
    game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)

    # Gewinner-Logik zurücksetzen
    winner_detected = False
    winner_detected_time = None
    winner_display_time = 3000  # 3 Sekunden

    run = True
    while run:
        clock.tick(FPS)

        # Ereignisse verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_manager.running = False
                return None

        # Gewinnerprüfung
        if not winner_detected:
            winner = game_logic.ermittle_winner(end_screen)
            if winner:
                winner_detected = True
                winner_detected_time = pygame.time.get_ticks()

        # Hintergrund zeichnen
        draw_bg()

        # Bewegung und Aktualisierung der Spieler, falls Countdown beendet ist
        if not winner_detected and game_logic.intro_count <= 0:
            fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_2)
            fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, fighter_1)

        fighter_1.update()
        fighter_2.update()

        # Spieler zeichnen
        fighter_1.draw(screen)
        fighter_2.draw(screen)

        # UI aktualisieren
        ui_manager.draw_health_bar(fighter_1.health, 20, 20)
        ui_manager.draw_health_bar(fighter_2.health, 580, 20)
        ui_manager.draw_champion_profilepicture(selected_characters[0], 20, 60)
        ui_manager.draw_champion_profilepicture(selected_characters[1], 930, 60)
        ui_manager.draw_mana_bar(fighter_1.mana, 80, 65)
        ui_manager.draw_mana_bar(fighter_2.mana, 618, 65)

        # Namen der Spieler anzeigen
        draw_text(fighter_1_data["attributes"]["name"], fonts["name_font"], colors["WHITE"], 80, 80)
        draw_text(fighter_2_data["attributes"]["name"], fonts["name_font"], colors["WHITE"], 817, 80)

        # Spiel-Logik aktualisieren
        if not winner_detected:
            game_logic.update_countdown()
            game_logic.update_timer()
            game_logic.check_berserker_phase()
            game_logic.update_fighter_berserker_state()
            game_logic.display_berserker_message()
            game_logic.check_round_status()
            game_logic.draw_round_wins()

        # Gewinneranzeige
        if winner_detected:
            current_time = pygame.time.get_ticks()

            # Gewinnertext vorbereiten
            winner_text = f"{end_screen.winner} WINS!"
            rendered_text = fonts["winner_font"].render(winner_text, True, colors["GOLD"])

            # Gewinnertext mittig positionieren
            text_width = rendered_text.get_width()
            text_height = rendered_text.get_height()
            x = (SCREEN_WIDTH - text_width) // 2
            y = (SCREEN_HEIGHT - text_height) // 2

            # Gewinnertext anzeigen
            screen.blit(rendered_text, (x, y))

            # Prüfe, ob die Anzeigezeit vorbei ist
            if winner_detected_time and current_time - winner_detected_time > winner_display_time:
                return "end_screen"

        pygame.display.update()

    #return None  // nochmal nachschauen





# Hauptprogramm
if __name__ == "__main__":
    game_manager = GameManager(screen, fonts, colors)
    
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
                    game_manager.running = False
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if animated_button.is_clicked(event.pos):
                        return True

            pygame.display.update()

    game_manager.run_main_menu(main_menu)

    while game_manager.running:
        if game_manager.game_state == "menu":
            game_manager.run_main_menu(main_menu)
        elif game_manager.game_state == "character_select":
            game_manager.run_character_select()
        elif game_manager.game_state == "running":
            result = main_game(game_manager.selected_character)
            if result == "end_screen":
                game_manager.game_state = "end_screen"
        elif game_manager.game_state == "end_screen":
            restart = end_screen.run()  # Zeige Endscreen an
            if restart == "restart":
                game_manager.game_state = "menu"  # Zurück ins Hauptmenü





    pygame.quit()
    exit()

