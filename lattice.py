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
        rightIdX = self.x_coord + 1 
        leftIdX = self.x_coord - 1
        isNextToX = vx == leftIdX  or vx == rightIdX
        isConstantY =  vy == self.y_coord
        noWrap = not (rightIdX % 3 ==0 or (leftIDX+1)%3 == 0)
        
        isXNeighbor = isNextToX and isConstantY and noWrap
        isYNeighbor = ((vy+1)==self.y_coord or (vy-1)==self.y_coord) and vx == self.x_coord
        if (isXNeighbor or isYNeighbor):# and (not(isXNeighbor and isYNeighbor)):
            return True
        return False
    
    

        
class LatticeGraph(Graph):
    def __init__(self,params):
        Graph.__init__(self,params)
        self.sideLength = int(math.ceil(math.sqrt(self.numVerts)))
        self.makeVertices()
        self.makeConnections()
        self.vaccinate(self.targeted)
        
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
            #print "Ns \t",vert1," : ",lst," ", (vert1.x_coord,vert1.y_coord)
            for i in lst:
                if i !=None and i>0 and i < self.numVerts:
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
    def getXNeighbor(self,vert):
        rightIdX = vert.x_coord + 1 
        leftIdX = vert.x_coord - 1
        if rightIdX % self.sideLength ==0 :
            return [leftIdX]
        elif (leftIdX+1) % self.sideLength == 0:
            return [rightIdX]
        else: 
            return [rightIdX,leftIdX]
    def getNeighborId(self,vert):
        yu = vert.id - self.sideLength
        yd = vert.id + self.sideLength
        if vert.id %self.sideLength ==0:
            xl = None
        else:
            xl = vert.id-1
        if (vert.id+1) % self.sideLength == 0:
            xr = None
        else:
            xr = vert.id+1
        res = list(set([xl,xr,yu,yd]))
        return res