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
        dino_element = 0
        robo_element = 0

        while len(self.fleet.robots) != 0 or len(self.herd.dinosaurs) != 0:
            
            if dino_element >= len(self.herd.dinosaurs):
                dino_element = 0

            self.dino_turn(self.herd.dinosaurs[dino_element])
            dino_element += 1
           
            if len(self.fleet.robots) != 0:

                if robo_element >= len(self.fleet.robots):
                    robo_element = 0

                self.robo_turn(self.fleet.robots[robo_element])
                robo_element += 1

    def dino_turn(self, dinosaur):
        self.show_robo_opponent_options()
        opponent = int(input('Choose which robot to attack: #'))

        dinosaur.attack(self.fleet.robots[opponent-1])

        if self.fleet.robots[opponent - 1].health <= 0:
            self.fleet.robots.remove(self.fleet.robots[opponent - 1])

    def robo_turn(self, robot):
        self.show_dino_opponent_options()
        opponent = int(input('Choose which dinosaur to attack: #'))

        robot.attack(self.herd.dinosaurs[opponent-1])

        if self.herd.dinosaurs[opponent - 1].health <= 0:
            self.herd.dinosaurs.remove(self.herd.dinosaurs[opponent - 1])

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
