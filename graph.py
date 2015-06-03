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


    def update(self):
        s = 0
        i = 0
        r = 0
        for item in self.vertices:
            if item.getStatus() == 'S':
                s += 1
            if item.getStatus() == 'I':
                i += 1
            if item.getStatus() == "R":
                r += 1
            item.update()
        print("S is",s,"I is",i,"R is",r)

def main():
     #duration,prob of infection, prob of recov, initial infection
    g = Graph(3, .02, .05, .1)
    g.makeVertices(2000)         # of people
    g.makeConnections(.005)         #prob they are connected
    for i in range(0,40):
        g.update()

if __name__ == "__main__":
    main()







































