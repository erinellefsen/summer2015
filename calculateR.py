__author__ = 'elleer02'
import vertexclass
import graph
import disease
import random

for things in range(10):
    g = graph.Graph(8,.9,0,50)
    g.makeVertices(300)
    g.makeConnections(.01)
    print(g.calculateR())