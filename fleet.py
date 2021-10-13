from weapon import Weapon
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot_1 = Robot('bot1')
        robot_1.health = 500
        robot_1.weapon = Weapon('Gattling Gun',100)
        self.robots.append(robot_1)

        robot_2 = Robot('bot2')
        robot_2.health = 250
        robot_1.weapon = Weapon('Blaster',75)
        self.robots.append(robot_2)

        robot_3 = Robot('bot3')
        robot_3.health = 300
        robot_1.weapon = Weapon('Power Fist',70)
        self.robots.append(robot_3)
