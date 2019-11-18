# Generic Search Algorithm
# John Andrew Taylor, 2019
# General purpose classes defining graphs, edges, vertices.
# The search will return a path from the start to the goal state
# The algorithm can handle disconnected points (empty path)
# The solutions for BFS and DFS are not guaranteed to be optimal

import utilData, utilGraph

def search(graph, start, goal, search = 1, heuristic = {}):
    
    if (search == 1):
        #Algorithm is DFS
        openList = utilData.Stack()
    if (search == 2):
        #Algorithms is BFS
        openList = utilData.Queue()
    if (search == 3):
        #Algorithm is Dijkstra or UCS
        openList = utilData.PriorityQueue()
    if (search == 4):
        #Algorithm is A* or A-Star
        openList = utilData.PriorityQueue()
        #Warning: precomputed heuristic dictionary must be provided
        #For any gven vertex label, a number must be returned

    current = start
    closedList = []
    path = []
    #The parents dictionary is used to keep track of the parent node of each vertex
    #This is required to be able to return the path after discovering a solution
    parents = {}

    while not (current == goal):
        closedList.append(current)
        successors = graph.getNeighbors(current)
        for s in successors:
            if not s[0] in closedList:
                parents[s[0].getLabel()] = current
                if (search < 3):
                    openList.push(s[0])
                else:
                    cost = s[1]
                    if s[0].getLabel() in heuristic:
                        cost += heuristic.get(s[0].getLabel())
                    openList.push(s[0], cost)
        while current in closedList:
            if not openList.isEmpty():
                current = openList.pop()
            else:
                #If the openList is empty, then there is no path (disconnected)
                return path

    #Finding the path from the goal to the start and adding in reverse order
    while not current == start:
        path.insert(0, (parents.get(current.getLabel()),current))
        current = parents.get(current.getLabel())
    return path

def main():
    #g = utilGraph.Graph(["A", "B", "C"], [("A","B"), ("B","C")])
    g = utilGraph.Graph([1,2,3,4,5], [(1,2,5),(2,3,6),(3,4,2),(1,3,15)])
    print(search(g, utilGraph.Vertex(1), utilGraph.Vertex(5), search = 3))

if __name__ == '__main__':
    main()
