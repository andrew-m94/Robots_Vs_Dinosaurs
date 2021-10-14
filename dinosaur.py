class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 0
        self.energy = 100

    def attack(self, robot):
        if self.energy > 0:
            robot.health -= self.attack_power
            self.energy -= 10

        elif self.energy <= 0:
            print('Out of energy! Attack Failed! Resting...')
            self.energy = 100
