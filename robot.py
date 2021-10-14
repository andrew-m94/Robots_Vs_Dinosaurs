from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.power_level = 100
        self.armory = []
        self.fill_armory()
        self.weapon = None #set through choose_weapon()

    def attack(self, dinosaur):
        if self.power_level > 0:
            dinosaur.health -= self.weapon.attack_power
            self.power_level -= 10

        elif self.power_level <= 0:
            print('Out of power! attack failed! Recharging...')
            self.power_level = 100

    def choose_weapon(self):
        option = 1

        for weapon in self.armory:
            print(f'[{option}] {weapon.name}')
            option += 1

        weapon_choices = ['1','2','3']
        choice = ''

        while choice not in weapon_choices:
            choice = (input(f'Robot team, Choose a weapon for {self.name}!'))
            print('')

        self.weapon = self.armory[(int(choice) - 1)]

    def fill_armory(self):
        weapon_one = Weapon('Gattling Gun',100)
        weapon_two = Weapon('Blaster', 75)
        weapon_three = Weapon('Power Fist', 70)

        self.armory.append(weapon_one)
        self.armory.append(weapon_two)
        self.armory.append(weapon_three)