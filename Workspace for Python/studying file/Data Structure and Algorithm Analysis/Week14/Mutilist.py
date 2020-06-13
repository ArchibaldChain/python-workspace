"""
@Author Archibald
@Date Sept. 12th
Python code used for generate Adjacency Mutilist
This code only used for undirected graph
"""


class Node:
    def __init__(self, key):
        self.out_degree = 0
        self.key = key
        self.edge = None



class Edge:
    def __init__(self, tail, header):
        self.tail = tail
        self.header = header
        self.next_edge = None

class UndirectedGraph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []
        for each in range(vertex):
            self.graph.append(Node(each))


    def add_undirected_edge(self, tail, header):
        if not self.graph[tail].edge or not self.graph[header].edge:
            edge = Edge(tail, header)
            if not self.graph[tail].edge:
                self.graph[tail].edge = edge
            else:
                temp = self.graph[tail].edge
                while temp.next_edge:
                    temp = temp.next_edge
                temp.next_edge = edge
            if not self.graph[header].edge:
                self.graph[header].edge = edge
            else:
                temp = self.graph[tail].edge
                while temp.next_edge:
                    temp = temp.next_edge
                temp.next_edge = edge
            self.graph[tail].out_degree += 1
            self.graph[header].out_degree += 1

        else:
            temp = self.graph[tail].edge
            while temp.next_edge:
                temp = temp.next_edge
            temp.next_edge = Edge(tail, header)
            self.graph[tail].out_degree += 1
            self.graph[header].out_degree += 1

    def print_graph(self):
        for i in range(self.vertex):
            print("vertex {} ".format(i), "")
            temp = self.graph[i].edge
            while temp:
                print(" -> edge {}-{}".format(temp.tail, temp.header), "")
                temp = temp.next_edge
            print()

if __name__ == "__main__":
    adjacencyMap = [[0,1,1,0,0],
                    [1,0,0,1,0],
                    [1,0,0,1,0],
                    [0,1,1,0,1],
                    [0,0,0,1,0]]

    V = 5
    graph = UndirectedGraph(V)
    for i in range(V):
        for j in range(i, V):
            if not adjacencyMap[i][j] == 0:
                graph.add_undirected_edge(i, j)

    for i in range(V):
        print("Vertex {} has out degree {}".format(i, graph.graph[i].out_degree))
    print()
    graph.print_graph()
