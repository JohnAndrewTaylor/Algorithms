# Graph Utilities
# John Andrew Taylor, 2019
# General purpose classes defining graphs, edges, vertices.
#

class Graph:
    def __init__(self, vertices, edges):
        self.vertexList = []
        self.edgeList = []
        
        for v in vertices:
            self.vertexList.append(Vertex(v))
        for e in edges:
            self.edgeList.append(Edge(e))

        # Initialize vertex neighbors dictionary
        # Uses vertex label to return a list of Vertex objects
        self.neighborsDict = {}
        for v in self.vertexList:
            neighbors = []
            for e in self.edgeList:
                if (e.getStart().getLabel() == v.getLabel()):
                    neighbors.append(e.getEnd())
                if (e.getEnd().getLabel() == v.getLabel()):
                    neighbors.append(e.getStart())
            self.neighborsDict[v.getLabel()] = neighbors

    def __str__(self):
        return "Vertices: %s ||| Edges: %s" % (self.vertexList, self.edgeList)

    def __repr__(self):
        return self.__str__()

    def getEdges(self):
        return self.edgeList

    def getVertices(self):
        return self.vertexList

    def getNeighbors(self, v):
        return self.neighborsDict.get(v.getLabel())

class Edge(Graph):
    def __init__(self, tupleEdge):
        self.startVertex = Vertex(tupleEdge[0])
        self.endVertex = Vertex(tupleEdge[1])
        if len(tupleEdge) == 3:
            self.weight = tupleEdge[2]
        else:
            self.weight = 1

    def __str__(self):
        return "{(%s,%s) weight:%s}" % (self.startVertex.getLabel(),self.endVertex.getLabel(),self.getWeight())

    def __repr__(self):
        return self.__str__()

    def getTuple(self):
        return (self.startVertex, self.endVertex)

    def getStart(self):
        return self.startVertex

    def getEnd(self):
        return self.endVertex

    def getWeight(self):
        return self.weight

class Vertex(Graph):
    def __init__(self, label):
        self.vertexLabel = label

    def __str__(self):
        return "%s" % (self.vertexLabel)

    def __repr__(self):
        return self.__str__()

    def getLabel(self):
        return self.vertexLabel
