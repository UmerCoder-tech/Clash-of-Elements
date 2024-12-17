import pygame
from pygame import mixer
mixer.init()
# Animationen und Sounds müssen von anderen Modulen bereitgestellt werden
from spritesheets import animations_zuko, animations_susanoo, animations_basim, animations_mai #lädt die animationen aus der spritesheets datei

# Charakterdaten dictionary
characters = {
    "Zuko": {
        "animations": animations_zuko,
        "sound":pygame.mixer.Sound( "Audio/FeuerritterSOUND.mp3"),
        "attributes": {
            "name": "Zuko",
            "profil_bild": "Zuko/zuko_pb.png",
        },
    },
    "Susanoo": {
        "animations": animations_susanoo,
        "sound":pygame.mixer.Sound( "Audio/WasserfrauSOUND.mp3"),
        "attributes": {
            "name": "Susanoo",
            "profil_bild": "Susanoo/susanoo_pb.png",
        },
    },
    "Basim": {
        "animations": animations_basim,
        "sound":pygame.mixer.Sound("Audio/FeuerritterSOUND.mp3"),
        "attributes": {
            "name": "Basim",
            "profil_bild": "Basim/basim_pb_.png",
        },
    },
    "Mai": {
        "animations": animations_mai,
        "sound":pygame.mixer.Sound("Audio/WasserfrauSOUND.mp3"),
        "attributes": {
            "name": "Mai",
            "profil_bild": "Mai/mai_pb.png",
        },
    },
}

# Vorladen von Profilbildern und Sounds
for char_name, char_data in characters.items():  #char_name enthält namen des chars #char_data ist das dict. mit den details des chars
    # Profilbild laden und skalieren
    char_data["loaded_profile_picture"] = pygame.transform.scale( #fügt das skalierte bild in das characters dict. hinzu
        pygame.image.load(char_data["attributes"]["profil_bild"]), (100, 100) #zieht sich das bild was in dem Pfad hinter prpfilbild gespeichert ist
    )
    # Sound laden
    #char_data["loaded_sound"] = pygame.mixer.Sound(char_data["sound"])
