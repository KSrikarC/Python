class directed_Graph:
    
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self,source, destination):
        if source not in self.graph:
            self.add_vertex(source)
        self.graph[source].append(destination)
        

    def get_vertices(self):
        return self.graph.keys()
    
    def get_edges(self):
        self.edges = []
        for vertex in self.graph:
            for sub_vertices in self.graph[vertex]:
                self.edges.append((vertex,sub_vertices))
        return self.edges


    def dfs(self,start_vertex):
        self.visited = set()

        def dfs_util(vertex):
            self.visited.add(vertex)
            print(vertex,end=' ')
            
            if vertex in self.graph:
                for adj_vertex in self.graph[vertex]:
                    if adj_vertex not in self.visited:
                        dfs_util(adj_vertex)
        dfs_util(start_vertex)


    def bfs(self,start_vertex):                                                     #           H

        self.visited = set()                                                        #      A    B   C
        
        from  collections import deque                                              #      D    E   F
        q = deque()                                                                 #           F
        self.visited.add(start_vertex)
        q.append(start_vertex)
        
        while q:
            cur_vertex = q.popleft()
            print(cur_vertex,end=' ')

            if cur_vertex in self.graph:
                for adj_vertex in self.graph[cur_vertex]:
                    if adj_vertex not in self.visited:
                        self.visited.add(adj_vertex)
                        q.append(adj_vertex)


g = directed_Graph()

g.add_edge('H','A')
g.add_edge('H','B')
g.add_edge('H','C')
g.add_edge('A','D')
g.add_edge('B','E')
g.add_edge('C','F')
g.add_edge('D','G')
g.add_edge('E','G')
g.add_edge('F','G')        


g.bfs('H')
