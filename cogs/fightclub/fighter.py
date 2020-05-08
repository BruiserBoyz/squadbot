class Fighter:
    def __init__(self):
        self.health = 50.0
        self.strength = 50.0
        self.stamina = 50.0
        self.agility = 50.0
        self.player = ""
        self.weapon = ""

    def set_health(self, health_change):
        self.health += health_change
        return True

    def get_health(self):
        return self.health

    def set_strength(self, strength_change):
        self.strength += strength_change
        return True

    def get_strength(self):
        return self.strength

    def set_stamina(self, stamina_change):
        self.stamina += stamina_change
        return True

    def get_stamina(self):
        return self.stamina

    def set_agility(self, agility_change):
        self.agility += agility_change
        return True

    def get_agility(self):
        return self.agility

    def set_player(self, player):
        self.player = player
        return True

    def get_player(self):
        return self.player

    def set_weapon(self, weapon):
        self.weapon = weapon
        return True

    def get_weapon(self):
        return self.weapon
