from weapon import Weapon
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot('bot 1', 500)
        self.robots.append(robot_1)

        robot_2 = Robot('bot 2', 250)
        self.robots.append(robot_2)

        robot_3 = Robot('bot 3', 300)
        self.robots.append(robot_3)
