import tkinter as tk
import operator

operations_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
#TO DO------------ #
# 1. change var labels to text drawn on self.canvas

class Stats():
    """Contains all stats affecting damage, monster health, lanes traveled, etc inside a frame. Handles all updates to
    stats via upgrades, modifiers and game progress. """
    def __init__(self, frame, saved_data_dict_stats):

        self.data = saved_data_dict_stats

        self.canvas = tk.Canvas(frame, width=100, height=600)
        self.canvas.grid(column=0, row=0)

        # stat variables
        self.blood_bank_var = self.data['blood bank']
        self.damage_per_hit_var = self.data['damage per hit']
        self.total_damage_dealt_var = self.data['total damage dealt']
        self.attack_interval_var = self.data['attack interval']
        self.horizontal_attack_span_var = self.data['horizontal attack span']
        self.monster_health_var = self.data['monster health']
        self.monsters_killed_var = self.data['monsters killed']
        self.lanes_traveled_var = self.data['lanes traveled']


        # stat string vars for display on labels
        self.blood_bank_string = tk.StringVar()
        self.damage_per_hit_string = tk.StringVar()
        self.total_damage_dealt_string = tk.StringVar()
        self.attack_interval_string = tk.StringVar()
        self.horizontal_attack_span_string = tk.StringVar()
        self.monsters_killed_string = tk.StringVar()
        self.lanes_traveled_string = tk.StringVar()


        # self.canvas.create_text(100, 100, text=f"Damage per hit: {self.damage_per_hit_var}")

        # Int/Double vars on labels
        self.blood_bank_label = tk.Label(self.canvas, textvariable=self.blood_bank_string).grid(column=1, row=0, pady=40)
        self.damage_per_hit_label = tk.Label(self.canvas, textvariable=self.damage_per_hit_string).grid(column=1, row=1)
        self.total_damage_dealt_label = tk.Label(self.canvas, textvariable=self.total_damage_dealt_string).grid(column=1, row=2)
        self.attack_interval_label = tk.Label(self.canvas, textvariable=self.attack_interval_string).grid(column=1, row=3)
        self.horizontal_attack_span_label = tk.Label(self.canvas, textvariable=self.horizontal_attack_span_string).grid(column=1, row=4)
        self.monsters_killed_label = tk.Label(self.canvas, textvariable=self.monsters_killed_string).grid(column=1, row=5)
        self.lanes_traveled_label = tk.Label(self.canvas, textvariable=self.lanes_traveled_string).grid(column=1, row=6)

        self.update_all()

    def update_blood_bank(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.blood_bank_var = perform_operation(self.blood_bank_var, value)
        self.blood_bank_string.set(f"Blood bank: {self.blood_bank_var} mL")

    def update_damage_per_hit(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.damage_per_hit_var = perform_operation(self.damage_per_hit_var, value)
        self.damage_per_hit_string.set(f"Damage per hit: {self.damage_per_hit_var}")

    def update_total_damage_dealt(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.total_damage_dealt_var = perform_operation(self.total_damage_dealt_var, value)
        self.total_damage_dealt_string.set(f"Total damage dealt: {self.total_damage_dealt_var}")

    def update_attack_interval(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.attack_interval_var = perform_operation(self.attack_interval_var, value)
        self.attack_interval_string.set(f"One attack every {self.attack_interval_var} seconds")

    def update_horizontal_attack_span(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.horizontal_attack_span_var = perform_operation(self.horizontal_attack_span_var, value)

        if self.horizontal_attack_span_var == 1:
            self.horizontal_attack_span_string.set(f"Your horizontal attack spans {self.horizontal_attack_span_var} cell")
        else:
            self.horizontal_attack_span_string.set(
                f"Your horizontal attack spans {self.horizontal_attack_span_var} cells")

    def update_monsters_killed(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.monsters_killed_var = perform_operation(self.monsters_killed_var, value)
        self.monsters_killed_string.set(f"Monsters killed: {self.monsters_killed_var}")

    def update_lanes_traveled(self, **kwargs):
        if kwargs.get('operation') is not None:
            perform_operation = operations_dict[kwargs['operation']]
            value = kwargs['value']
            self.lanes_traveled_var = perform_operation(self.lanes_traveled_var, value)
        self.lanes_traveled_string.set(f"Lanes traveled: {self.lanes_traveled_var}")



    def update_all(self):
        self.update_blood_bank()
        self.update_damage_per_hit()
        self.update_total_damage_dealt()
        self.update_attack_interval()
        self.update_horizontal_attack_span()
        self.update_monsters_killed()
        self.update_lanes_traveled()