import vertexclass
import disease
import random
class Graph:
    def __init__(self,k,p,r,initinfect, vaccinated = 0):
        self.vertices = []
        self.k = k
        self.p = p
        self.r = r
        self.infectRate = initinfect
        self.ilist = []
        self.rlist = []
        self.iandrlist = []
        self.numS = 0
        self.numI = 0
        self.numR = 0
        self.highEpi = False
        self.finalEpi = False
    
    def resetGraph(self):
        '''We need to save the original state of the graph'''
        pass
    def getVertices(self):
        return self.vertices

    def makeVertices(self,numVertices):
        for item in range(0,numVertices):
            v = vertexclass.Vertex(item, disease.Disease(self.k,self.p,self.r))
            self.vertices = self.vertices + [v]
            if random.random() < self.infect:
                v.initialInfect()


    def makeConnections(self,x):
        for item in self.vertices:
            for item2 in self.vertices:
                if item.getId() != item2.getId() and item2 not in item.getConnections():
                    if random.random() < x:
                        item.addNeighbor(item2)


    def countAndUpdateStatuses(self):
        '''Helper Function for update'''
        
        for item in self.vertices:
            if item.getStatus() == 'S':
                self.numS += 1
            if item.getStatus() == 'I':
                self.numI += 1
            if item.getStatus() == 'R':
                self.numR += 1
            item.update()
            
    def updateLists(self):
        '''Helper function for update'''
        self.ilist = self.ilist + [self.numI] 
        self.rlist = self.rlist + [self.numR]
        self.iandrlist = self.iandrlist + [self.numI+self.numR]
    def checkHighConcentrationEpi(self):
        '''Helper Function for update'''
        if self.numI > .05*len(self.vertices):
            self.highEpi = True
    def checkFinalEpi(self):
        '''Help Function for update '''
        if self.iandrlist[len(self.iandrlist)-1] > .10*len(self.vertices):
            self.finalEpi = True
    def update(self, numrepetitions, numtrials):
        for stuff in range(0,numrepetitions):
            self.countAndUpdateStatuses()
            self.updateLists()
            self.checkHighConcentrationEpi()

        self.checkFinalEpi()
        #print(epidemicfor10/numtrials*100,"%", "epidemic for 10% at end", epidemicfor5/numtrials*100,"%","epidemic for 5% at any time")
    def getEpis(self):
        '''Returns boolean values for if epidemics occured. 
        output: finalEpi, highEpi
        '''
        return self.getFinalEpi(), self.getHighEpi()
    def getFinalEpi(self):
        return self.finalEpi
    def getHighEpi(self):
        return self.highEpi


def main():

    #duration,prob of infection, prob of recov, initial infection
    g = Graph(2, .02, 0, .01)   #k,p,r,%infected
    g.makeVertices(500)         # of people
    g.makeConnections(.02)         #prob they are connected
    g.update(50,30)                   #number of repetitions, num trials


if __name__ == "__main__":
    main()
