import sys

class Vertex:
    def __init__(self,key,disease):
        self.id = key
        self.connectedTo = []
        self.disease = disease
        self.pred = None #Track infection
        self.status = 'S'

    def addNeighbor(self,nbr):
        self.connectedTo = self.connectedTo + [nbr]
        #print(self.getConnections())
        #print(nbr.getConnections())
        if self not in nbr.getConnections():
            nbr.addNeighbor(self)
    def __str__(self):
        return str(self.id) + ' connectedTo: '+ str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo
    def getId(self):
        return self.id


    def setPred(self,p):
        self.pred = p
    def getPred(self):
        return self.pred
    def setStatus(self,status):
        self.status = status
    def getStatus(self):
        return self.status

