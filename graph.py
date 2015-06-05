import vertexclass
import disease
import random
import copy 
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

    def resetGraph(self):
        '''We need to save the original state of the graph'''
        self.resetCounts()
        self.resetLists()
        self.resetBools()
        temp = self.spliceLst(self.original)
        self.vertices = []
        for i in temp:
            self.vertices.append(copy.deepcopy(i))
        self.vertices = copy.deepcopy(self.original)

    def spliceLst(self,lst):
        lstLst = []
        l = len(lst)
        step = l // 200 + 1
        old = 0
        for i in range(step):
            lstLst.append(lst[old:old+200])
            old += 200
        return lstLst

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



    def makeConnections(self,probOfConnection): #added more discriptive parameter
        '''Helper Function that creates all of the graphs connections'''
        for item in self.vertices:
            for item2 in self.vertices:
                if item.getId() != item2.getId() and item2 not in item.getConnections():
                    if random.random() < probOfConnection:
                        item.addNeighbor(item2)
    
    def saveOriginal(self):
        '''This function saves the first state of the graph, after vertices and connections have been made'''
        if self.original == []:
            self.original = copy.deepcopy(self.vertices)
                    
    def makeVerticesAndConnections(self,numVertices,probOfConnection):
        self.makeVertices(numVertices)
        self.makeConnections(probOfConnection)
        self.saveOriginal()

    def resetLists(self):
        self.ilist,self.rlist,self.iandrlist = [],[],[]
    def resetBools(self):
        self.highEpi,self.finalEpi = False,False
    def resetCounts(self):
        '''Helper Function for countAndUpdateStatuses'''
        self.numS, self.numR, self.numI = 0,0,0
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

    def checkHighConcentrationEpi(self):
        '''Helper Function for update'''
        if self.numI > self.highTreshold*len(self.vertices):
            self.highEpi = True
    def checkFinalEpi(self):
        '''Help Function for update '''
        if self.iandrlist[len(self.iandrlist)-1] > self.finalThreshold*len(self.vertices):
            self.finalEpi = True

    def getCurrentState(self):
        '''returns the current state of the graph'''
        return self.vertices

    def countAndUpdateStatuses(self):
        '''Helper Function for update'''
        self.numS = 0
        self.numR = 0
        self.numI = 0
        for item in self.vertices:
            if item.getStatus() == 'S':
                self.numS += 1
            if item.getStatus() == 'I':
                self.numI += 1
            if item.getStatus() == 'R':
                self.numR += 1
            item.updateVertex()

    def getStatuses(self):
        return self.numS, self.numI, self.numR
            
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

    def __repr__(self):
        stri = ""
        for i in self.vertices:
            stri += str(i)
        return(stri)

def main():
    vaccinationpercent = 0
    orderedpairlistHighEpi = []
    orderedpairlistLowEpi = []
    while vaccinationpercent < 1:
        trials = 60
        HighEpi = 0
        FinalEpi = 0
        for x in range(trials):

            g = Graph(10, .02, 0, .01, vaccinationpercent)   #k,p,r,%infected,%vaccinated
            g.makeVertices(500)         #of people
            g.makeConnections(.01)         #prob they are connected
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
    test()
