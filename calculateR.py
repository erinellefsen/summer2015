__author__ = 'elleer02'
import graph
import statistics

vaccination = 0
while vaccination <=0:
    Rlist =[]
    connList = []
    for things in range(100000):

        g = graph.Graph(8,.3,0,vaccination)
        g.makeVertices(100)
        connList = connList + [g.makeConnections(.01)]
        Rlist = Rlist + [g.calculateR()]

    x = statistics.mean(Rlist)
    y = statistics.pstdev(Rlist,x)
    z = statistics.pvariance(Rlist,x)
    avgConn = sum(connList)/len(connList)

    print(avgConn)
    print('mean',x,)
    #print('standard dev',y)
    print('variance',z)
    vaccination += 10