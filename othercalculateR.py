__author__ = 'elleer02'

import graph
import statistics
vaccination = 0
while vaccination < 200:
    Rlist =[]
    for things in range(100):
        g = graph.Graph(5,.5,0,vaccination)
        g.makeVertices(200)
        g.makeConnections(.02)
        Rlist = Rlist + [g.calculateR()]

    x = statistics.mean(Rlist)
    y = statistics.pstdev(Rlist,x)
    z = statistics.pvariance(Rlist,x)

    print(vaccination,'mean',x,)
    #print('standard dev',y)
    #print('variance',z)
    vaccination += 10