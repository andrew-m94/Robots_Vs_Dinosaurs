from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.robot_weapons()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print('Welcome to Robots Vs Dinosaurs!')
        print('Each team will take turns attacking opponents using number keys 1-3')
        input('Press enter to begin!')
        print('')

    def battle(self):
        dino_element = 0
        robo_element = 0

        while len(self.fleet.robots) != 0 or len(self.herd.dinosaurs) != 0:
           
            if len(self.herd.dinosaurs) != 0:

                if dino_element >= len(self.herd.dinosaurs):
                    dino_element = 0

                self.dino_turn(self.herd.dinosaurs[dino_element])
                dino_element += 1

            else:
                break
           
            if len(self.fleet.robots) != 0:

                if robo_element >= len(self.fleet.robots):
                    robo_element = 0

                self.robo_turn(self.fleet.robots[robo_element])
                robo_element += 1
            
            else:
                break

    def dino_turn(self, dinosaur):
        print(f'\n{dinosaur.name} is attacking!')
        self.show_robo_opponent_options()

        opponent = ''
        opponent_choices = ['1','2','3']

        while opponent not in opponent_choices:
            opponent = (input('Choose which robot to attack: #'))
        
        self.dino_attack_name(dinosaur)
        dinosaur.attack(self.fleet.robots[int(opponent)-1])

        if self.fleet.robots[int(opponent) - 1].health <= 0:
            self.fleet.robots.remove(self.fleet.robots[int(opponent) - 1])

    def robo_turn(self, robot):
        print(f'\n{robot.name} is attacking!')
        self.show_dino_opponent_options()

        opponent = ''
        opponent_choices = ['1','2','3']

        while opponent not in opponent_choices:
            opponent = (input('Choose which dinosaur to attack: #'))

        robot.attack(self.herd.dinosaurs[int(opponent)-1])

        if self.herd.dinosaurs[int(opponent) - 1].health <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[int(opponent) - 1])

    def show_dino_opponent_options(self):
        element = 0
        option = 1
        print('')

        for dino in self.herd.dinosaurs:
            print(f'[{option}] {self.herd.dinosaurs[element].name}: {self.herd.dinosaurs[element].health}HP Remaining')
            element += 1
            option += 1

    def show_robo_opponent_options(self):
        element = 0
        option = 1
        print('')

        for robot in self.fleet.robots:
            print(f'[{option}] {self.fleet.robots[element].name}: {self.fleet.robots[element].health}HP Remaining')
            element += 1
            option  += 1

    def display_winners(self):

        if len(self.herd.dinosaurs) == 0:
            print('Robots win!')

        if len(self.fleet.robots) == 0:
            print('Dinosaurs win!')

    def robot_weapons(self):
        element = 0
        
        for robot in self.fleet.robots:
            self.fleet.robots[element].choose_weapon()
            element += 1

    def dino_attack_name(self, dinosaur):
        attacks = ('Bite','Headbutt','Tailwhip')
        options = 1
        print('')

        for attack_name in attacks:
            print(f'[{options}] {attack_name}')
            options += 1

        attack_choices = ['1','2','3']
        choice = ''

        while choice not in attack_choices:
            choice = (input('Choose an attack!'))

        print(f'\n{dinosaur.name} used {attacks[int(choice) - 1]}!')


