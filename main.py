import tkinter as tk
from master_cell_dict import master_cell_dict, master_column_dict
from player_class import Character
from move_button_class import MoveButton
from stats_class import Stats
from upgrade_button_class import UpgradeButton
import json
from random import choice
from will_hit_check_class import WillHitCheck

# TO DO
# # condense left face/right face sprite dicts into one dict with left/right as nested dicts
# # Keep fleshing out will hit check class
# # create a way to randomize stage layouts
# # decide on starting upgrades, add all to a list and put it in NEW_GAME_DATA_DICT
    # # then figure out how to save it and pull it back out
# # Add new environment sprite type:
    # # add it to photoimage dict to allow it to spawn maybe?
# # find way to load current upgrade levels in a saved game
# #

# -----------GLOBALS-------------- #
# Placement
PLAYER_STARTING_CELL = 'c3xr3'

# Attack Loop
DAMAGE_TEXT_SPAWN_FRAME = 6

# Colors
GRASS_GREEN_COLOR = '#76a37a'

# Starting data dict if no saved data
NEW_GAME_DATA_DICT = {
    'stat data': {
        'blood bank': 0.0,
        'damage per hit': 2.0,
        'total damage dealt': 0.0,
        'attack interval': 1.50,
        'horizontal attack span': 1,
        'monster health': 80.0,
        'monsters killed': 0,
        'lanes traveled': 0,
    },
    'location data': {
        'player cell': PLAYER_STARTING_CELL,
        'monster cells': [],
        'env layout': {}
    },
}


# ------------ROOT TK------------- #
root = tk.Tk()
root.geometry('1050x600')
root.resizable(False, False)


# -----------PHOTOIMAGE DICTS--------- #
player_sprite_left_face_dict = {
    'sp_1': tk.PhotoImage(file='./sprite/sprite_1.png'),
    'sp_2': tk.PhotoImage(file='./sprite/sprite_2.png'),
    'sp_3': tk.PhotoImage(file='./sprite/sprite_3.png'),
    'sp_4': tk.PhotoImage(file='./sprite/sprite_4.png'),
    'sp_5': tk.PhotoImage(file='./sprite/sprite_5.png'),
    'sp_6': tk.PhotoImage(file='./sprite/sprite_6.png'),
    'sp_7': tk.PhotoImage(file='./sprite/sprite_7.png'),
    'sp_8': tk.PhotoImage(file='./sprite/sprite_8.png'),
    'sp_9': tk.PhotoImage(file='./sprite/sprite_9.png'),
    'sp_10': tk.PhotoImage(file='./sprite/sprite_10.png'),
    'sp_11': tk.PhotoImage(file='./sprite/sprite_11.png')
}
player_sprite_right_face_dict = {
    'sp_1': tk.PhotoImage(file='./player_sprite_face_right/sprite_1_face_right.png'),
    'sp_2': tk.PhotoImage(file='./player_sprite_face_right/sprite_2_face_right.png'),
    'sp_3': tk.PhotoImage(file='./player_sprite_face_right/sprite_3_face_right.png'),
    'sp_4': tk.PhotoImage(file='./player_sprite_face_right/sprite_4_face_right.png'),
    'sp_5': tk.PhotoImage(file='./player_sprite_face_right/sprite_5_face_right.png'),
    'sp_6': tk.PhotoImage(file='./player_sprite_face_right/sprite_6_face_right.png'),
    'sp_7': tk.PhotoImage(file='./player_sprite_face_right/sprite_7_face_right.png'),
    'sp_8': tk.PhotoImage(file='./player_sprite_face_right/sprite_8_face_right.png'),
    'sp_9': tk.PhotoImage(file='./player_sprite_face_right/sprite_9_face_right.png'),
    'sp_10': tk.PhotoImage(file='./player_sprite_face_right/sprite_10_face_right.png'),
    'sp_11': tk.PhotoImage(file='./player_sprite_face_right/sprite_11_face_right.png'),
}

monster_sprite_dict = {
    'monster_1': {
        'normal': {'sprite_1': tk.PhotoImage(file='./monster_sprite/monster_1_sprite.png')},
        'red': {'sprite_1': tk.PhotoImage(file='./monster_sprite/monster_1_sprite_red.png')}
    }
}

env_sprite_dict = {
    # 'grass_image': tk.PhotoImage(file='./env_assets/grass_with_path.png'),
    'grass_full': tk.PhotoImage(file='./env_assets/grass_full_2.png'),
    'grass_with_tree': tk.PhotoImage(file='./env_assets/grass_with_tree.png'),
    # 'grave_short': tk.PhotoImage(file='./env_assets/grave_short.png')
}

upgrade_sprite_dict = {
    'damage per hit 1': tk.PhotoImage(file='./upgrade_assets/SteelMelee.png'),
    'damage per hit 2': tk.PhotoImage(file='./upgrade_assets/MeleeDamage.png'),
    'blood drop': tk.PhotoImage(file='./upgrade_assets/blood_drop_1.png'),
    'blood drop small': tk.PhotoImage(file='./upgrade_assets/blood_drop_1_small.png'),
    'long blade 1': tk.PhotoImage(file='./upgrade_assets/PierceDamage.png')
}

# -----------ENVIRONMENT TYPE DATA--------- #
# env_type_data_dict = {
#     'grass': {
#         'image': {
#             'name': 'grass_full',
#             'photoimage': tk.PhotoImage(file='./env_assets/grass_full_2.png')
#         },
#         'type': 'neutral'
#     },
#     'tree': {
#         'image': {
#             'name': 'grass_with_tree',
#             'photoimage': tk.PhotoImage(file='./env_assets/grass_with_tree.png')
#         },
#         'type': 'wood'
#     }
# }

# ------------LOADING SAVED DATA------------- #
try:
    with open('stat_data.json', 'r') as data_file:
        saved_data_json = json.load(data_file)
        saved_data_dict = saved_data_json

except FileNotFoundError:
    saved_data_dict = NEW_GAME_DATA_DICT


# ------------MAIN CANVAS------------- #
main_canvas = tk.Canvas(width=600, height=600, bg=GRASS_GREEN_COLOR)
main_canvas.grid(column=1, row=0, padx=5)

# ------------ENV LAYOUT------------- #
def choose_random_env_sprite():
    chosen_env = choice(list(env_sprite_dict.keys()))
    return chosen_env

# generates random env images on tiles if new game
if saved_data_dict['location data']['env layout'] == {}:
    saved_data_dict['location data']['env layout'] = {key: choose_random_env_sprite() for key in master_cell_dict.keys()}


def draw_tiles_on_canvas():
    for entry in master_cell_dict:
        # if master_cell_dict[entry]['column'] == 0:
        #     column_tag = 'column_0'
        # elif master_cell_dict[entry]['column'] == 1:
        #     column_tag = 'column_1'
        # elif master_cell_dict[entry]['column'] == 2:
        #     column_tag = 'column_2'
        # elif master_cell_dict[entry]['column'] == 3:
        #     column_tag = 'column_3'
        # elif master_cell_dict[entry]['column'] == 4:
        #     column_tag = 'column_4'
        # elif master_cell_dict[entry]['column'] == 5:
        #     column_tag = 'column_5'

        main_canvas.create_image(master_cell_dict[entry]['xy'][0],
                                 master_cell_dict[entry]['xy'][1],
                                 image=env_sprite_dict[saved_data_dict['location data']['env layout'][entry]],
                                 # tags=column_tag,
                                 anchor='nw',
                                 )


draw_tiles_on_canvas()

# ------------------FRAMES------------------- #
upgrade_frame = tk.Frame(height=600, width=100, borderwidth=0, highlightthickness=0)
upgrade_frame.grid(column=2, row=0)

stats_frame = tk.Frame(height=600, width=100, borderwidth=0, highlightthickness=0)
stats_frame.grid(column=0, row=0)



# -----------------STATS--------------- #
stats = Stats(frame=stats_frame, saved_data_dict_stats=saved_data_dict['stat data'])


# ---------------UPGRADES--------------- #
upgrade_parameter_dict = {
    'plus damage per hit': {
        'level 1': {
            'image': upgrade_sprite_dict['damage per hit 1'],
            'text': '+1 damage per hit',
            'cost': 10,
            'operation': '+',
            'value': 1,
            'update': "stats.update_damage_per_hit"
        },
        'level 2': {
            'image': upgrade_sprite_dict['damage per hit 2'],
            'text': '+2 damage per hit',
            'cost': 50,
            'operation': '+',
            'value': 2,
            'update': "stats.update_damage_per_hit"
        }
    },
    'plus horizontal attack span': {
        'level 1': {
            'image': upgrade_sprite_dict['long blade 1'],
            'text': 'horizontal attack  \nspans +1 more cell',
            'cost': 200,
            'operation': '+',
            'value': 1,
            'update': "stats.update_horizontal_attack_span"
        },
        'level 2': {
            'image': upgrade_sprite_dict['long blade 1'],
            'text': 'horizontal attack  \nspans +1 more cell',
            'cost': 600,
            'operation': '+',
            'value': 1,
            'update': "stats.update_horizontal_attack_span"
        },
    }
}

upgrades_for_purchase_list = []

damage_per_hit_upgrade = UpgradeButton(parent_frame=upgrade_frame,
                                       column=1, row=1,
                                       stats=stats,
                                       upgrade_params=upgrade_parameter_dict['plus damage per hit']
                                       )
upgrades_for_purchase_list.append(damage_per_hit_upgrade)

horizontal_attack_span_upgrade = UpgradeButton(parent_frame=upgrade_frame,
                                               column=1, row=2,
                                               stats=stats,
                                               upgrade_params=upgrade_parameter_dict['plus horizontal attack span']
                                               )
upgrades_for_purchase_list.append(horizontal_attack_span_upgrade)

# ---------------PLAYER---------------- #

player = Character(canvas=main_canvas,
                   cell_dict=master_cell_dict,
                   left_face_sprite_dict=player_sprite_left_face_dict,
                   right_face_sprite_dict=player_sprite_right_face_dict,
                   starting_cell=saved_data_dict['location data']['player cell'],
                   stats=stats
                   )

# --------------MONSTERS--------------- #
active_monster_list = []


def choose_random_monster():
    monster_sprite_dict_key_list = [k for k in monster_sprite_dict]
    chosen_monster = choice(monster_sprite_dict_key_list)
    return chosen_monster


def choose_random_start_cell():
    occupied_cell_coords = [monster.current_cell_xy for monster in active_monster_list]
    occupied_cell_coords.append(player.current_cell_xy)

    choose_again = True
    while choose_again:
        monster_start_cell = choice([k for k in master_cell_dict.keys()])
        if master_cell_dict[monster_start_cell]['xy'] not in occupied_cell_coords:
            choose_again = False
    return monster_start_cell


def summon_monster(**list_interaction):
    chosen_monster = choose_random_monster()
    try:
        monster_start_cell = saved_data_dict['location data']['monster cells'].pop(0)
    except:
        monster_start_cell = choose_random_start_cell()
    monster = Character(canvas=main_canvas,
                        cell_dict=master_column_dict,
                        left_face_sprite_dict=monster_sprite_dict[chosen_monster]['normal'],
                        right_face_sprite_dict=monster_sprite_dict[chosen_monster]['red'],
                        starting_cell=monster_start_cell,
                        stats=stats,
                        type='monster')
    if list_interaction.get('list_interaction') == 'replace':
        return monster
    else:
        active_monster_list.append(monster)


# ------------MOVE BUTTONS------------- #


master_move_button_dict = {
    'column 0': {
        'button_r0': MoveButton(main_canvas, column=master_column_dict['xy_column_0'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c0xr0'),
        'button_r1': MoveButton(main_canvas, column=master_column_dict['xy_column_0'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c0xr1'),
        'button_r2': MoveButton(main_canvas, column=master_column_dict['xy_column_0'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c0xr2'),
        'button_r3': MoveButton(main_canvas, column=master_column_dict['xy_column_0'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c0xr3'),
        'button_r4': MoveButton(main_canvas, column=master_column_dict['xy_column_0'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c0xr4'),
        'button_r5': MoveButton(main_canvas, column=master_column_dict['xy_column_0'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c0xr5'),
    },
    'column 1': {
        'button_r0': MoveButton(main_canvas, column=master_column_dict['xy_column_1'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c1xr0'),
        'button_r1': MoveButton(main_canvas, column=master_column_dict['xy_column_1'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c1xr1'),
        'button_r2': MoveButton(main_canvas, column=master_column_dict['xy_column_1'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c1xr2'),
        'button_r3': MoveButton(main_canvas, column=master_column_dict['xy_column_1'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c1xr3'),
        'button_r4': MoveButton(main_canvas, column=master_column_dict['xy_column_1'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c1xr4'),
        'button_r5': MoveButton(main_canvas, column=master_column_dict['xy_column_1'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c1xr5'),
    },
    'column 2': {
        'button_r0': MoveButton(main_canvas, column=master_column_dict['xy_column_2'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c2xr0'),
        'button_r1': MoveButton(main_canvas, column=master_column_dict['xy_column_2'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c2xr1'),
        'button_r2': MoveButton(main_canvas, column=master_column_dict['xy_column_2'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c2xr2'),
        'button_r3': MoveButton(main_canvas, column=master_column_dict['xy_column_2'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c2xr3'),
        'button_r4': MoveButton(main_canvas, column=master_column_dict['xy_column_2'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c2xr4'),
        'button_r5': MoveButton(main_canvas, column=master_column_dict['xy_column_2'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c2xr5'),
    },
    'column 3': {
        'button_r0': MoveButton(main_canvas, column=master_column_dict['xy_column_3'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c3xr0'),
        'button_r1': MoveButton(main_canvas, column=master_column_dict['xy_column_3'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c3xr1'),
        'button_r2': MoveButton(main_canvas, column=master_column_dict['xy_column_3'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c3xr2'),
        'button_r3': MoveButton(main_canvas, column=master_column_dict['xy_column_3'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c3xr3'),
        'button_r4': MoveButton(main_canvas, column=master_column_dict['xy_column_3'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c3xr4'),
        'button_r5': MoveButton(main_canvas, column=master_column_dict['xy_column_3'],
                                img=env_sprite_dict['grass_full'],
                                player=player, stats=stats, cell='c3xr5'),
    },
    'column 4': {
        'button_r0': MoveButton(main_canvas, column=master_column_dict['xy_column_4'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c4xr0'),
        'button_r1': MoveButton(main_canvas, column=master_column_dict['xy_column_4'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c4xr1'),
        'button_r2': MoveButton(main_canvas, column=master_column_dict['xy_column_4'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c4xr2'),
        'button_r3': MoveButton(main_canvas, column=master_column_dict['xy_column_4'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c4xr3'),
        'button_r4': MoveButton(main_canvas, column=master_column_dict['xy_column_4'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c4xr4'),
        'button_r5': MoveButton(main_canvas, column=master_column_dict['xy_column_4'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c4xr5'),
    },
    'column 5': {
        'button_r0': MoveButton(main_canvas, column=master_column_dict['xy_column_5'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c5xr0'),
        'button_r1': MoveButton(main_canvas, column=master_column_dict['xy_column_5'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c5xr1'),
        'button_r2': MoveButton(main_canvas, column=master_column_dict['xy_column_5'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c5xr2'),
        'button_r3': MoveButton(main_canvas, column=master_column_dict['xy_column_5'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c5xr3'),
        'button_r4': MoveButton(main_canvas, column=master_column_dict['xy_column_5'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c5xr4'),
        'button_r5': MoveButton(main_canvas, column=master_column_dict['xy_column_5'],
                                img=env_sprite_dict['grass_with_tree'], player=player, stats=stats, cell='c5xr5'),
    }
}


def place_move_buttons():
    active_monster_xy_list = [monster.current_cell_xy for monster in active_monster_list]
    for column in master_move_button_dict:
        for row in master_move_button_dict[column]:
            button = master_move_button_dict[column][row]

            button.change_env_image(img=env_sprite_dict[saved_data_dict['location data']['env layout'][button.cell]])

            x = button.cell_xy[0]
            y = button.cell_xy[1]
            if button.cell_xy != player.current_cell_xy and button.cell_xy not in active_monster_xy_list:
                button.button.place(x=x, y=y)
                button.state = 'active'
            else:
                button.button.place_forget()
                button.state = 'hidden'


place_move_buttons()


# ----------ADDING IN NEW COLUMNS---------- #
# def add_forest_column():
#     main_canvas.delete('column_4')
#     for entry in master_cell_dict:
#         if master_cell_dict[entry]['column'] == 4:
#             main_canvas.create_image(master_cell_dict[entry]['xy'][0],
#                                      master_cell_dict[entry]['xy'][1],
#                                      image=env_sprite_dict['grass_with_tree'],
#                                      anchor='nw',
#                                      tags='column_4')
#     main_canvas.tag_lower('column_4', player.sprite_label)
#

# ----------SAVING DATA-------------- #
def update_stat_data_for_save():
    var_list = []
    for var in vars(stats):
        if var.split('_')[-1] == 'var':
            var_list.append(vars(stats)[var])

    var_list_iter = iter(var_list)
    for k in stats.data:
        stats.data[k] = next(var_list_iter)

    return stats.data


def update_player_location_data_for_save():
    current_player_cell = [cell for cell in master_cell_dict.keys() if master_cell_dict[cell]['xy'] == player.current_cell_xy][0]
    return current_player_cell


def update_monster_location_data_for_save():
    current_monster_coords = [monster.current_cell_xy for monster in active_monster_list]
    current_monster_cells = [cell for cell in master_cell_dict.keys() if master_cell_dict[cell]['xy'] in current_monster_coords]
    return current_monster_cells



print(saved_data_dict['location data']['env layout'])


def save_and_quit():
    saved_data_dict['stat data'] = update_stat_data_for_save()
    saved_data_dict['location data']['player cell'] = update_player_location_data_for_save()
    saved_data_dict['location data']['monster cells'] = update_monster_location_data_for_save()

    with open('stat_data.json', 'w') as file:
        json.dump(saved_data_dict, file, indent=4)

    root.destroy()


# -----------MENU BUTTONS------------ #
save_quit_button = tk.Button(stats.canvas, text='Save and Quit', command=save_and_quit)
save_quit_button.grid(column=1, row=7, pady=100)


# ---------PLAYER ATTACK LOOP--------- #

def player_attack_loop():
    """tk after function - check and perform functions during each player attack frame"""
    # iters through sprite images to animate player
    main_canvas.itemconfigure(player.sprite_label,
                              image=player.current_face_sprite_dict[player.sprite_key_list[player.animation_frame]])

    for monster in active_monster_list:
        # checks if player hits any active monster
        hit_check = WillHitCheck(player=player, monster=monster, stats=stats)
        if hit_check.will_horizontal_attack_hit():
            monster.damage.flip_player_to_face_damage(player=player)

            # if player hits, creates damage instance and updates blood bank/total damage stats
            if player.animation_frame == DAMAGE_TEXT_SPAWN_FRAME:
                monster.flip_character_sprite()
                monster.damage.deal_damage(root, main_canvas, stats.damage_per_hit_var)

                stats.update_blood_bank(operation='+', value=stats.damage_per_hit_var)
                stats.update_total_damage_dealt(operation='+', value=stats.damage_per_hit_var)

            if monster.damage.health_value_current <= 0:
                monster.forget(canvas=main_canvas)
                monster_in_list = active_monster_list.index(monster)
                monster = summon_monster(list_interaction='replace')
                active_monster_list[monster_in_list] = monster

                stats.update_monsters_killed(operation='+', value=1)

    if player.animation_frame >= 10:
        player.animation_frame = 0

    else:
        player.animation_frame += 1

    # All the checks and updates

    # # # # # # INSERT THINGS THAT TRIGGER ON MONSTERS KILLED # # # # # #

    # re-place move buttons
    place_move_buttons()

    root.after(player.animation_frame_change_speed, player_attack_loop)


# -----------------PROGRAM---------------- #
# if len(active_monster_list) == 0:
#     summon_monster()
summon_monster()
summon_monster()



player_attack_loop()

root.mainloop()