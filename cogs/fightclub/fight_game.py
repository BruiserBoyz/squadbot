import random
class FightGame:
    def __init__(self):
        self.number_fighters = 0;
        self.fighters = []
        self.current_champ = ""
        self.fightprize = 500

    def set_num_fighters(self, increment):
        self.number_fighters += increment
        return True

    def get_num_fighters(self):
        return self.number_fighters

    def set_fighter(self, fighter):
        self.fighters.append(fighter)
        return True

    def get_fighter(self, fighter_index):
        return self.fighters[fighter_index]

    def get_all_fighters(self):
        return self.fighters

    def drop_fighter(self, fighter_index):
        self.fighters.pop(fighter_index)
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

    def set_fighter_weapon(self, weapon, fighter_name):
        # find the fighter
        fighter_index = 0;
        fighter_found = False
        while not fighter_found and fighter_index < self.number_fighters:
            for fighter in self.fighters:
                if fighter.get_player() == fighter_name:
                    fighter.set_weapon(weapon)
                    fighter_found = True
                else:
                    fighter_index +=1
        return fighter_found

    def set_all_weapons(self, weapon):
        for fighter in self.fighters:
            fighter.set_weapon(weapon)
        return True

    def fight_two(self):
        """ Fights the first two fighters in a three round brawl."""
        # check there are two fighters.
        if self.number_fighters < 2:
            return "not enough fighters"
        else:
            rtn_msg = ""
            f = [self.fighters[0], self.fighters[1]]

            # Check the fight can proceed
            stammed_out = False
            deathed_out = False
            for fighter in f:

                if fighter.get_stamina() < 30:
                    rtn_msg += f'{fighter.get_player()} is too weak and forfiets.\n'
                    stammed_out += 1

                if fighter.get_health() < 1:
                    rtn_msg += f'{fighter.get_player()} happens to be dead.\n'
                    deathed_out +=1

                if stammed_out >= 1 or deathed_out >=1:
                    return rtn_msg

            # otherwise let's have a fight.
            rando = random.randint(0,999999)
            if rando % 2:
                winner = f[0]
                loser = f[1]
            else:
                winner = f[1]
                loser = f[0]

            # fought harder, loses some stamina
            percent_dip = random.randint(0, 10) / 100
            winner.set_stamina(-(percent_dip * winner.get_stamina()))
            winner.set_strength(1)
            rtn_msg += f'{winner.get_player()} won this round with his {winner.get_weapon()}.\n'

            # fought harder, loses some stamina
            stam_dip = random.randint(0, 5) / 100
            health_dip = random.randint(0,100) / 100
            loser.set_stamina(-(stam_dip * loser.get_stamina()))
            loser.set_strength(-1)
            loser.set_health(-(health_dip * loser.get_health()))
            rtn_msg += f'{loser.get_player()} lost this round '
            if loser.get_health() > 1:
                rtn_msg += f'they are somehow still alive'
            else:
                rtn_msg += f'they are quite dead.\n'

            return rtn_msg