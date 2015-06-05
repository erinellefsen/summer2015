import graph

graphLst = []
for i in range(10):
    g = graph.Graph(2, .2, 0, .01) #k,p,r,%infected
    g.makeVerticesAndConnections(10,.1)        #prob they are connected
    graphLst.append(g)

lstLst = []
for i in range(10):
    lst = []
    lstLst.append(lst)


for index in range(len(graphLst)):
    g = graphLst[index]

    for i in range(10):
        highEpi = 0
        finalEpi = 0
        g.update(10)            #number of repetitions, num trials
        if g.getHighEpi():
            highEpi +=1
        if g.getFinalEpi():
            finalEpi +=1
        highPercent = highEpi
        finalPercent = finalEpi
        lstLst[i].append((highPercent,finalPercent))
        g.resetGraph()

for i in lstLst:
    print(i, "\n\n")

#What am I trying to do?
'''  
For 1000 random graphs, are there any that are obnoxiously resilient to infection?
Matrix A: m*n Where m = Number of tests to find likelihood of epidemic. 
                    n = Number of Graphs tested for epidemics
Average the likelihood in each column to see if there are any graphs that have very extreme rates of infection.
For each location in the matrix Aij, we need to find the likelihood of infection we need to find the likelihood 
of epidemic for trial i, graph j. 
'''


'''
For small groups we would more likely find structures that inhibit the spread.
Perhaps these small structures could be found in larger networks, and these small structures could be the reason that 
larger networks have certain rates of epidemic.
'''
