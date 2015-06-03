import random
class Disease:
    def __init__(self, k, p , r,):
        self.duration = k
        self.contagion = p
        self.recovprob = r
        self.infectiontime = 0
    def timeChange(self):
        self.infectiontime += 1
    def checkRecovered(self):
        if self.infectiontime > self.duration or random.random() < self.recovprob:
            return True
        else:
            return False
    def checkSpread(self):
        if random.random() < self.contagion:
            return True
        else:
            return False
    def getDuration(self):
        return self.duration
    def getContagion(self):
        return self.contagion
    def getRecovery(self):
        return self.recovery
    def getInfection(self):
        return self.infectiontime