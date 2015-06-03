import vertexclass
import disease
import random
class Graph:
    def __init__(self,k,p,r, initinfectrate, vaccinated = 0):
        self.vertices = []
        self.k = k
        self.p = p
        self.r = r
        self.infect = initinfectrate
    def makeVertices(self,numVertices):
        for item in range(0,numVertices):
            v = vertexclass.Vertex(id, disease.Disease(self.k,self.p,self.r))
            self.vertices = self.vertices + [v]
            if random.random < self.infect:
                v.initialInfect('I')

    def makeConnections(self,p):
        for item in self.vertices:
            for item2 in self.vertices:
                if item != item and item2 not in item.getConnections():
                    if random.random() < p:
                        item.addNeighbor(item2)
    def update(self):
        for item in self.vertices:
            item.update()


def main():
<<<<<<< HEAD
    count = 0
    for i in range(5):

        A = vertexclass.Vertex("A",disease.Disease(3,.45,.1))
        B = vertexclass.Vertex("B",disease.Disease(3,.45,.1))
        C = vertexclass.Vertex("C",disease.Disease(3,.45,.1))
        D = vertexclass.Vertex("D",disease.Disease(3,.45,.1))
        E = vertexclass.Vertex("E",disease.Disease(3,.45,.1))
        F = vertexclass.Vertex("F",disease.Disease(3,.45,.1))
        G = vertexclass.Vertex("G",disease.Disease(3,.45,.1))
        H = vertexclass.Vertex("H",disease.Disease(3,.45,.1))
        I = vertexclass.Vertex("I",disease.Disease(3,.45,.1))
        
        vertLst = [A,B,C,D,E,F,G,H,I]
        
        A.addNeighbor(B)
        A.addNeighbor(C)
        B.addNeighbor(D)
        B.addNeighbor(G)
        C.addNeighbor(E)
        C.addNeighbor(F)
        D.addNeighbor(F)
        E.addNeighbor(H)
        F.addNeighbor(H)
        F.addNeighbor(I)
        H.addNeighbor(I)
        A.initialInfect()
        for i in range(5):
            for i in vertLst:
                i.update()
            print(vertLst)
                
        count += 1
        print("End case ",count)

if __name__ == "__main__":
    main()

