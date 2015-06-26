import vertex
import disease
import random
import copy
import tank
import math
import edge
import group
import numpy as np
import params as pm
import networkx as nx


class Graph:
    def __init__(self,params,clustered = False,lattice = False):
        self.vertices = []
        self.edges = []
        self.k = params.k
        self.p = params.p
        self.r = params.r
        self.numVerts=params.numVerts
        self.nu = params.numVacc    #number of vaccinated individuals
        self.rho = params.connectionProb  #percent of population each node should connect to
        self.percentVacc = params.percentVacc
        self.random = params.random
        self.ilist = []
        self.rlist = []
        self.iandrlist = []
        self.numS = 0
        self.numI = 0
        self.numR = 0
        self.nx = None
        self.highEpi = False
        self.finalEpi = False
        self.grouplist = []
        self.highThreshold = .05
        self.finalThreshold = .1
        self.original = []
        self.q = 1-((1-self.p)**self.k) #succes of spread to neighbor. 
        self.numGroups = int(6 + .01*self.numVerts)
        #self.makeVertices()
        #self.makeNewConnections()
        '''make vertices. make connections. Calculate hubscores. infect 1. vaccinate, either randomly or with targeted vaccination'''
        
        if clustered:
            self.makeVertices()
            self.makeClusteredConnections()
            self.vaccinate()
        if random:
            self.makeVertices()
            self.makeConnections()
            self.vaccinate()
        #if not self.random:
        #    self.calcHubs()

        
    
    def addEdge(self,edge):
        self.edges += [edge]
    
    def calcHubs(self):
        if self.nx == None:
            self.nx = self.makeNetworkX()
        paths = nx.shortest_path_length(self.nx)
        for vert in self.vertices:
            distLst = []

            lengthLst = paths[vert].values()
            lengthLst.sort()
            res = 0
            current = 1
            for i in range(1,len(lengthLst)):
                temp = lengthLst[i]

                res += (self.q**temp)
            vert.setHubScore(res)
      
        
    def calculateR(self, basic = False):
        res = (self.sumNeighbors(basic)/float(len(self.vertices)))*self.q
        return res
    
    def checkFinalEpi(self):
        '''Help Function for update '''
        if self.iandrlist[len(self.iandrlist)-1] > self.finalThreshold*len(self.vertices):
            self.finalEpi = True
    
    def checkHighConcentrationEpi(self):
        '''Helper Function for update'''
        if self.numI > self.highThreshold*len(self.vertices):
            self.highEpi = True
    
    def connect(self,source,dest, connprob):
        if random.random() < connprob: # check to see if this number 
            source.addSource(dest)
            dest.addDest(source)
            ed = edge.Edge(source,dest,self.p) #or use some distribution counter (adjust edge)
            dest.addEdge(ed)
            self.addEdge(ed)   
    
    def copyVertices(self,source,dest):
        '''This function saves the first state of the graph, after vertices and connections have been made'''
        source_tank = tank.Tank(source)
        dest_tank = copy.deepcopy(source_tank)
        source = source_tank.lift()
        dest = dest_tank.lift()
        return dest       
    
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
    
    def getClusteringCoefficient(self):
        if self.nx == None:
            self.nx = self.makeNetworkX()
        ccLst = nx.clustering(self.nx).values()
        res = np.mean(ccLst)
        return res
        
    def getEdges(self):
        return self.edges
        
    def getEpis(self):
        '''Returns boolean values for if epidemics occured. 

        output: finalEpi, highEpi
        '''
        return self.getFinalEpi(), self.getHighEpi()
    def getFinalEpi(self):
        '''returns finalEpi, a boolean that says whether an overall epidemic occured  '''
        return self.finalEpi
    
    def getGroupList(self):
        return self.grouplist
    
    def getI(self):
        return self.numI
    
    def getHighEpi(self):
        '''returns highEpi, a boolean that says whether a high concentration epidemic occured  '''

        return self.highEpi
    
    def getR(self):
        return self.numR     
    
    def getStatuses(self):
        return self.numS, self.numI, self.numR

    def getVertices(self):
        return self.vertices   
   
    def makeClusteredConnections(self):
        grouplst = self.makeGroups()
        for group in grouplst:
            probOfConn = group.getProbOfConn()
            memberlst = group.getMembers()
            for i in range(len(memberlst)):
                member = memberlst[i]
                for x in range(i+1,len(memberlst)):
                    member2 = memberlst[x]
                    self.twoWayConnect(member,member2,probOfConn)
    
    def makeGroups(self): 
         
        numpeople = int(.99*self.numVerts)
        track = 0
        while track < numpeople:
            people = int(math.ceil(np.random.normal(1.5,.5)))
            g = group.Group(len(self.grouplist)+1,5/self.numVerts,1,self.p)
            self.grouplist = self.grouplist + [g]
            for x in range(track,track + people + 1):
                g.addMember(self.vertices[x])
            track = track + people + 1
        numfamilies = len(self.grouplist)
        for x in range(self.numGroups):
            y = random.random()
            if y > 0 and y <= .90:
                propIncl = np.random.normal((50*self.numVerts)/(500+self.numVerts),(20000+self.numVerts)/(20000))
                probofConn =  .175
            if y > .80:
                propIncl = np.random.normal((200*self.numVerts)/(2000+self.numVerts),(20000+self.numVerts)/(20000))
                probofConn = .1
            self.grouplist = self.grouplist + [group.Group(len(self.grouplist)+1, propIncl , probofConn, self.p)]
        for x in range(numfamilies, len(self.grouplist)):
            x = self.grouplist[x]
            numIncl = int(x.getPropIncl())
            includedlst = random.sample(range(self.numVerts),numIncl)
            for y in includedlst:
                x.addMember(self.vertices[y])        
        return self.grouplist
    
    def makeNetworkX(self):
        G=nx.Graph()
        G.add_nodes_from(self.getVertices())
        edgeLst = []
        for vert in self.getVertices():
            connections = vert.getDestTo()
            for i in connections:
                edgeLst.append([vert,i])
        G.add_edges_from(edgeLst)
        return G
        #nx.draw_networkx(G,node_size = 100,node_color="lightblue")

    def makeConnections(self,  twoWay=True ): 
        '''Helper Function that creates all of the graphs connections''' 
        for i in range(len(self.vertices)):
            item = self.vertices[i]
            for x in range(i+1,len(self.vertices)):
                item2 = self.vertices[x]
                if twoWay:
                    self.twoWayConnect(item,item2, self.rho)
                else:
                    self.connect(item,item2,self.rho)
                    self.connect(item2,item,self.rho)
                    #if random.random() < probOfConnection:


    def makeVertHubDict(self):
        resDct = {}
        for vert in self.vertices:
            resDct[vert] = vert.getHubScore()
        return resDct
        
    def makeVertices(self):
        '''Helper function that creates all of the graphs vertex objects'''

        for item in range(0,self.numVerts):
            v = vertex.Vertex(item, disease.Disease(self.k,self.p,self.r))
            self.vertices = self.vertices + [v]


    def makeVerticesAndConnections(self):
        self.makeVertices()
        self.makeConnections()
        self.original = self.copyVertices(self.vertices,self.original)
    
    def randomVacc(self):
        infected = random.randrange(0,self.numVerts)
        listofvaccinated = []
        while len(listofvaccinated) < self.nu: 
            x = random.randrange(0,self.numVerts)
            if x != infected and x not in listofvaccinated:
                listofvaccinated = listofvaccinated + [x]
        for v in self.vertices:
            if v.getId() == infected:
                v.initialStatus('I')
            if v.getId() in listofvaccinated:
                v.initialStatus('V')
    def resetBools(self):
        self.highEpi,self.finalEpi = False,False
        
    def resetCounts(self):
        '''Helper Function for countAndUpdateStatuses'''
        self.numS, self.numR, self.numI = 0,0,0
        
    def resetGraph(self):
        '''We need to save the original state of the graph'''
        self.vertices = self.copyVertices(self.original,self.vertices)                    

    def resetLists(self):
        self.ilist,self.rlist,self.iandrlist = [],[],[]
        
    def setup(self):
        self.makeVertices()
        self.makeConnections()
    

    def sumNeighbors(self, basic):
        count = 0
        if not basic:
            for item in self.vertices:

                lst = item.getSourceTo()

                for vert in lst:
                    if not vert.getStatus() == 'V':
                        count += 1
        if basic:
            for bleh in self.vertices:

                lst = bleh.getSourceTo()

                count += len(lst)
        return count   
    
    def targetedVacc(self):
        dct = self.makeVertHubDict()
        keys = dct.keys()
        keys.sort(key=lambda x : x.hubScore)
        susLst, vaccLst = keys[0:int(self.numVerts*(1-self.percentVacc))], keys[int(self.numVerts*(1-self.percentVacc)):]
        infected = random.randrange(0,len(susLst))
        #print("HERE IN TARGETED VACC")
        susLst[infected].initialStatus("I")
        for vert in vaccLst:
            vert.initialStatus('V')
        return vaccLst
        
    def totalReset(self):
        self.resetCounts()
        self.resetLists()
        self.resetBools()
        self.resetGraph()           

    
    def twoWayConnect(self,vert1,vert2,connprob):
        if random.random() < connprob: # check to see if this number 
            if vert1 in vert2.getSourceTo():
                pass
            else:
                vert1.addSource(vert2)
                vert2.addDest(vert1)
                ed = edge.Edge(vert1,vert2,self.p) #or use some distribution counter (adjust edge)
                vert2.addSource(vert1)
                vert1.addDest(vert2)
                ed1 = edge.Edge(vert2,vert1,self.p) #or use some distribution counter

                vert2.addEdge(ed)
                self.addEdge(ed)            

                vert1.addEdge(ed1)
                self.addEdge(ed1)

    def update(self):
        self.countAndUpdateStatuses()
        self.updateLists()
        self.checkHighConcentrationEpi()
        while self.getI() != 0:
            self.countAndUpdateStatuses()
            self.updateLists()
            self.checkHighConcentrationEpi()

        self.checkFinalEpi()

    def updateLists(self):
        '''Helper function for update'''
        self.ilist = self.ilist + [self.numI] 
        self.rlist = self.rlist + [self.numR]
        self.iandrlist = self.iandrlist + [self.numI+self.numR]         
        
    def vaccinate(self):
        if self.random: self.randomVacc()
        else: self.targetedVacc()

    def __getitem__(self,i):
        return self.vertices[i]


def main():
    p = pm.Params(8,.1,1000,.01,0,random = False) #k,p,N,rho,nu
    g = Graph(p,clustered = True)
    print(g.getClusteringCoefficient())
    

if __name__ == "__main__":
    main()

