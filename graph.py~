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


    def update(self, numrepetitions):
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

        newlist = []
        for item in range(len(self.ilist)-1):
            newlist = newlist + [self.ilist[item + 1] - self.ilist[item]]
        newlist2 = []
        for item in range(len(self.rlist) -1):
            newlist2 = newlist2 + [self.rlist[item+1] - self.rlist[item]]
        newlist3 = []
        for item in range(len(self.iandrlist)-1):
            newlist3 = newlist3 + [self.iandrlist[item+1] - self.iandrlist[item]]
        if self.iandrlist[len(self.iandrlist)-1] > .10*len(self.vertices):
            print("epidemic?",'10% at end:', True,",", ".05% I:", epidemic)
        else:
            print("epidemic?",'10% at end:', False,",", ".05% I:", epidemic)





def main():

    #duration,prob of infection, prob of recov, initial infection
    g = Graph(2, .02, 0, .01)
    g.makeVertices(500)         # of people
    g.makeConnections(.02)         #prob they are connected
    g.update(100)


if __name__ == "__main__":
    main()
