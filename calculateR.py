__author__ = 'elleer02'
import graph
import statistics


Rlist =[]

for things in range(100000):


    p = params.Params(8,.5,100,.4,0)
    g = graph.Graph(p)
    Rlist = Rlist + [g.calculateR()]

x = statistics.mean(Rlist)
y = statistics.pstdev(Rlist,x)
z = statistics.pvariance(Rlist,x)

print('mean',x,)

print('variance',z)
