import cPickle as pickle
import graph 
import tank
import params as pm
import minimalGraph as mg
import random 
import sys

pop = 5000
fileName = sys.argv[1]
dirName = sys.argv[2]
vaccLevel = sys.argv[3]
p_low = sys.argv[4]
p_high = sys.argv[5]
graphType = sys.argv[6]

if graphType == "-c":

    with open(str(dirName)+"/"+str(fileName)+".pkl", 'wb') as output1:
        pickler = pickle.Pickler(output1,-1)
        for inde in range(90):
            k = 5
            p = random.uniform(float(p_low),float(p_high))
            N = pop
            rho = 0 #rho doesn't matter for clustered
            nu = float(vaccLevel)*pop
            prams = pm.Params(k,p,N,rho,nu,targeted= False) 
           
            g = graph.Graph(prams,clustered=True)
            g.update()
            r = g.calculateR(True) #basic = true
            rPrime = g.calculateR()
            i = g.getR()/float(pop)
            iPrime = (g.getR() - 1)/float(N-nu) #This is the proportion infected out of the original number of susceptibles.
            z = None#g.getEdges()
            c = g.getClusteringCoefficient()

            minG = mg.MinimalGraph(prams,r,rPrime,i,iPrime,c,z,kind="clustered")
            tp1 = tank.Tank(minG)
            pickler.dump(tp1)
        output1.close()
        
elif graphType == "-r":

    with open(str(dirName)+"/"+str(fileName)+".pkl", 'wb') as output1:
        pickler = pickle.Pickler(output1,-1)
        for inde in range(90):
            k = 5
            p = random.uniform(float(p_low),float(p_high))
            N = pop
            rho = .005066
            nu = float(vaccLevel)*pop
            prams = pm.Params(k,p,N,rho,nu,targeted= False) #changed p to 1

            g = graph.Graph(prams,random=True)
            g.update()
            r = g.calculateR(True) #basic = true
            rPrime = g.calculateR()
            i = g.getR()/float(pop)
            iPrime =(g.getR() - 1)/float(N-nu)#get proportion of initial infected individuals.
          
            z = None#g.getEdges()
            c = g.getClusteringCoefficient()
          
            minG = mg.MinimalGraph(prams,r,rPrime,i,iPrime,c,z,kind="random")
            tp1 = tank.Tank(minG)
            pickler.dump(tp1)
        output1.close()
else:
     raise ValueError("graphType was neither -r or -c")