# import tkinter as tk
from tkinter import ttk
# from master_cell_dict import master_cell_dict, master_column_dict

DMG_TXT_X_OFFSET = 60
DMG_TXT_Y_OFFSET = 30
HEALTHBAR_X_OFFSET = 25
HEALTHBAR_Y_OFFSET = 80
STARTING_FONT_SIZE = 20


GRASS_GREEN_COLOR = '#76a37a'




class Damage:
    def __init__(self, canvas, monster, stats):

        # Damage Text
        self.damage_value = stats.damage_per_hit_var
        self.health_value_max = stats.monster_health_var
        self.health_value_current = stats.monster_health_var

        self.monster = monster
        self.monster_parent_cell = self.monster.current_cell_xy

        self.damage_text_x = self.monster.current_cell_xy[0] + DMG_TXT_X_OFFSET
        self.damage_text_y = self.monster.current_cell_xy[1] + DMG_TXT_Y_OFFSET
        self.damage_text_distance_scrolled = 0
        self.damage_text = canvas.create_text(self.monster.current_cell_xy, text='', )
        self.damage_text_font_size = 20

        # Health Bar
        self.healthbar_x = self.monster.current_cell_xy[0] + HEALTHBAR_X_OFFSET
        self.healthbar_y = self.monster.current_cell_xy[1] + HEALTHBAR_Y_OFFSET

        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", background='red', foreground='red', thickness=10)
        self.healthbar_progressbar = ttk.Progressbar(canvas,
                                                     style="red.Horizontal.TProgressbar",
                                                     orient="horizontal",
                                                     mode="determinate",
                                                     length=50)
        self.healthbar_progressbar['value'] = 110
        self.healthbar_progressbar.place(x=self.healthbar_x, y=self.healthbar_y)

    def scroll_damage_text(self, root, canvas):
        self.change_to_red_sprite(canvas)
        canvas.itemconfig(self.damage_text, text=self.damage_value, font=('Arial', self.damage_text_font_size, 'bold'))
        canvas.coords(self.damage_text, self.damage_text_x, self.damage_text_y)
        self.damage_text_y -= 5
        self.damage_text_distance_scrolled += 5
        self.damage_text_font_size -= 5

        if self.damage_text_distance_scrolled >= 25:
            root.after_cancel(self.scroll_damage_text)
            self.change_to_normal_sprite(canvas)
            canvas.itemconfig(self.damage_text, text='')
            self.damage_text_x = self.monster.current_cell_xy[0] + DMG_TXT_X_OFFSET
            self.damage_text_y = self.monster.current_cell_xy[1] + DMG_TXT_Y_OFFSET
            self.damage_text_distance_scrolled = 0
            self.damage_text_font_size = STARTING_FONT_SIZE

        else:
            root.after(80, self.scroll_damage_text, root, canvas)

    def health_percent_decrease(self):
        damage_value_as_percent = (self.damage_value * 100) / self.health_value_max
        return damage_value_as_percent

    def reduce_health(self):
        """reduces health value and the visual on the healthbar"""
        self.healthbar_progressbar["value"] -= self.health_percent_decrease()
        self.health_value_current -= self.damage_value

    def deal_damage(self, root, canvas, damage_per_hit_var):
        self.damage_value = damage_per_hit_var
        self.scroll_damage_text(root, canvas)
        self.reduce_health()

    def flip_player_to_face_damage(self, player): # FIX TO TAKE IN CURRENT_ROW/CURRENT_COLUMN VARIABLES!!
        if player.current_cell_xy[0] < self.monster.current_cell_xy[0] and player.current_face_sprite_dict == player.left_face_sprite_dict:
            player.flip_character_sprite()
        elif player.current_cell_xy[0] > self.monster.current_cell_xy[0] and player.current_face_sprite_dict == player.right_face_sprite_dict:
            player.flip_character_sprite()

    def change_to_normal_sprite(self, canvas):
        canvas.itemconfig(self.monster.sprite_label, image=self.monster.left_face_sprite_dict['sprite_1'])

    def change_to_red_sprite(self, canvas):
        canvas.itemconfig(self.monster.sprite_label, image=self.monster.right_face_sprite_dict['sprite_1'])