from collections import defaultdict
import sys

class Graph():                                                             
    def __init__(self, size):
        self.edges = defaultdict(list)                                      #dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}                                                   #dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size                                                    #assign the size
        self.dist = []                                                      
        for i in range(size):                                              
            self.dist.append(sys.maxsize)                                   
        self.previous = []                                                  
        for i in range(size):                                               
            self.previous.append(None)                                      
            
    def add_edge(self, from_node, to_node, weight):                         #bidirectional
        self.edges[from_node].append(to_node)                               
        self.edges[to_node].append(from_node)                               
        self.weights[(from_node, to_node)] = weight                        
        self.weights[(to_node, from_node)] = weight                         

    def findSmallestNode(self): 
        smallest = self.dist[self.getIndex(self.Q[0])]                      
        result = self.getIndex(self.Q[0])                                   
        node = self.dist                                                    
        for i in range(len(self.dist)):                                     
            if self.dist[i] < smallest:                                     
                if node in self.Q:                                          
                    smallest = self.dist[i]                                 
                    result = self.getIndex(node)                            
        return result
            
    def getIndex(self, neighbour):
        for i in range(len(self.unpoppedQ)):                                
            if neighbour == self.unpoppedQ[i]:                              
                return i

    def getPopPosition(self, uNode):
        result = 0                                                          #creating an empty result
        for i in range(len(self.Q)):                                        
            if self.Q[i] == uNode:                                          
                return i
        return result

    def getUnvisitedNodes(self, uNode):
        resultList = []                                                     
        allNeighbours = self.edges[uNode]                                   
        for neighbour in allNeighbours:                                     
            if neighbour in self.Q:                                         
                resultList.append(neighbour)                                
        return resultList          

    def dijsktra(self, start, end):                                         
        self.Q = []                                                        
        for key in self.edges:                                              
            self.Q.append(key)                                              
        for i in range(len(self.Q)):                                        
            if self.Q[i] == start:                                          
                self.dist[i] = 0                                            
        self.unpoppedQ = self.Q[0:]                                         
                     
        while self.Q:                                                                                                          
            u = self.findSmallestNode()                                     
            if self.dist[u] == sys.maxsize:                                 
                break                                           
            if self.unpoppedQ[u] == end:                                    
                break
            uNode = self.unpoppedQ[u]                                       

            for i in self.edges[uNode]:                                     
                if i in self.Q:                                             
                    if i in self.getUnvisitedNodes(uNode):                  
                        if int (self.dist[self.unpoppedQ.index(uNode)]) + self.weights[(uNode,i)] < self.dist[self.unpoppedQ.index(i)]:
                            self.dist[self.unpoppedQ.index(i)] = int (self.dist[self.unpoppedQ.index(uNode)]) + self.weights[(uNode,i)]
                            self.previous[self.unpoppedQ.index(i)] = uNode  
            self.Q.pop(self.Q.index(uNode))
        
        weight = self.dist[self.unpoppedQ.index(uNode)+1]                   
        shortest_path = []                                                  
        shortest_path.insert(0, end)                                        
        u = self.getIndex(end)                                              

        while self.previous[u] != None:                                     
            shortest_path.insert(0, self.previous[u])                       
            u = self.getIndex(self.previous[u])                             
        output = (shortest_path,weight)                                     
        return output

graph = Graph(8)                                                            
edges =[                                                                    
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
    
for edge in edges:                                                          
    graph.add_edge(*edge)                                                   
print(graph.dijsktra('O', 'T'))                                             