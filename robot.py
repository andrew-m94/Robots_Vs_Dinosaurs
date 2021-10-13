from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = None

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power