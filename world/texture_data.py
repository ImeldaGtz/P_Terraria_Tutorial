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
        'filepath': 'res/player.png', 
        'size': (TILESIZE*4, TILESIZE*4)
        },
    'zombie_static': {
        'type': 'enemy',
        'filepath': 'res/zombie.png', 
        'size': (TILESIZE*4, TILESIZE*4)
        },
    'shortsword': {
        'type': 'weapon',
        'filepath': 'res/shortsword.png',
        'size': (TILESIZE, TILESIZE)
        }
}