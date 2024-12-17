
import pygame
from pygame import mixer
from game_manager import GameManager
from buttons import Button
from spritesheets import animations_zuko, animations_susanoo, animations_basim, animations_mai
from champion import Champion
from gamestate import GameLogic
#from selectscreen import CharacterSelectScreen
from ui_manager import UIManager
from endscreen import EndScreen
from character_data import characters
#from map_manager import MapSelectScreen


# Initialisiere Pygame
pygame.init()
mixer.init()

# Bildschirmgröße und Framerate
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

#Hauptost

main_theme = pygame.mixer.music.load("Audio/menu_musik.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)


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
            "offset_y": -120,
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

def draw_text(text, font, text_col, x, y):
    # text: Der anzuzeigende Text (String).
    # font: Das pygame.font.Font-Objekt, das den Schriftstil und die Größe definiert.
    # text_col: Die Farbe des Textes als RGB-Tupel, z. B. (255, 255, 255) für Weiß.
    # x, y: Die Koordinaten, an denen der Text auf dem Bildschirm gezeichnet wird.
    img = font.render(text, True, text_col)  # Render den Text als Bild (antialiasing=True, text_col für die Farbe).
    screen.blit(img, (x, y))  # Zeichne das Bild an die gewünschte Position auf dem Bildschirm.

# Ereignisse zentral behandeln
def handle_events():
    for event in pygame.event.get():  #behandelt die quitfunktion und beendet das spiel um jeden preis
        if event.type == pygame.QUIT:
            game_manager.running = False
            return False
    return True



# Fenster erstellen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clash of Elements")
clock = pygame.time.Clock()


def draw_bg():
    if game_manager.selected_map:
        bg_image = game_manager.maps[game_manager.selected_map]["image"]
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))


# Soundeffekte
dragon_slayer_fx = pygame.mixer.Sound("Audio/FeuerritterSOUND.mp3")
dragon_slayer_fx.set_volume(0.9) #0.5
katana__fx = pygame.mixer.Sound("Audio/WasserfrauSOUND.mp3")
katana__fx.set_volume(0.9) #0.5

# UI-Manager und Endbildschirm
ui_manager = UIManager(screen, fonts, colors, draw_text, maps)
game_manager = GameManager(screen, fonts, colors, maps)
end_screen = EndScreen(screen, fonts, colors,game_manager)


def main_game(selected_characters,selected_map):


    # Erstelle Champion-Objekte für beide Spieler
    fighter_1_data = characters[selected_characters[0]]
    fighter_2_data = characters[selected_characters[1]]

    map_data = maps[selected_map]

    fighter_1 = Champion(
        1,  # Spieler 1 ID
        200,  # X-Position
        310,  # Y-Position
        fighter_1_data["animations"],
        fighter_1_data["sound"],
        fighter_1_data["attributes"]["name"],
        map_data=map_data
    )

    fighter_2 = Champion(
        2,  # Spieler 2 ID
        700,  # X-Position
        310,  # Y-Position
        fighter_2_data["animations"],
        fighter_2_data["sound"],
        fighter_2_data["attributes"]["name"],
        map_data=map_data
    )


    
    

    

    # Spiel-Logik initialisieren und End-Bildschirm
    game_logic = GameLogic(fighter_1, fighter_2, fonts, colors, screen, draw_text)

    # Gewinner-Logik zurücksetzen
    winner_detected = False
    winner_detected_time = None
    winner_display_time = 3000  # 3 Sekunden

    run = True
    while run:
        clock.tick(FPS)

        if not handle_events():   #sorgt dafür das wenn das spiel unterbrochen wird durch fenster schließung das spiel auch wirklich geschlossen wird
            return None

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

    return None #hier endet main game




# Hauptprogramm
if __name__ == "__main__":



    game_manager = GameManager(screen, fonts, colors, maps)

    def main_menu():

        #game_manager.play_music("Audio/menu_musik.mp3")

        button_width = 200
        button_height = 80
        start_button_x = SCREEN_WIDTH // 2 - button_width // 2  # Zentriert
        start_button_y = SCREEN_HEIGHT // 2 - button_height - 40  # Oberhalb des Quit-Buttons
        quit_button_x = SCREEN_WIDTH // 2 - button_width // 2  # Zentriert
        quit_button_y = SCREEN_HEIGHT // 2 + 40  # Unterhalb des Start-Buttons


        # Start-Button erstellen
        start_button = Button(
            image_path="ButtonRed/pngegg.png",
            x=start_button_x,
            y=start_button_y,
            new_width=button_width,
            new_height=button_height,
            text="Start",
            font=fonts["button_font"],
            text_color=colors["WHITE"]
        )

    # Quit-Button erstellen
        quit_button = Button(
            image_path="ButtonRed/pngegg.png",
            x=quit_button_x,
            y=quit_button_y,
            new_width=button_width,
            new_height=button_height,
            text="Quit",
            font=fonts["button_font"],
            text_color=colors["WHITE"]
        )


    

        #animated_button = AnimatedButton(button_image_paths, SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 37, 150, 75)
        menu_running = True

        while menu_running:
            dt = clock.tick(FPS) / 1000
            screen.fill(colors["BLACK"])
            #animated_button.update(dt)
            start_button.draw(screen)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_manager.running = False
                    pygame.mixer.music.stop() #stoppt die hauptost
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.is_clicked(event.pos):
                        game_manager.game_state = "character_select"
                        #pygame.mixer.music.stop() #stoppt die hauptost
                        return True
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_manager.running = False
                    return #None
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Linksklick prüfen
                    if start_button.is_clicked(event.pos):
                        game_manager.game_state = "character_select"
                        menu_running = False  # Hauptmenü-Schleife verlassen

                    if quit_button.is_clicked(pygame.mouse.get_pos()):
                        pygame.quit()
                        exit()

            #pygame.display.update()
            # Buttons zeichnen
            #start_button.draw(screen)
            quit_button.draw(screen)

        # Bildschirm aktualisieren
            pygame.display.update()
            clock.tick(FPS)
    



# Stelle sicher, dass reset_game_state verfügbar ist


    game_manager.run_main_menu(main_menu)
    
    while game_manager.running:
        if game_manager.game_state == "menu":
            game_manager.run_main_menu(main_menu)
        elif game_manager.game_state == "character_select":
            game_manager.run_character_select()
        elif game_manager.game_state == "map_select":  # Hinzugefügt
            game_manager.run_map_select()
        elif game_manager.game_state == "running":
            result = main_game(game_manager.selected_character, game_manager.selected_map)
            if result == "end_screen":
                game_manager.game_state = "end_screen"
        elif game_manager.game_state == "end_screen":
            result = end_screen.run()  # Zeige Endscreen an
            if result == "restart":
                game_manager.game_state = "menu"  # Zurück ins Hauptmenü
            elif result == "replay":
                #game_manager.game_state = "running" #eben gespeilte runde wird neugestartet
                game_manager.stop_music()
                game_manager.play_music(game_manager.maps[game_manager.selected_map]["music"])
                
                game_manager.game_state = "running"
    

        
        if not handle_events():
            break



    pygame.quit()
    exit()


