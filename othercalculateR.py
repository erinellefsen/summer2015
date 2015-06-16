__author__ = 'elleer02'

import graph
import statistics
vaccination = 0
#while vaccination < 200:
Rlist =[]
for things in range(500):
    g = graph.Graph(8,.3,0,vaccination)
    g.makeVertices(10000)
    g.makeConnections(.01)
    Rlist = Rlist + [g.calculateR()]

x = statistics.mean(Rlist)
y = statistics.pstdev(Rlist,x)
z = statistics.variance(Rlist,.932928381)

print(vaccination,'mean',x,)
print('standard dev',y)
print('variance',z)
    #vaccination += 10