class MinimalGraph():
    def __init__(self,params,r_0,propI,clusteringNum,edges=None,kind =None):
        self.prams = params
        self.r_0 = r_0
        self.propI = propI
        self.edges = edges
        self.clusteringNum=clusteringNum
        self.kind = kind
        
    def __str__(self):
        return self.kind+ "\t "+str(self.clusteringNum)+ "\t "+str(self.r_0)+"\t " +str(self.propI)