import cPickle as pickle
import graph 
import tank
import params as pm
p1 = pm.Params(3,.1,4000,.05,0) #k,p,N,rho,nu
p2 = pm.Params(1,.9, 1500,.5,0) 
g1 = graph.Graph(p1)
print(g1.numVerts)
g2 = graph.Graph(p2)
print(g2.numVerts)
with open('testPickledObjs.pkl', 'wb') as output:
    pickler = pickle.Pickler(output,-1)
    print("created")
    tp1 = tank.Tank(g1)
    tp2 = tank.Tank(g2)
    print("tanked")
    pickler.dump(tp1)
    print("dump1")
    pickler.dump(tp2)
    print("dump2")
    output.close()
print("stored")
with open('testPickledObjs.pkl', 'rb') as inputFile:
    unPickler = pickle.Unpickler(inputFile)
    pt1 = unPickler.load()
    g6 = pt1.lift()
    print("lift1")
    pt2 = unPickler.load()
    g7 = pt2.lift()
    print("lift2")
    print(g6.numVerts)
    print(g7.numVerts)
    inputFile.close()
#        def copyVertices(self,source,dest):
#        '''This function saves the first state of the graph, after vertices and connections have been made'''
#        source_tank = tank.Tank(source)
#        dest_tank = copy.deepcopy(source_tank)
#        source = source_tank.lift()
#        dest = dest_tank.lift()
#        return dest  


'''
R_0
Params
prop infected
clustering coefficient?
list of vertices/edges
'''