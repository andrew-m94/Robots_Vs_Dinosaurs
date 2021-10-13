from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):

        dino_1 = Dinosaur('T-rex, 100')
        dino_1.health = 500

        dino_2 = Dinosaur('Velociraptor, 75')
        dino_2.health = 250

        dino_3 = Dinosaur('Ankylosaurus, 70')
        dino_3.health = 300


        
        