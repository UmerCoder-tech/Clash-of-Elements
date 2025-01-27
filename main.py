
import pygame
from pygame import mixer
from game_manager import GameManager
from buttons import Button
from spritesheets import animations_zuko, animations_susanoo, animations_basim, animations_mai
from champion import Champion
from gamelogic import GameLogic
from ui_manager import UIManager
from endscreen import EndScreen
from character_data import characters
from ressource import fonts,colors,maps
from button_manager import ButtonManager


# Initialisiere Pygame
pygame.init()
mixer.init()

# Bildschirmgröße und Framerate
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
FPS = 60

#Hauptost

main_theme = pygame.mixer.music.load("Audio/menu_musik.mp3")
pygame.mixer.music.set_volume(0.4) #lautstärke einstellen
pygame.mixer.music.play(-1, 0.0, 5000)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)  
    screen.blit(img, (x, y))  

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


def draw_selected_map():
    if game_manager.selected_map:
        bg_image = game_manager.maps[game_manager.selected_map]["image"]
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))




# UI-Manager und Endbildschirm,Gamemanager
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
        draw_selected_map()

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
        ui_manager.draw_player_names(fighter_1_data, fighter_2_data)

    

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


        game_manager = GameManager(screen, fonts, colors, maps)

        #Hintergrund wird über den Buttonmanager aufgerufen
        button_manager = ButtonManager(
            screen, 
            fonts, 
            colors, 
            bg_image_path="Hintergrund/menu_picture.png"  # Pfad zu deinem Hintergrundbild
        )

        # Buttons erstellen
        button_manager.create_buttons(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Buttons abrufen
        buttons = button_manager.get_buttons()
        start_button = buttons["start"]
        quit_button = buttons["quit"]

        
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
                    elif quit_button.is_clicked(event.pos):
                        pygame.quit()
                        exit()

            
            quit_button.draw(screen)
            button_manager.draw_buttons()

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


