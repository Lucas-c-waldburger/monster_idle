import tkinter as tk

class MoveButton:
    def __init__(self, canvas, column, img, player, stats, cell, **type):

        self.cell = cell
        self.cell_xy = column[cell]

        self.button_parameters = {
            'height': 97,
            'width': 97,
            'image': img,
            'bd': 0,
            'highlightthickness': 0,
            'relief': 'flat'
        }

        self.button = tk.Button(canvas, **self.button_parameters)

        def move_player_to_button_effects():
            player.move_character_sprite(canvas, cell)
            stats.update_lanes_traveled(operation='+', value=1)
        # # # # # # INSERT THINGS THAT TRIGGER ON LANES TRAVELED # # # # # #

        self.button.config(command=move_player_to_button_effects)

        self.state = 'hidden'

    def change_env_image(self, img):
        self.button.config(image=img)