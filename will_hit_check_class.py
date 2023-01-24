class WillHitCheck:
    def __init__(self, player, monster, stats):

        self.player = player
        self.monster = monster
        self.stats = stats
        self.horizontal_attack_will_hit = None


    def will_horizontal_attack_hit(self):
        if self.player.current_row == self.monster.current_row:
            for n in range(0, self.stats.horizontal_attack_span_var + 1):
                self.calculate_horizontal_attacks(n)
                if self.horizontal_attack_will_hit:
                    return True

    def calculate_horizontal_attacks(self, n):
        if self.player.current_column == self.monster.current_column + n or \
                self.player.current_column == self.monster.current_column - n:
            self.horizontal_attack_will_hit = True
        else:
            self.horizontal_attack_will_hit = False
        return self.horizontal_attack_will_hit

    # def will_horizontal_attack_hit(self):
    #     print(f'current player row = {self.player.current_row}')
    #     print(f'current monster row = {self.monster.current_row}')
    #     if self.player.current_row == self.monster.current_row:
    #         for n in range(0, self.stats.horizontal_attack_span_var + 1):
    #             print(f'current horizontal attack span = {self.stats.horizontal_attack_span_var}')
    #             print(f'current player column = {self.player.current_column}')
    #             print(f'current monster column = {self.monster.current_column}')
    #             print(f'n = {n}')
    #             print(f'monster column + n = {self.monster.current_column + n}')
    #             if self.player.current_column == self.monster.current_column + n or \
    #                     self.player.current_column == self.monster.current_column - n:
    #                 self.horizontal_attack_will_hit = True
    #             else:
    #                 self.horizontal_attack_will_hit = False
    #             print(f'will horizontal attack hit = {self.horizontal_attack_will_hit}')
    #     return self.horizontal_attack_will_hit

