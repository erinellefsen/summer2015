import cPickle as pickle
import graph 
import tank
import params as pm
import minimalGraph as mg
import random 
import sys

pop = 4000
vaccLst = [0,.2,.4,.6,.8]
print("1% Completed")
accu = 0
for ind in range(1):
    '''    
    with open('CHANGE_NAME--RANDOM'+str(ind)+'.pkl', 'wb') as output:
        pickler = pickle.Pickler(output,-1)
        for inde in range(3):
            k=1
            p=.05
            for index in range(13):
                rho = random.uniform(0.0015,0.0035)
                prams = pm.Params(k,.1,pop,rho,vaccLst[ind]*pop,targeted= False)
                g = graph.Graph(prams,random = True)
                g.update()
                r = g.calculateR(True) #basic = true
                i = g.getR()/float(pop)
                z = g.getEdges()
                c = g.getClusteringCoefficient()
                minG = mg.MinimalGraph(prams,r,i,c,z,kind="random")
                tp1 = tank.Tank(minG)
                pickler.dump(tp1)
                k += 1

            for index in range(27):
                rho = random.uniform(0.0015,0.004)
                prams = pm.Params(3,p,pop,rho,vaccLst[ind]*pop,targeted = False)
                g = graph.Graph(prams,random=True)
                g.update()
                r = g.calculateR(True) #basic = true
                i = g.getR()/float(pop)
                z = g.getEdges()
                c = g.getClusteringCoefficient()

                minG = mg.MinimalGraph(prams,r,i,c,z,kind="random")
                tp1 = tank.Tank(minG)
                pickler.dump(tp1)

                p+= .05
    output.close()
    print(str((ind+1)*20)+"% Completed")
    '''
    with open(str(sys.argv[2])+"/"+str(sys.argv[1])+".pkl", 'wb') as output1:
        pickler = pickle.Pickler(output1,-1)
        for inde in range(90):
            p = random.uniform(float(sys.argv[3]),float(sys.argv[4]))
            prams = pm.Params(5,p,pop,.123,float(sys.argv[3])*pop,targeted= False)

            g = graph.Graph(prams,clustered=True)
            g.update()
            r = g.calculateR(True) #basic = true
            i = g.getR()/float(pop)
            z = None#g.getEdges()
            c = g.getClusteringCoefficient()
            minG = mg.MinimalGraph(prams,r,i,c,z,kind="clustered")
            tp1 = tank.Tank(minG)
            pickler.dump(tp1)
        output1.close()
#'''















