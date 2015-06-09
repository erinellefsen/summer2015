import vertexclass
import disease
import random
import copy
import tank
class Graph:
    def __init__(self,k,p,r,initinfect, vaccinated = 0.0):
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
        self.vaccine = vaccinated
        self.highThreshold = .05
        self.finalThreshold = .1
        self.original = []

    def getVertices(self):
        return self.vertices

    def makeVertices(self,numVertices):
        '''Helper function that creates all of the graphs vertex objects'''
        for item in range(0,numVertices):
            v = vertexclass.Vertex(item, disease.Disease(self.k,self.p,self.r))
            self.vertices = self.vertices + [v]
            if random.random() < self.infectRate:
                v.initialStatus("I")
            if v.getStatus() != "I" and random.random() <  self.vaccine:
                v.initialStatus("V")

    def makeConnections(self,probOfConnection): 
        '''Helper Function that creates all of the graphs connections'''
        for item in self.vertices:
            for item2 in self.vertices:
                if item.getId() != item2.getId() and item2 not in item.getConnections():
                    if random.random() < probOfConnection:
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
                    if count == 0:
                        if random.random()<standardprob:
                            item.addNeighbor(item2)
                    else:
                        if random.random() < count * standardprob:
                            item.addNeighbor(item2)


    def makeVerticesAndConnections(self,numVertices,probOfConnection):
        self.makeVertices(numVertices)
        self.makeConnections(probOfConnection)
        self.original = self.copyVertices(self.vertices,self.original)


    def copyVertices(self,source,dest):
        '''This function saves the first state of the graph, after vertices and connections have been made'''
        source_tank = tank.Tank(source)
        dest_tank = copy.deepcopy(source_tank)
        source = source_tank.lift()
        dest = dest_tank.lift()
        return dest
        
    def resetGraph(self):
        '''We need to save the original state of the graph'''

        self.vertices = self.copyVertices(self.original,self.vertices)
        
    def totalReset(self):
        self.resetCounts()
        self.resetLists()
        self.resetBools()
        self.resetGraph()           


    def resetLists(self):
        self.ilist,self.rlist,self.iandrlist = [],[],[]
    def resetBools(self):
        self.highEpi,self.finalEpi = False,False
    def resetCounts(self):
        '''Helper Function for countAndUpdateStatuses'''
        self.numS, self.numR, self.numI = 0,0,0

    def checkHighConcentrationEpi(self):
        '''Helper Function for update'''
        if self.numI > self.highThreshold*len(self.vertices):
            self.highEpi = True
    def checkFinalEpi(self):
        '''Help Function for update '''
        if self.iandrlist[len(self.iandrlist)-1] > self.finalThreshold*len(self.vertices):
            self.finalEpi = True


    def getCurrentState(self):
        '''returns the current state of the graph'''
        return self.vertices

    def getStatuses(self):
        return self.numS, self.numI, self.numR
    
    def countAndUpdateStatuses(self):
        '''Helper Function for update'''
        self.resetCounts()
        for item in self.vertices:
            if item.getStatus() == 'S':
                self.numS += 1
            if item.getStatus() == 'I':
                self.numI += 1
            if item.getStatus() == 'R':
                self.numR += 1
            item.updateVertex()

    def updateLists(self):
        '''Helper function for update'''
        self.ilist = self.ilist + [self.numI] 
        self.rlist = self.rlist + [self.numR]
        self.iandrlist = self.iandrlist + [self.numI+self.numR]            
            
            
    def update(self, numrepetitions):
        for stuff in range(0,numrepetitions):
            self.countAndUpdateStatuses()
            self.updateLists()
            self.checkHighConcentrationEpi()

        self.checkFinalEpi()
        
    

    def getEpis(self):
        '''Returns boolean values for if epidemics occured. 

        output: finalEpi, highEpi
        '''
        return self.getFinalEpi(), self.getHighEpi()
    def getFinalEpi(self):
        '''returns finalEpi, a boolean that says whether an overall epidemic occured  '''
        return self.finalEpi
    def getHighEpi(self):
        '''returns highEpi, a boolean that says whether a high concentration epidemic occured  '''

        return self.highEpi

    #def __repr__(self):
    #    stri = ""
    #    for i in self.vertices:
    #        stri += str(i) + " "
    #    return(stri)
    def printHi(self):
        print("Hi")

def main():
    vaccinationpercent = 0
    orderedpairlistHighEpi = []
    orderedpairlistLowEpi = []
    while vaccinationpercent < 1:
        trials = 30
        HighEpi = 0
        FinalEpi = 0
        for x in range(trials):

            g = Graph(8, .9, 0, .02, vaccinationpercent)   #k,p,r,%infected,%vaccinated
            g.makeVertices(100)         #of people
            g.makebetterClusteredConnections(.005)         #prob they are connected
            g.update(50)            #number of repetitions, num trials
            if g.getHighEpi():
                HighEpi +=1
            if g.getFinalEpi():
                FinalEpi +=1
        orderedpairlistHighEpi = orderedpairlistHighEpi + [[vaccinationpercent,(HighEpi/trials)*100]]
        orderedpairlistLowEpi = orderedpairlistLowEpi + [[vaccinationpercent, (FinalEpi/trials)*100]]

        y = (vaccinationpercent,(HighEpi/trials)*100 , (FinalEpi/trials)*100)

        vaccinationpercent += .05
    print(".05 at a time" , orderedpairlistHighEpi)
    print(".10 at end time" , orderedpairlistLowEpi)


if __name__ == "__main__":
    main()

