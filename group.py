
    

class Group:
    def __init__(self, id, propIncl, probOfConn, p):
        self.Id = id 
        self.PropIncl = propIncl
        self.probOfConn = probOfConn
        self.members = []
        self.p = p
        
    def addMember(self, member):
        self.members = self.members + [member]
        
    def getMembers(self):
        return self.members
    
    def getId(self):
        return self.Id
    
    def getPropIncl(self):
        return self.PropIncl
    
    def getProbOfConn(self):
        return self.probOfConn
    