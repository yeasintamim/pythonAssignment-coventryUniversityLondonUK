from collections import defaultdict
import sys

class Graph():
    def __init__(self, size):
        self.edges = defaultdict(list)                                      #dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}                                                   #dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size                                                    #assign the size
        self.dist = []                                                      #empty list of the distances
        for i in range(size):                                               #for loop of the size
            self.dist.append(sys.maxsize)                                   #adding the max size to the distance
        self.previous = []                                                  #empty dictionary for the previous
        for i in range(size):                                               #for loop of the range
            self.previous.append(None)                                      #adding nothing to the previous
            
    def add_edge(self, from_node, to_node, weight):                         #bidirectional
        self.edges[from_node].append(to_node)                               #adding the node to the edge
        self.edges[to_node].append(from_node)                               #adding the previous node to the edge
        self.weights[(from_node, to_node)] = weight                         #assigning the nodes to the weight
        self.weights[(to_node, from_node)] = weight                         #assigning the nodes to the weight

    def findSmallestNode(self): 
        smallest = self.dist[self.getIndex(self.Q[0])]                      #assigning the shortest distance node
        result = self.getIndex(self.Q[0])                                   #assigning the shortest node
        node = self.dist                                                    #assinging the distance
        for i in range(len(self.dist)):                                     #for loop of the length of distance
            if self.dist[i] < smallest:                                     #if the distance is less than smallest
                if node in self.Q:                                          #if the node is part of Q
                    smallest = self.dist[i]                                 #assigning the dist to smallest
                    result = self.getIndex(node)                            #creating the result
        return result
            
    def getIndex(self, neighbour):
        for i in range(len(self.unpoppedQ)):                                #for loop of length of the unpopped
            if neighbour == self.unpoppedQ[i]:                              #if the previous is equal to unpopped
                return i

    def getPopPosition(self, uNode):
        result = 0                                                          #creating an empty result
        for i in range(len(self.Q)):                                        #for loop of the length of Q
            if self.Q[i] == uNode:                                          #if Q is equal to input node
                return i
        return result

    def getUnvisitedNodes(self, uNode):
        resultList = []                                                     #empty list of results
        allNeighbours = self.edges[uNode]                                   #assigning the edges of input nodes to the neighbours
        for neighbour in allNeighbours:                                     #for loop of neighbours in all of the neighbours
            if neighbour in self.Q:                                         #if the neighbour is part of Q
                resultList.append(neighbour)                                #adding the neighbour to the result list
        return resultList          

    def dijsktra(self, start, end):                                         
        self.Q = []                                                         #empty list for Q
        for key in self.edges:                                              #for loop of the key in the edges
            self.Q.append(key)                                              #adding the key to Q
        for i in range(len(self.Q)):                                        #for loop of length of Q
            if self.Q[i] == start:                                          #if Q is equal to 0
                self.dist[i] = 0                                            #0 is assigned to the distance
        self.unpoppedQ = self.Q[0:]                                         #assigning the first Q to unpopped
                     
        while self.Q:                                                       #while loop of Q                                                       
            u = self.findSmallestNode()                                     #assigning the smallest node to u
            if self.dist[u] == sys.maxsize:                                 #if the fistance of u is equal to the maximum
                break                                           
            if self.unpoppedQ[u] == end:                                    #if the unpopped of u is equal to the end
                break
            uNode = self.unpoppedQ[u]                                       #assigning the unpopped Q to uNode

            for i in self.edges[uNode]:                                     #for loop of edges of uNode
                if i in self.Q:                                             #if edge in Q
                    if i in self.getUnvisitedNodes(uNode):                  #if the edge is part of univisited nodes
                        if int (self.dist[self.unpoppedQ.index(uNode)]) + self.weights[(uNode,i)] < self.dist[self.unpoppedQ.index(i)]:#if the weight and unpopped is less than the distance of unpopped
                            self.dist[self.unpoppedQ.index(i)] = int (self.dist[self.unpoppedQ.index(uNode)]) + self.weights[(uNode,i)]#assigning the distance and weight to distance
                            self.previous[self.unpoppedQ.index(i)] = uNode  #assigning the previous to uNode
            self.Q.pop(self.Q.index(uNode))
        
        weight = self.dist[self.unpoppedQ.index(uNode)+1]                   #assigning the distance of uNode to the weight
        shortest_path = []                                                  #empty list of shortest path
        shortest_path.insert(0, end)                                        #inserting the start and end to the shortest path
        u = self.getIndex(end)                                              #assigning the index to u

        while self.previous[u] != None:                                     #while loop of the previous not being empty
            shortest_path.insert(0, self.previous[u])                       #adding the previous of u to the shortest path
            u = self.getIndex(self.previous[u])                             #assigning the previous u of index to u
        output = (shortest_path,weight)                                     #assigning the weight of shortest path to output
        return output

graph = Graph(8)                                                            #the number of nodes of the graph
edges =[                                                                    #the weights of the edges in a list of tuples in a list
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]
    
for edge in edges:                                                          #for loop of the edges
    graph.add_edge(*edge)                                                   #adding the eddges to the graph size
print(graph.dijsktra('O', 'T'))                                             #printing the path