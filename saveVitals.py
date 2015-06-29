import cPickle as pickle
import graph 
import tank
import params as pm
import minimalGraph as mg

with open('CHANGE_THIS_FILE_NAME.pkl', 'wb') as output:
    pickler = pickle.Pickler(output,-1)
    for i in range(4):
        k=1
        p=.05
        vaccination = 0
        for i in range(15):

            j = pm.Params(k,.1,3000,.002,vaccination*3000,targeted= False)
            g = graph.Graph(j)
            g.update()
            r = g.calculateR(True) #basic = true
            i = g.getR()
            z = g.getEdges()
            c = g.getClusteringCoefficient()
            minG = mg.MinimalGraph(j,r,i,z)
            tp1 = tank.Tank(minG)
            pickler.dump(tp1)





            k += 1
        for i in range(30):

            j = pm.Params(3,p,3000,.002,vaccination*3000,targeted = False)
            g = graph.Graph(j)
            g.update()
            r = g.calculateR(True) #basic = true
            i = g.getR()
            z = g.getEdges()
            c = g.getClusteringCoefficient()

            minG = mg.MinimalGraph(j,r,i,z)
            tp1 = tank.Tank(minG)
            pickler.dump(tp1)

            p+= .05

    output.close()