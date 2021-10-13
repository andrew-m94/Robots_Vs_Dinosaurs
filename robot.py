from weapon import Weapon
from dinosaur import Dinosaur

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.weapon = Weapon()

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power