from globals import *

atlas_texture_data = {
    'grass': {
        'type': 'block',
        'size': (TILESIZE, TILESIZE),
        'position': (0, 0)
    },
    'dirt': {
        'type': 'block',
        'size': (TILESIZE, TILESIZE),
        'position': (0, 1)
    },
    'stone': {
        'type': 'block',
        'size': (TILESIZE, TILESIZE),
        'position': (1, 0)
    }

}

solo_texture_data = {
    'player_static': {
        'type': 'player',
        'filepath': 'res/Terraria_Guide.png', 
        'size': (TILESIZE, TILESIZE)
        }
}