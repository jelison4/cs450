import random

class Neuron:
    def __init__ (self, value, weight, isBias):
        self.weight = random.uniform(-1.0,1.0)
        self.weight = weight
        self.value = value
        self.isBias = isBias