import cPickle as pickle
import graph 
import lattice
import tank
import params as pm
from datetime import datetime
import minimalGraph as mg

initial = datetime.now()

p1 = pm.Params(3,.1,4000,.05,0) #k,p,N,rho,nu
#p2 = pm.Params(1,.9, 1500,.5,0) 
g1 = graph.Graph(p1,random=True)
#g2 = graph.Graph(p2)
t1 = datetime.now()
print "created ",t1-initial

g1.update()
#g2.update()
t2 = datetime.now()
print "update ",t2-t1
x = g1.calculateR()
y = g1.getR()/g1.numVerts
z = g1.getEdges()
print(len(z))
minG = mg.MinimalGraph(p1,x,y,4,z)
#print(g2.numVerts),
print "before ", x
with open('testPickledObjs.pkl', 'wb') as output:
    pickler = pickle.Pickler(output,-1)

    tp1 = tank.Tank(minG)
    #tp2 = tank.Tank(g2)
    t3 = datetime.now()
    print "tanked ",t3-t2
    
    pickler.dump(tp1)
    #pickler.dump(tp2)
    t4 = datetime.now()
    print "dumped ", t4-t3 
    
    output.close()

with open('testPickledObjs.pkl', 'rb') as inputFile:
    unPickler = pickle.Unpickler(inputFile)
    pt1 = unPickler.load()
    #pt2 = unPickler.load()
    t5=datetime.now()
    print "loaded ",t5-t4
    
    g6 = pt1.lift()
    #g7 = pt2.lift()
    t6 = datetime.now()
    print "lifted ",t6-t5
    
    #print(g6.numVerts)
    #print(g7.numVerts)
    inputFile.close()
    
    print(len(g6.edges))
    g = g6.expand()
    print "after " ,g.calculateR()
#        def copyVertices(self,source,dest):

#        source_tank = tank.Tank(source)
#        dest_tank = copy.deepcopy(source_tank)
#        source = source_tank.lift()
#        dest = dest_tank.lift()
#        return dest  ''' 
                       

#R_0
#Params
#prop infected
#clustering coefficient?
#list of vertices/edges
