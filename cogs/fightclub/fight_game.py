class FightGame:
    def __init__(self):
        self.fighter = []
        self.current_champ = ""
        self.fightprize = 500

    def set_fighter(self, fighter):
        self.fighter.append(fighter)
        return True

    def get_fighter(self, fighter_index):
        return self.fighter[fighter_index]

    def get_all_fighters(self):
        return self.fighter

    def drop_fighter(self, fighter_index):
        self.fighter.pop(fighter_index)
        return True

    def set_current_champ(self, new_champ):
        self.current_champ = new_champ
        return True

    def get_current_champ(self):
        return self.current_champ

    def set_fight_prize(self, new_prize):
        self.fightprize += new_prize

    def get_fight_prize(self):
        return self.fightprize
