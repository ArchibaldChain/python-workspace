"""
This code was used to implement the Topology Sort in a Graph
"""



class DirectedAcyclicGraph:

    def __init__(self, num):
        self.num = num
        self.visited = [False] * num
        self.adj_list = []
        self.in_degree = [0] * num
        for x in range(num):
            self.adj_list.append([])

    def add_edge(self, tail, head):
        self.adj_list[tail].append(head)

    def topological_sort(self):
        stack = []
        for i in range(self.num):
            for j in self.adj_list[i]:
                self.in_degree[j] += 1

        for x in range(self.num):
            if not self.visited[x] and self.in_degree[x] == 0:
                self.topological_sort_util(x, stack)
        if len(stack) < self.num:
            print("This is not a directed Acyclic graph")
        else:
            print(stack)

    def topological_sort_util(self, vertex, stack):
        self.visited[vertex] = True
        stack.append(vertex)
        for i in self.adj_list[vertex]:
            self.in_degree[i] -= 1

        for x in self.adj_list[vertex]:

            if not self.visited[x] and self.in_degree[x] == 0:
                self.topological_sort_util(x, stack)



v = 6
g = DirectedAcyclicGraph(v)
adj_map = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [1,1,0,0,0],
    [1,0,1,0,0]]

for i in range(v):
    for j in range(v - 1):
        if adj_map[i][j] == 1:
            g.add_edge(i, j)

print( "Following is a Topological Sort of the given graph")
g.topological_sort()
