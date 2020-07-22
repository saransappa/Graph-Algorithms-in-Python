class graph_node:
    label = None 
    adjlist = None # adjacency list of the node
    visited = None # -1 if node is not visited, 0 if visited but still under process and 1 if node visited
    def __init__(self, l):
        self.label = l
        self.adjlist = []
        self.visited = -1

    def add_neighbour(self, k):
        self.adjlist.append(k)
    
    def print(self,adj = True):
        print(self.label,end = " ")
        if adj:
            print("->",end=" ")
            for i in self.adjlist:
                print(i.label, end=" -> ") 
            print("\n")
    
    def dfs(self):
        print(self.label,end=" -> ")
        self.visited = 0
        for i in self.adjlist:
            if i.visited == -1:
                i.dfs()
        self.visited = 1
        
class graph:
    size = None
    directed = None 
    nodes = None 
    def __init__(self, s, directed=True):
        self.size =s 
        self.directed = directed
        self.nodes = []
        for i in range(s):
            g= graph_node(i)
            self.nodes.append(g)

    def print(self):
        for i in self.nodes:
            i.print()

    def add_edge(self,k,l):
        p = None #Temporary variable 
        q = None #Temporary variable
        for i in self.nodes:
            if i.label == k:
                p = i
                break 
        for i in self.nodes:
            if i.label == l:
                q = i
        if self.directed:
            p.add_neighbour(q)
        else:
            p.add_neighbour(q)
            q.add_neighbour(p)
    
    def dfs(self, start = -1): # start denotes the label of starting node for DFS
        print('-'*10 + " Depth First Search "+'-'*10)
        if start==-1: # start becomes -1 if label if start node is not provided
            for i in self.nodes:
                if i.visited == -1:
                    i.dfs()
        else:
            self.nodes[start].dfs()
        for i in self.nodes:  # Marking all nodes as unvisited after completion of DFS 
            i.visited = -1
    
    def bfs(self, start = -1): # start denotes the label of starting node for BFS
        print('-'*10 + " Breadth First Search "+'-'*10)
        initial = None 
        if start==-1: # start becomes -1 if label if start node is not provided
            initial = 0
        else:
            initial = start 
        queue = []
        queue.append(self.nodes[initial])
        #self.nodes[initial].visited = 1
        while len(queue)!=0:
            p = queue.pop(0)
            p.visited = 1
            print(p.label,end=" -> ")
            for i in p.adjlist:
                if i.visited == -1:
                    queue.append(i) 
                    i.visited = 0
        for i in self.nodes:  # Marking all nodes as unvisited after completion of BFS 
            i.visited = -1 
       
if __name__ == "__main__":
    s = int(input("Please enter the size of the graph : ")) 
    k = int(input("Please enter 1 for directed graph or 0 for undirected graph : ")) 
    z = None 
    if k==1:
        z = True 
    else:
        z = False
    g = graph(s, directed=z) 
    t = int(input("Please enter the no.of edges : ")) 
    print("Please enter the edges in the format \"K l\" (without quotes) for an edge(k,l)")
    for i in range(t):
        k = input().split() 
        g.add_edge(int(k[0]),int(k[1]))
    g.print()
    g.bfs(start =2)
    