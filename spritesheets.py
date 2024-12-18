import pygame as pg

# Funktion zum Laden und Skalieren von Animationsframes
def load_animation_frames(base_path, frame_count, scale_factor=1):
    frames = []
    for i in range(1, frame_count + 1):  # Startet bei 1 und geht bis frame_count
        frame = pg.image.load(f"{base_path}_{i}.png")  # Lade das Bild
        # Skalierung anwenden
        scaled_frame = pg.transform.scale(
            frame,
            (int(frame.get_width() * scale_factor), int(frame.get_height() * scale_factor))
        )
        frames.append(scaled_frame)
    return frames

# Animationen laden und direkt skalieren
scale_factor = 3.5  # Passe dies an die gewünschte Größe an

animations_zuko = {
    "idle": load_animation_frames("Zuko/idle_frames/idle", 8, scale_factor),
    "run": load_animation_frames("Zuko/run_frames/run", 8, scale_factor),
    "jump": load_animation_frames("Zuko/jump_frames/jump", 20, scale_factor),
    "defend": load_animation_frames("Zuko/defend_frames/defend", 10, scale_factor),
    "atk1": load_animation_frames("Zuko/atk1_frames/air_atk", 8, scale_factor),
    "atk2": load_animation_frames("Zuko/atk2_frames/2_atk", 19, scale_factor),
    "atk3": load_animation_frames("Zuko/sp_atk_frames/sp_atk", 18, scale_factor),
    "take_hit": load_animation_frames("Zuko/take_hit_frames/take_hit", 6, scale_factor),
    "death": load_animation_frames("Zuko/death_frames/death", 13, scale_factor)
}

animations_susanoo = {
    "idle": load_animation_frames("Susanoo/idle_frames/idle", 10, scale_factor),
    "run": load_animation_frames("Susanoo/run_frames/run", 8, scale_factor),
    "jump": load_animation_frames("Susanoo/jump_frames/jump_full", 20, scale_factor),
    "defend": load_animation_frames("Susanoo/defend_frames/defend", 8, scale_factor),
    "atk1": load_animation_frames("Susanoo/atk1_frames/air_atk", 8, scale_factor),
    "atk2": load_animation_frames("Susanoo/atk2_frames/2_atk", 10, scale_factor),
    "atk3": load_animation_frames("Susanoo/sp_atk_frames/sp_atk", 20, scale_factor),
    "take_hit": load_animation_frames("Susanoo/take_hit_frames/take_hit", 6, scale_factor),
    "death": load_animation_frames("Susanoo/death_frames/death_uncen", 20, scale_factor)
}

animations_basim = {
    "idle": load_animation_frames("Basim/idle_frames/idle", 8, scale_factor),
    "run": load_animation_frames("Basim/run_frames/run", 8, scale_factor),
    "jump": load_animation_frames("Basim/jump_frames/j_up", 3, scale_factor),
    "defend": load_animation_frames("Basim/defend_frames/defend", 8, scale_factor),
    "atk1": load_animation_frames("Basim/air_atk_frames/air_atk", 7, scale_factor),
    "atk2": load_animation_frames("Basim/atk2_frames/2_atk", 18, scale_factor),
    "atk3": load_animation_frames("Basim/sp_atk_frames/sp_atk", 30, scale_factor),
    "take_hit": load_animation_frames("Basim/take_hit_frames/take_hit", 6, scale_factor),
    "death": load_animation_frames("Basim/death_frames/death", 19, scale_factor)
}

animations_mai = {
    "idle": load_animation_frames("Mai/idle_frames/idle",8, scale_factor),
    "atk1": load_animation_frames("Mai/1atk_frames/1_atk",7,scale_factor),
    "atk2": load_animation_frames("Mai/2atk_frames/2_atk",21,scale_factor),
    "atk3": load_animation_frames("Mai/3atk_frames/3_atk",27,scale_factor),
    "run":  load_animation_frames("Mai/walk_frames/walk",10,scale_factor),
    "jump": load_animation_frames("Mai/jump_frames/j_up",3,scale_factor),
    "defend": load_animation_frames("Mai/defend_frames/defend", 12, scale_factor),
    "take_hit": load_animation_frames("Mai/take_hit_frames/take_hit",7,scale_factor),
    "death": load_animation_frames("Mai/death_frames/death",16,scale_factor)
    
}

animations_rayna = {
    "idle": load_animation_frames("Rayna/idle_frames/01_idle",8, scale_factor),
    "atk1": load_animation_frames("Rayna/air_atk_frames/air_atk",8,scale_factor),
    "atk2": load_animation_frames("Rayna/2_atk_frames/08_2_atk",8,scale_factor),
    "atk3": load_animation_frames("Rayna/sp_atk_frames/10_sp_atk",11,scale_factor),
    "run":  load_animation_frames("Rayna/run_frames/02_run",8,scale_factor),
    "jump": load_animation_frames("Rayna/jump_full_frames/03_jump",20,scale_factor),
    "defend": load_animation_frames("Rayna/defend_frames/11_defend", 12, scale_factor),
    "take_hit": load_animation_frames("Rayna/take_hit_frames/12_take_hit",6,scale_factor),
    "death": load_animation_frames("Rayna/death_frames/13_death",12,scale_factor)
    
}

#Der tatsächliche scalefaktor wurde bei tenzin intern geändert da dieser Char eigenartig gezeichnet ist
animations_tenzin = {
    "idle": load_animation_frames("Tenzin/idle_frames/idle",6, 3.9),
    "atk1": load_animation_frames("Tenzin/air_atk_frames/air_atk",7, 3.9),
    "atk2": load_animation_frames("Tenzin/2_atk_frames/2_atk",12, 3.9),
    "atk3": load_animation_frames("Tenzin/sp_atk_frames/sp_atk",25, 3.9),
    "run":  load_animation_frames("Tenzin/run_frames/run",8, 3.9),
    "jump": load_animation_frames("Tenzin/j_up_frames/j_up",3, 3.9),
    "defend": load_animation_frames("Tenzin/defend_frames/defend", 13, 3.9),
    "take_hit": load_animation_frames("Tenzin/take_hit_frames/take_hit",6, 3.9),
    "death": load_animation_frames("Tenzin/death_frames/death",18, 3.9)

}



animations_thyrion = {
    "idle": load_animation_frames("Thyrion/idle/idle",8, scale_factor),
    "atk1": load_animation_frames("Thyrion/air_atk/air_atk",8,scale_factor),
    "atk2": load_animation_frames("Thyrion/2_atk/2_atk",7,scale_factor),
    "atk3": load_animation_frames("Thyrion/sp_atk/sp_atk",15,scale_factor),
    "run":  load_animation_frames("Thyrion/run/run",8,scale_factor),
    "jump": load_animation_frames("Thyrion/jump_full/jump_full",21,scale_factor),
    "defend": load_animation_frames("Thyrion/defend/defend", 9, scale_factor),
    "take_hit": load_animation_frames("Thyrion/take_hit/take_hit",6,scale_factor),
    "death": load_animation_frames("Thyrion/death/death",15,scale_factor)
}


animations_valeryon = {
    "idle": load_animation_frames("Valeryon/idle/idle",12, scale_factor),
    "atk1": load_animation_frames("Valeryon/air_atk/air_atk",10,scale_factor),
    "atk2": load_animation_frames("Valeryon/2_atk/2_atk",15,scale_factor),
    "atk3": load_animation_frames("Valeryon/sp_atk/sp_atk",17,scale_factor),
    "run":  load_animation_frames("Valeryon/run/run",10,scale_factor),
    "jump": load_animation_frames("Valeryon/jump_full/jump",22,scale_factor),
    "defend": load_animation_frames("Valeryon/defend/defend", 19, scale_factor),
    "take_hit": load_animation_frames("Valeryon/take_hit/take_hit",6,scale_factor),
    "death": load_animation_frames("Valeryon/death/death",19,scale_factor)
}



