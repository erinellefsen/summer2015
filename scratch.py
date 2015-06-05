

import random

def makeClusteredConnections(self,lowendprob,highendprob): #added more discriptive parameter '''Helper Function that creates all of the graphs connections'''
    x = random.randrange(lowendprob,highendprob+1)/100
    for item in self.vertices:
        for item2 in self.vertices:
            if item.getId() != item2.getId() and item2 not in item.getConnections():
                if random.random() < x:
                    item.addNeighbor(item2)

def makebetterClusteredConnections(self, standardprob):
    for item in self.vertices:
        for item2 in self.vertices:
            if item.getId() != item2.getId() and item2 not in item.getConnections():
                x = item.getConnections()
                y = item2.getConnections()
                count = 0
                for connection in x:
                    if connection in y:
                        count +=1
                if random.random() < count * standardprob:
                    item.addNeighbor(item2)