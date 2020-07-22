class graph_node:
    label = None 
    adjlist = None
    visited = None
    def __init__(self, l):
        self.label = l
        self.adjlist = []
        self.visited = 0
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
        self.visited = 1
        for i in self.adjlist:
            if i.visited == 0:
                i.dfs()


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
        p = None 
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
    
    def dfs(self):
        for i in self.nodes:
            if i.visited == 0:
                i.dfs()

if __name__ == "__main__":
    s = int(input("Please enter the size of the graph : ")) 
    g = graph(s, directed=True) 
    t = int(input("Please enter the no.of edges : ")) 
    for i in range(t):
        k = input().split() 
        g.add_edge(int(k[0]),int(k[1]))
    g.print()
    g.dfs()
    
