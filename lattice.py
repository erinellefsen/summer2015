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
        vx = vert.getX()
        vy = vert.getY()
        isXNeighbor = ((vx+1)==self.x_coord or (vx-1)==self.x_coord) and vy == self.y_coord
        isYNeighbor = ((vy+1)==self.y_coord or (vy-1)==self.y_coord) and vx == self.x_coord
        if (isXNeighbor or isYNeighbor):# and (not(isXNeighbor and isYNeighbor)):
            return True
        return False
   
        
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
            lst = self.getNeighborId(vert1)
            print "Ns \t",vert1," : ",lst," ", (vert1.x_coord,vert1.y_coord)
            for i in lst:
                if i>0 and i < self.numVerts:
                    #print vert1.getId()," : ",i
                    self.connect(vert1,self[i],1)
                    self.connect(self[i],vert1,1)
            #self.connect(vert1,self[n1],1)
            #self.connect(vert1,self[n2],1)
            #self.connect(vert1,self[n3],1)
            #self.connect(vert1,self[n4],1)
           # 
           # self.connect(self[n1],vert1,1)
            #self.connect(self[n2],vert1,1)
            #self.connect(self[n3],vert1,1)
            #self.connect(self[n4],vert1,1)
            
#            for x in range(i,len(self.vertices)):
#                vert2 = self.vertices[x]
#                if vert1.isNeighbor(vert2):
#                    self.connect(vert1,vert2,self.rho)
#                    self.connect(vert2,vert1,self.rho)
    def getNeighborId(self,vert):
        n1, n2 = vert.id -1, vert.id+1
        n3, n4 = vert.id - self.sideLength, vert.id+self.sideLength
        res = list(set([n1,n2,n3,n4])) 
        print "res: ",res
        return res
        