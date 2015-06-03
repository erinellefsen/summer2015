import sys
import disease

class Vertex:
    def __init__(self,key,disease):
        self.id = key
        self.connectedTo = []
        self.disease = disease
        self.pred = None #Track infection
        self.status = 'S' 
        self.nextStatue = 'S'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo.append(nbr)
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

    def update(self):
        '''
        This function updates the status of the vertex by
        looking at it's neighbors and for each infected, 
        it 

        '''
        return None

def main():
    d = disease.Disease(3,.45,.1)
    v = Vertex('A',d)
    print(v.update.__doc__)
    print("HELLO")
if __name__ == "__main__":
    main()
