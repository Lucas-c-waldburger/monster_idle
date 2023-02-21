import tkinter as tk


class UpgradeButton:
    def __init__(self, parent_frame, column, row, stats, upgrade_params, name):

        self.name = name

        self.frame = tk.Frame(parent_frame, height=100, width=100)
        self.frame.grid(column=column, row=row, sticky='w')

        self.parameters = upgrade_params

        self.level_iter = iter(upgrade_params)
        self.level = next(self.level_iter)

        self.button = tk.Button(self.frame, image=self.parameters[self.level]['image'], state='disabled',
                                relief='sunken')
        self.button.grid(column=0, row=0, rowspan=2)

        self.tooltip_label = tk.Label(self.frame, text=self.parameters[self.level]['text'])
        self.tooltip_label.grid(column=1, row=0, columnspan=2)

        self.blood_image = tk.PhotoImage(file='./upgrade_assets/blood_drop_1_small.png')
        self.blood_img_label = tk.Label(self.frame, image=self.blood_image)
        self.blood_img_label.grid(column=1, row=1, sticky='w')

        self.cost_label = tk.Label(self.frame, text=self.parameters[self.level]['cost'], fg='red')
        self.cost_label.grid(column=1, row=1)

        def check_if_can_afford(var, index, mode):
            """change button/cost label appearance if player can afford it"""
            if stats.blood_bank_var >= self.parameters[self.level]['cost']:
                self.button.config(state='active', relief='raised')
                self.cost_label.config(fg='green')
            else:
                self.button.config(state='disabled', relief='sunken')
                self.cost_label.config(fg='red')

        self.trace_afford = stats.blood_bank_string.trace_add('write', check_if_can_afford)

        def upgrade_button_command():
            """perform all functions associated with buying upgrades"""

            # updates necessary stat variable using eval() of 'update' string in self.parameters
            eval(self.parameters[self.level]['update'] +
                 "(operation=self.parameters[self.level]['operation'], value=self.parameters[self.level]['value'])")

            # subtract cost from blood bank
            stats.update_blood_bank(
                operation='-',
                value=self.parameters[self.level]['cost'])

            # attempt to proceed to next level in self.parameters and configure widgets with this data
            try:
                self.level = next(self.level_iter)
            except StopIteration:
                self.button.config(state='disabled', relief='sunken')
                self.cost_label.config(text="MAXED OUT", font="italic", fg="grey")
                self.blood_img_label.config(image="")
                stats.blood_bank_string.trace_remove('write', self.trace_afford)
            else:
                self.button.config(image=self.parameters[self.level]['image'])
                self.tooltip_label.config(text=self.parameters[self.level]['text'])
                self.cost_label.config(text=self.parameters[self.level]['cost'])

        self.button.config(command=upgrade_button_command)


class UpgradeParams:
    def __init__(self, sprites):

        self.sprite_dict = sprites

        self.upgrade_parameter_dict = {
            'plus damage per hit': {
                'level 1': {
                    'image': self.sprite_dict['damage per hit 1'],
                    'text': '+1 damage per hit',
                    'cost': 10,
                    'operation': '+',
                    'value': 1,
                    'update': "stats.update_damage_per_hit"
                },
                'level 2': {
                    'image': self.sprite_dict['damage per hit 2'],
                    'text': '+2 damage per hit',
                    'cost': 50,
                    'operation': '+',
                    'value': 2,
                    'update': "stats.update_damage_per_hit"
                },
                'level 3': {
                    'image': self.sprite_dict['damage per hit 3'],
                    'text': '+3 damage per hit',
                    'cost': 100,
                    'operation': '+',
                    'value': 3,
                    'update': "stats.update_damage_per_hit"
                }
            },
            'plus horizontal attack span': {
                'level 1': {
                    'image': self.sprite_dict['long blade 1'],
                    'text': 'horizontal attack  \nspans +1 more cell',
                    'cost': 200,
                    'operation': '+',
                    'value': 1,
                    'update': "stats.update_horizontal_attack_span"
                },
                'level 2': {
                    'image': self.sprite_dict['long blade 1'],
                    'text': 'horizontal attack  \nspans +1 more cell',
                    'cost': 600,
                    'operation': '+',
                    'value': 1,
                    'update': "stats.update_horizontal_attack_span"
                },
            }
        }




    def set_upgrade_level(self, upgrade_name: str, current_level: str):
        add_to_upgrade_dict = False
        upgrade_parameters_starting_from_level = dict()
        for key, val in self.upgrade_parameter_dict[upgrade_name].items():
            if key == current_level or add_to_upgrade_dict:
                add_to_upgrade_dict = True
                upgrade_parameters_starting_from_level[key] = val
        return upgrade_parameters_starting_from_level


