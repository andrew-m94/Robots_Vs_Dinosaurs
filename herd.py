from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):

        dino_1 = Dinosaur('T-rex', 100)
        dino_1.health = 500
        self.dinosaurs.append(dino_1)

        dino_2 = Dinosaur('Velociraptor', 75)
        dino_2.health = 250
        self.dinosaurs.append(dino_2)

        dino_3 = Dinosaur('Ankylosaurus', 70)
        dino_3.health = 300
        self.dinosaurs.append(dino_3)


        
        