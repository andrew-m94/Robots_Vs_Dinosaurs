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

    # def dino_turn(self, dinosaur):
    #     #In work
    #     self.show_robo_opponent_options()
    #     opponent = input('Choose which robot to attack: ')

    #     dinosaur.attack(opponent)

    def robo_turn(self, robot):
        # no return
        pass

    def show_dino_opponent_options(self):
        # no return
        pass

    def show_robo_opponent_options(self):
        element = 0
        for robot in self.fleet.robots:
            print(f'{self.fleet.robots[element].name}: {self.fleet.robots[element].health}HP Remaining')
            element += 0

    def display_winners(self): 
        # no return
        pass
