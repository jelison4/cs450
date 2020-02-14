import random

class Neuron:
    def __init__ (self, value, weight, isBias):
        #self.weight = random.uniform(-10,10)
        self.weight = weight
        self.value = value
        self.isBias = isBias