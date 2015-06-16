__author__ = 'elleer02'
import graph
RandIdict = {}
k = 1
for x in range(25):
    g = graph.Graph(k,.3,0,0)
    g.makeVertices(1000)
    g.makeConnections(.005)
    g.update()
    r = g.calculateR()
    i = g.getR()
    RandIdict[r] = [i/1000]
    k += 1


p = .01
for x in range(9):
    g = graph.Graph(5,p,0,0)
    g.makeVertices(1000)
    g.makeConnections(.005)
    g.update()
    r = g.calculateR()
    i = g.getR()
    RandIdict[r] = [i/1000]
    p += .05

k = 1
for x in range(25):
    g = graph.Graph(k,.3,0,0)
    g.makeVertices(2000)
    g.makeConnections(.005)
    g.update()
    r = g.calculateR()
    i = g.getR()
    RandIdict[r] = [i/2000]
    k += 1


p = .01
for x in range(9):
    g = graph.Graph(5,p,0,0)
    g.makeVertices(2000)
    g.makeConnections(.005)
    g.update()
    r = g.calculateR()
    i = g.getR()
    RandIdict[r] = [i/2000]
    p += .05

k = 1
for x in range(25):
    g = graph.Graph(k,.3,0,0)
    g.makeVertices(500)
    g.makeConnections(.005)
    g.update()
    r = g.calculateR()
    i = g.getR()
    RandIdict[r] = [i/500]
    k += 1


p = .01
for x in range(9):
    g = graph.Graph(5,p,0,0)
    g.makeVertices(500)
    g.makeConnections(.005)
    g.update()
    r = g.calculateR()
    i = g.getR()
    RandIdict[r] = [i/500]
    p += .05

print(RandIdict)
