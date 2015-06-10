__author__ = 'elleer02'
import graph
import statistics


Rlist =[]
for things in range(50):

    g = graph.Graph(8,.9,0,0)
    g.makeVertices(5000)
    g.makeConnections(.001)
    Rlist = Rlist + [g.calculateR(True)]

x = statistics.mean(Rlist)
y = statistics.pstdev(Rlist,x)
z = statistics.pvariance(Rlist,x)

print(Rlist)
print('mean',x,)
print('standard dev',y)
print('variance',z)
