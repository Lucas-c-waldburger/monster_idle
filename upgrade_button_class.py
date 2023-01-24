import tkinter as tk


class UpgradeButton:
    def __init__(self, parent_frame, column, row, stats, upgrade_params):

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

        stats.blood_bank_string.trace('w', check_if_can_afford)

        def upgrade_button_command():
            """perform all functions associated with buying upgrade"""

            # updates necessary stat variable using eval() of 'update' string in self.parameters
            eval(self.parameters[self.level]['update'] +
                 "(operation=self.parameters[self.level]['operation'], value=self.parameters[self.level]['value'])")

            # subtract cost from blood bank
            stats.update_blood_bank(
                operation='-',
                value=self.parameters[self.level]['cost'])

            # proceed to next level in self.parameters and configure widgets with this data
            self.level = next(self.level_iter)
            self.button.config(image=self.parameters[self.level]['image'])
            self.tooltip_label.config(text=self.parameters[self.level]['text'])
            self.cost_label.config(text=self.parameters[self.level]['cost'])

        self.button.config(command=upgrade_button_command)