import cPickle as pickle
import graph 
import tank
import params as pm
import minimalGraph as mg

pop = 5000
vaccLst = [0,.2,.4,.6,.8]
for ind in range(5):    
    with open('CHANGE_NAME--RANDOM'+str(ind)+'.pkl', 'wb') as output:
        pickler = pickle.Pickler(output,-1)
        for inde in range(4):
            k=1
            p=.05
            for index in range(15):

                j = pm.Params(k,.1,pop,.002,vaccLst[inde]*pop,targeted= False)
                g = graph.Graph(j,random = True)
                g.update()
                r = g.calculateR(True) #basic = true
                i = g.getR()/float(pop)
                z = g.getEdges()
                c = g.getClusteringCoefficient()
                minG = mg.MinimalGraph(j,r,i,c,z,kind="random")
                tp1 = tank.Tank(minG)
                pickler.dump(tp1)
                k += 1

            for index in range(35):

                j = pm.Params(3,p,pop,.002,vaccLst[inde]*pop,targeted = False)
                g = graph.Graph(j,random=True)
                g.update()
                r = g.calculateR(True) #basic = true
                i = g.getR()/float(pop)
                z = g.getEdges()
                c = g.getClusteringCoefficient()

                minG = mg.MinimalGraph(j,r,i,c,z,kind="random")
                tp1 = tank.Tank(minG)
                pickler.dump(tp1)

                p+= .05
    output.close()
    with open('CHANGE_NAME--CLUSTERED'+str(ind)+'.pkl', 'wb') as output1:
        pickler = pickle.Pickler(output1,-1)
        for inde in range(4):
            k=1
            p=.05
            vaccination = 0
            for index in range(15):

                j = pm.Params(k,.1,pop,.002,vaccLst[inde]*pop,targeted= False)
                g = graph.Graph(j,clustered=True)
                g.update()
                r = g.calculateR(True) #basic = true
                i = g.getR()/float(pop)
                z = g.getEdges()
                c = g.getClusteringCoefficient()
                minG = mg.MinimalGraph(j,r,i,c,z,kind="random")
                tp1 = tank.Tank(minG)
                pickler.dump(tp1)
                k += 1

            for index in range(35):

                j = pm.Params(3,p,pop,.002,vaccLst[inde]*pop,targeted = False)
                g = graph.Graph(j,clustered=True)
                g.update()
                r = g.calculateR(True) #basic = true
                i = g.getR()/float(pop)
                z = g.getEdges()
                c = g.getClusteringCoefficient()

                minG = mg.MinimalGraph(j,r,i,c,z,kind="random")
                tp1 = tank.Tank(minG)
                pickler.dump(tp1)

                p+= .05
    output1.close()