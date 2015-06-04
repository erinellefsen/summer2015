import vertexclass
import disease
import random
class Graph:
    def __init__(self,k,p,r,initinfect, vaccinated = 0):
        self.vertices = []
        self.k = k
        self.p = p
        self.r = r
        self.infect = initinfect
        self.ilist = []
        self.rlist = []
        self.iandrlist = []

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


    def update(self, numrepetitions, numtrials):
        epidemicfor10 = 0
        epidemicfor5 = 0
        for x in range(numtrials):
            epidemic = False

            for stuff in range(0,numrepetitions):
                s = 0
                i = 0
                r = 0

                for item in self.vertices:
                    if item.getStatus() == 'S':
                        s += 1
                    if item.getStatus() == 'I':
                        i += 1
                    if item.getStatus() == 'R':
                        r += 1
                    item.update()
                if i > .05*len(self.vertices):
                    epidemic = True

                self.ilist = self.ilist + [i]
                self.rlist = self.rlist + [r]
                self.iandrlist = self.iandrlist + [i+r]
                #print("S is",s,"I is",i,"R is",r)

            if self.iandrlist[len(self.iandrlist)-1] > .10*len(self.vertices):
                #print("epidemic?",'10% at end:', True,",", ".05% I:", epidemic)
                epidemicfor10 += 1
            elif epidemic:
                epidemicfor5 += 1
            else:
                epidemicfor10+=0
                #print("epidemic?",'10% at end:', False,",", ".05% I:", epidemic)

        print(epidemicfor10/numtrials, epidemicfor5/numtrials)




def main():

    #duration,prob of infection, prob of recov, initial infection
    g = Graph(3, .02, 0, .01)
    g.makeVertices(500)         # of people
    g.makeConnections(.02)         #prob they are connected
    g.update(50,30)                   #number of repetitions, num trials


if __name__ == "__main__":
    main()
