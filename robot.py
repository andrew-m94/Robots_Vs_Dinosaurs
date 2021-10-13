from weapon import Weapon

class Robot:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.armory = []
        self.fill_armory()
        self.weapon = None

    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power

    def choose_weapon(self):
        option = 1

        for weapon in self.armory:
            print(f'[{option}] {weapon.name}')
            option += 1
    
        choice = int(input('Robot team, Choose your weapons!'))
        print('')
        
        self.weapon = self.armory[(choice - 1)]

    def fill_armory(self):
        weapon_one = Weapon('Gattling Gun',100)
        weapon_two = Weapon('Blaster', 75)
        weapon_three = Weapon('Power Fist', 70)

        self.armory.append(weapon_one)
        self.armory.append(weapon_two)
        self.armory.append(weapon_three)