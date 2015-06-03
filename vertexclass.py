import sys

class Vertex:
    def __init__(self,key,disease):
        self.id = key
        self.connectedTo = {}
        self.disease = disease
        self.pred = None #Track infection
        self.status = 'S'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connectedTo: '+ str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setPred(self,p):
        self.pred = p
    def getPred(self):
        return self.pred
    def setStatus(self,status):
        self.status = status
    def getStatus(self):
        return self.status

