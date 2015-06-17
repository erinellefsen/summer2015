import edge
import disease

class Vertex:
    '''Vertices are passive. They do no Give the disease, rather, the disease spreads to them'''
    def __init__(self,key,disease):
        self.id = key
        self.sourceTo = []
        self.destTo = []  
        self.edgeLst = [] # may not be necessary
        self.disease = disease
        self.pred = None #Track infection
        self.status = 'S' 
        self.nextStatus = 'S'



    def addSource(self,nbr):
        self.sourceTo += [nbr]
    def addDest(self,nbr):
        self.destTo += [nbr]
    def addEdge(self,edge):
        self.edgeLst += [edge]
        
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.id) + " : " + self.status

    def getSourceTo(self):
        return self.sourceTo
    
    def getDestTo(self):
        return self.destTo

    def __iter__(self):
        return iter(self.sourceTo)

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

    def initialStatus(self,s):
        self.status = s
        self.nextStatus = s
    def incInfection(self):
        '''
        This function is called on infected individuals and updates
        how long they've been infected
        '''
        self.disease.timeInc()
    def updateVertex(self):
        '''
        This function updates the status of the vertex by
        looking at it's neighbors and for each infected, 
        it randomly infects based on contagiousness. If the
        infection spreads, the vertex's attribute nextStatus
        is updated to I. At the beginning of the next step, 
        the vertex's status will be updated.

        '''
        
        self.status = self.nextStatus
        if self.getStatus()== 'S':
            for i in self.edgeLst:
                if i.getSource().getStatus()=='I':
                    if i.checkSpread():
                        self.nextStatus = 'I'
        elif self.getStatus() == "I":
            self.incInfection()
            if self.disease.checkRecovered():
                self.nextStatus = "R"
        else:
            return
def main():
    d = disease.Disease(3,.45,.1)
    v = Vertex('A',d)
    print(v.update.__doc__)
    print("HELLO")
if __name__ == "__main__":
    main()
