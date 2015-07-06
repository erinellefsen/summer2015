class Params():
    def __init__(self,k,p,numVert,connectionProb,numVacc,r=0,targeted = False):
        self.k=k
        self.p=p
        self.r=r
        self.numVerts=numVert
        self.connectionProb=connectionProb
        self.numVacc = numVacc
        self.percentVacc = float(numVacc)/float(numVert)
        self.targeted = targeted
        
        
        
     