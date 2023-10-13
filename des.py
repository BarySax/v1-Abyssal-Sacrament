import random

class Des:
    def __init__(self):
        self.num = 0
    
    def lancer(self, num_des, face):
        self.lancer = []

        for i in range(num_des):
            result = random.randint(1,face)
            self.lancer.append(result)
            print(result)