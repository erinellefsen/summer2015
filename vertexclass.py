import sys

class Vertex:
    def __init__(self,key,disease):
        self.id = key
        self.connectedTo = {}
        self.disease = disease
        self.status = 'S'  #S = 1, I = 2, R = 3. Use random numbers to assign.
        self.pred = None #Track infection
        self.lengthOfInfection 
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
    def setColor(self,color):
        self.color = color
    def setDistance(self,d):
        self.dist = d
    def setPred(self,p):
        self.pred = p
    def setDiscovery(self,dtime):
        self.disc = dtime
    def setFinish(self,ftime):
        self.fin = ftime
    def getFinish(self):
        return self.fin
    def getDiscovery(self):
        return self.disc
    def getPred(self):
        return self.pred
    def getDistance(self):
        return self.dist
    def getColor(self):
        return self.color
