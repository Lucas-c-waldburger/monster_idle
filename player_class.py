from damage_class import Damage
from master_cell_dict import master_cell_dict

# ------------GLOBALS------------- #
GRASS_GREEN_COLOR = '#76a37a'
PLAYER_STARTING_CELL = 'c3xr3'
MONSTER_STARTING_CELL = 'c2xr3'


class Character:
    def __init__(self, canvas, left_face_sprite_dict, right_face_sprite_dict, starting_cell, stats, **type):
        self.type = type.get("type")

        self.left_face_sprite_dict = left_face_sprite_dict
        self.right_face_sprite_dict = right_face_sprite_dict

        self.current_face_sprite_dict = left_face_sprite_dict
        self.sprite_key_list = [k for k in self.current_face_sprite_dict.keys()]

        self.current_cell_xy = None
        self.current_column = None
        self.current_row = None

        self.animation_frame = 0
        self.animation_frame_change_speed = round(stats.attack_interval_var / 11 * 1000) # MAKE FUNCTION TO CONVERT BACK INTO SECONDS WHEN UPLOADING SAVE DATA

        self.sprite_label = None
        self.create_character_sprite(canvas=canvas, starting_cell=starting_cell)

        if self.type == 'monster':
            self.damage = Damage( monster=self, canvas=canvas, stats=stats)


    def update_current_cell(self, new_cell):
        """update location-related attributes"""
        self.current_cell_xy = master_cell_dict[new_cell]['xy']
        self.current_column = master_cell_dict[new_cell]['column']
        self.current_row = master_cell_dict[new_cell]['row']

    def move_character_sprite(self, canvas, new_cell):
        self.update_current_cell(new_cell)
        canvas.moveto(self.sprite_label, x=self.current_cell_xy[0], y=self.current_cell_xy[1])

    def create_character_sprite(self, canvas, starting_cell):
        """assign character_sprite_assets image and location during initialization"""
        self.sprite_label = canvas.create_image(
            master_cell_dict[starting_cell]['xy'],
            image=self.current_face_sprite_dict[self.sprite_key_list[self.animation_frame]],
            anchor='nw')
        self.update_current_cell(starting_cell)

    def forget(self, canvas):
        """erase sprites/damage if monster is killed"""
        canvas.delete(self.sprite_label)
        self.damage.healthbar_progressbar.destroy()


    def flip_character_sprite(self):
        if self.current_face_sprite_dict == self.left_face_sprite_dict:
            self.current_face_sprite_dict = self.right_face_sprite_dict
        else:
            self.current_face_sprite_dict = self.left_face_sprite_dict