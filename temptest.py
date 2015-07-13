def calculateP(numConnections,k,r):
    p =1-( (1-(r/numConnections))**(1./k))
    return p

print(calculateP(25.33,4,5.85))
print(calculateP(25.33,6,5.85))
print(calculateP(25.33,4,10.65))
print(calculateP(25.33,6,10.65))
print(calculateP(25.33,4,14.4))
print(calculateP(25.33,6,14.4))
    