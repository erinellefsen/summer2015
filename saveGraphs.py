    for x in range(numTrials):
        g = graph.Graph(prams)
        g.update()
        r = g.calculateR(True) #basic = true
        i = g.getR()
        #print(i)
        lst.append([r, float(i)/float(prams.numVerts),prams.numVerts])
        #print(lst)
        #dct[r]=[float(i)/float(1000)]
        if accK: prams.k+=1
        if accP: prams.p+=.01  
    

for color in colorlist:
    acc =0
    RandIlst = []
    '''
    a = pram.Params(0,.05,1000,.005,vaccination*1000,random = False)
    b = pram.Params(3,0,1000,.005,vaccination*1000,random = False)   
    c = pram.Params(0,.05,2000,.0025,vaccination*2000,random = False)
    d = pram.Params(3,0,2000,.0025,vaccination*2000,random = False) #k,p,N,rho,nu
    e = pram.Params(0,.05,500,.01,vaccination*500,random = False)
    f = pram.Params(3,0,500,.01,vaccination*500,random = False)
    h = pram.Params(0,.05,1500,.003,vaccination*1500,random = False)
    l = pram.Params(3,0,1500,.003,vaccination*1500,random = False)
    '''
    j = pram.Params(0,.05,3000,.001,vaccination*3000,random = False)
    m = pram.Params(3,0,3000,.001,vaccination*3000,random = False)
    
    lst = [j,m]
    trialLst= [10,30]
    boolLst = [True,False]
    for i in range(len(lst)):
        rVersesPropInf(lst[acc],trialLst[acc%2],RandIlst,accK=boolLst[acc%2],accP=boolLst[(acc+1)%2]) 
        acc += 1
    print(RandIlst)
    RandILst = []
    vaccination +=.2