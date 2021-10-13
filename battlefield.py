from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        # no return
        pass

    def display_welcome(self):
        # no return
        pass

    def battle(self):
        # no return
        pass

    def dino_turn(self, dinosaur):
        self.show_robo_opponent_options()
        opponent = int(input('Choose which robot to attack: #'))

        dinosaur.attack(self.fleet.robots[opponent-1])

    def robo_turn(self, robot):
        self.show_dino_opponent_options()
        opponent = int(input('Choose which dinosaur to attack: #'))

        robot.attack(self.herd.dinosaurs[opponent-1])

    def show_dino_opponent_options(self):
        element = 0
        option = 1

        for dino in self.herd.dinosaurs:
            print(f'[{option}] {self.herd.dinosaurs[element].name}: {self.herd.dinosaurs[element].health}HP Remaining')
            element += 1
            option += 1

    def show_robo_opponent_options(self):
        element = 0
        option = 1

        for robot in self.fleet.robots:
            print(f'[{option}] {self.fleet.robots[element].name}: {self.fleet.robots[element].health}HP Remaining')
            element += 1
            option  += 1

    def display_winners(self): 
        # no return
        pass
