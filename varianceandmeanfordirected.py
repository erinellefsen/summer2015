__author__ = 'elleer02'
import graph
import statistics
import params
connlist = []
Rlst = []
for x in range(1000):
    prams = params.Params(8,.1,200,.02,0)
    g = graph.Graph(prams)
    lst = g.getEdges()
    r = g.calculateR()
    connlist = connlist + [len(lst)/200]
    Rlst = Rlst + [r]

mea = statistics.mean(connlist)
var = statistics.variance(connlist,mea)

mea2 = statistics.mean(Rlst)
var2 = statistics.variance(Rlst,mea2)
print(mea2, var2)