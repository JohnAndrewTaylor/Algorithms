# Graph Algorithms

## Generic Search Algorithm
This file countains a search function which can do a **Breadth First Search**, **Depth First Search**, **Dijkstra's / Uniform Cost Search**, and __A* Search__. The search parameter in the search function designates which type of search to perform, which is determined by the data structure used in the Generic Search Algorithm.

## Supporting Code
The files `utilData` and `utilGraph` provide foundational data structures and objects required to run the algorithms provided. The data structures provided are **Stack**, **Queue**, and **PriorityQueue**. The graph objects defined are **Graph**, **Edge**, and **Vertex**. A **Vertex** contains a label and an **Edge** contains the two vertices that define it and its weight (automatically set to 1). A **Graph** contains a list of vertices and edges that define it and a dictionary of neighbors to be able to provide a list of neighboring vertices along with the weight of their connecting **Edge** for any given **Vertex**.
