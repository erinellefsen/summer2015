def main():
    count = 0
    for i in range(5):

        A = vertexclass.Vertex("A",disease.Disease(3,.45,.1))
        B = vertexclass.Vertex("B",disease.Disease(3,.45,.1))
        C = vertexclass.Vertex("C",disease.Disease(3,.45,.1))
        D = vertexclass.Vertex("D",disease.Disease(3,.45,.1))
        E = vertexclass.Vertex("E",disease.Disease(3,.45,.1))
        F = vertexclass.Vertex("F",disease.Disease(3,.45,.1))
        G = vertexclass.Vertex("G",disease.Disease(3,.45,.1))
        H = vertexclass.Vertex("H",disease.Disease(3,.45,.1))
        I = vertexclass.Vertex("I",disease.Disease(3,.45,.1))

        vertLst = [A,B,C,D,E,F,G,H,I]

        A.addNeighbor(B)
        A.addNeighbor(C)
        B.addNeighbor(D)
        B.addNeighbor(G)
        C.addNeighbor(E)
        C.addNeighbor(F)
        D.addNeighbor(F)
        E.addNeighbor(H)
        F.addNeighbor(H)
        F.addNeighbor(I)
        H.addNeighbor(I)
        A.initialInfect()
        for i in range(5):
            for i in vertLst:
                i.update()
            print(vertLst)

        count += 1
        print("End case ",count)
