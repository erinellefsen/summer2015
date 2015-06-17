import vertex
import random
import numpy as np


class Edge():
    '''An Edge class makes a directed connection from vertA to vertB with weight w'''
    def __init__(self,vertA,vertB,w):
        self.a = vertA
        self.b = vertB
        self.weight = self.calcWeight(w)

    def __repr__(self):
        return str(self.a.getId())+"--"+str(self.weight)+"-->"+str(self.b.getId())
    def getWeight(self):
        return self.weight
    def getSource(self):
        return self.a
    def getDest(self):
        return self.b
    def checkSpread(self):
        if random.random() < self.weight:
            return True
        else:
            return False
    def calcWeight(self,mean):
        return np.random.normal(mean,mean/3.5)