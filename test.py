from graph import *
import tank
import copy
def copyVertexList(l1,l2):
    l2 = []
    for i in l1:
        l2.append(copy.deepcopy(i)) #WHY DIDN'T THIS WORK?!?!?

def copyVertices(self,source,dest):
    '''This function saves the first state of the graph, after vertices and connections have been made'''
    source_tank = tank.Tank(source)
    dest_tank = copy.deepcopy(source_tank)
    source = source_tank.lift()
    dest = dest_tank.lift()
    return dest
def test1():
    g = Graph(10,.4,0,.5) #steps,contagiousness,
    g.makeVerticesAndConnections(400,.07)
    #copyVertexList(g.vertices,g.original)
    print("1 ",g.vertices)
    print("2 ",g.original)
    g.update(100)

    #g.resetGraph()
    print("3 ",g.vertices)
    print("4 ",g.original)
    
def tankTest():
    g = Graph(10,.4,0,.5) #steps,contagiousness,
    g.makeVerticesAndConnections(10,.07)
    print(g.vertices)
    source_tank = tank.Tank(g.vertices)
    dest_tank = copy.deepcopy(source_tank)
    g.vertices = source_tank.lift()
    g.original = dest_tank.lift()
    print(g.vertices)
    #print(g.original)
    g.update(10)
    print(g.vertices)
    print(g.original)
    #print("2 ",g.original)
    #g.resetGraph()
    #print("3 ",g.vertices)
    
    
def main():
    test1()
    #x = tank.Tank([1,2,3,4,5,6,7])
    #print(x)
if __name__ == "__main__":
    main()