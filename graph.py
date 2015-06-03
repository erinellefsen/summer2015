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

    def makeConnections(self,p):
        for item in self.vertices:
            for item2 in self.vertices:
                if item.getId() != item2.getId() and item2 not in item.getConnections():
                    if random.random() < p:
                        item.addNeighbor(item2)

    def update(self):
        for item in self.vertices:
            item.update()

def main():

    g = Graph(3, .45, .1, .1)
    g.makeVertices(100)
    g.makeConnections(.25)
    for i in range(0,15):
        g.update()
        print(g.getVertices())







































if __name__ == "__main__":
    main()

