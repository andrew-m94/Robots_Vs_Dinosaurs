from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot_1 = Robot('bot1')
        robot_1.health = 500
        robot_1.weapon('Gattling Gun',100)

        robot_2 = Robot('bot2')
        robot_2.health = 250
        robot_1.weapon('Blaster',75)

        robot_3 = Robot('bot3')
        robot_3.health = 300
        robot_1.weapon('Power Fist',70)
