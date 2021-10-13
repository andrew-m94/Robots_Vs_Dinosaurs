from weapon import Weapon
from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        weapon_one = Weapon('Gattling Gun',100)
        robot_1 = Robot('bot1', 500, weapon_one)
        self.robots.append(robot_1)

        weapon_two = Weapon('Blaster', 75)
        robot_2 = Robot('bot2', 250, weapon_two)
        self.robots.append(robot_2)

        weapon_three = Weapon('Power Fist', 70)
        robot_3 = Robot('bot3', 300, weapon_three)
        self.robots.append(robot_3)
