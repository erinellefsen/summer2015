from vertex import *
from graph import *
class LatticeVertex(Vertex):
    def __init__(self,key,disease,x,y):
        Vertex.__init__(self,key,disease)
        self.x_coord = x
        self.y_coord = y
    def getX(self):
        return self.x_coord
    def getY(self):
        return self.y_coord
    def isNeighbor(self,vert):
        if vert.getY()+1 == self.y_coord or vert.getX()-1 == self.y_coord or vert.getX()+1 == self.x_coord or vert.getX()-1 == self.x_coord:
            return True
   
        
class LatticeGraph(Graph):
    def __init__(self,params):
        Graph.__init__(self,params)
        self.sideLength = int(math.ceil(math.sqrt(self.numVerts)))
    def makeVertices(self):
        id = 0
        for i in range(self.sideLength):
            for j in range(self.sideLength):
                if id <self.numVerts:
                    d = disease.Disease(self.k,self.p,self.r)
                    vert = LatticeVertex(id, d,i,j)
                    self.vertices.append(vert)
                    id +=1
    def getSideLength(self):
        return self.sideLength
    def makeConnections(self):
        for i in range(len(self.vertices)):
            vert1 = self.vertices[i]
            for x in range(i,len(self.vertices)):
                vert2 = self.vertices[x]
                if vert1.isNeighbor(vert2):
                    self.connect(vert1,vert2,self.rho)
                    self.connect(vert2,vert1,self.rho)
       