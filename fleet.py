from weapon import Weapon
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot('Bot 1', 500)
        self.robots.append(robot_1)

        robot_2 = Robot('Bot 2', 250)
        self.robots.append(robot_2)

        robot_3 = Robot('Bot 3', 300)
        self.robots.append(robot_3)
