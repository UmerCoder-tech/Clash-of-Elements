import pygame
from pygame import mixer
mixer.init()
# Animationen und Sounds müssen von anderen Modulen bereitgestellt werden
from spritesheets import animations_zuko, animations_susanoo, animations_basim, animations_mai,animations_rayna,animations_tenzin,animations_thyrion,animations_valeryon #lädt die animationen aus der spritesheets datei

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
        "sound":pygame.mixer.Sound( "Audio/SamuraiSOUND.mp3"),
        "attributes": {
            "name": "Susanoo",
            "profil_bild": "Susanoo/susanoo_pb.png",
        },
    },
    "Basim": {
        "animations": animations_basim,
        "sound":pygame.mixer.Sound("Audio/doubleknife.mp3"),
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
    "Rayna": {
        "animations": animations_rayna,
        "sound":pygame.mixer.Sound("Audio/doubleknife.mp3"), #vielleicht wasser
        "attributes": {
            "name": "Rayna",
            "profil_bild": "Rayna/rayna_pb.png",
        },
    },

    "Tenzin": {
        "animations": animations_tenzin,
        "sound":pygame.mixer.Sound("Audio/fist.mp3"),
        "attributes": {
            "name": "Tenzin",
            "profil_bild": "Tenzin/tenzin_pb.png",
        },
    },

    "Thyrion": {
        "animations": animations_thyrion,
        "sound":pygame.mixer.Sound("Audio/HammerSOUND.wav"),
        "attributes": {
            "name": "Thyrion",
            "profil_bild": "Thyrion/thyrion_pb.png",
        },
    },

    "Valeryon": {
        "animations": animations_valeryon,
        "sound":pygame.mixer.Sound("Audio/ValyrionSOUND2.wav"),
        "attributes": {
            "name": "Valeryon",
            "profil_bild": "Valeryon/valeryon_pb.png",
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
