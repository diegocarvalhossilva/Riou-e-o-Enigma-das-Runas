WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

#ui
HEALTH_BAR_HEIGHT = 20
ENERGY_BAR_HEIGHT = 14
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

#cores gerais
WATER_COLORS = '#71DDEE'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#cores ui
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#armas
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic':'../graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic':'../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic':'../graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic':'../graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic':'../graphics/weapons/sai/full.png'}
}

magic_data = {
    'flame':{'strength':5,'cost':20, 'graphic':'../graphics/particles/flame/fire.png'},
    'heal':{'strength':20,'cost':10, 'graphic':'../graphics/particles/heal/heal.png'}
}

monster_data = {
    'squid':{'health':100,'exp':100,'damage':20,'attack_type':'slash','attack_sound':'../audio/attack/slash.wav','speed':3,'resistance':3,'attack_radius':80,'notice_radius':360},
    'raccoon':{'health':80,'exp':100,'damage':10,'attack_type':'claw','attack_sound':'../audio/attack/claw.wav','speed':3,'resistance':3,'attack_radius':80,'notice_radius':350},
    'toad':{'health':90,'exp':110,'damage':10,'attack_type':'pound','attack_sound':'../audio/attack/claw.wav','speed':2,'resistance':4,'attack_radius':80,'notice_radius':350},
    'spirit':{'health':100,'exp':110,'damage':8,'attack_type':'thunder','attack_sound':'../audio/attack/fireball.wav','speed':3,'resistance':3,'attack_radius':60,'notice_radius':350},
    'bamboo':{'health':70,'exp':120,'damage':6,'attack_type':'leaf_attack','attack_sound':'../audio/attack/slash.wav','speed':3,'resistance':3,'attack_radius':50,'notice_radius':360},
    'toad_king':{'health':320,'exp':275,'damage':40,'attack_type':'pound','attack_sound':'../audio/attack/claw.wav','speed':4,'resistance':5,'attack_radius':120,'notice_radius':400}
}