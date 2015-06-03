import sys
import disease

class Vertex:
    def __init__(self,key,disease):
        self.id = key
        self.connectedTo = []
        self.disease = disease
        self.pred = None #Track infection
        self.status = 'S' 
        self.nextStatus = 'S'


    def addNeighbor(self,nbr):
        self.connectedTo = self.connectedTo + [nbr]

        if self not in nbr.getConnections():
            nbr.addNeighbor(self)
    def __repr__(self):
        return str(self.id)
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
        '''THis is a cool comment thing'''
        return None

def main():
    d = disease.Disease(3,.45,.1)
    v = Vertex('A',d)
    print(v.update.__doc__)
    print("HELLO")
if __name__ == "__main__":
    main()
