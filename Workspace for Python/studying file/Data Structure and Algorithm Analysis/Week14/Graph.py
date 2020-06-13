"""
Python program to implement Graph
@Author: Archibald
@Date: Sept. 12
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V


    def add_directed_edge(self, tail, header):
        node = Node(header)
        node.next = self.graph[tail]
        self.graph[tail] = node

    def print_graph(self):
        for i in range(self.V):
            print("vertex {} ".format(i), end = "")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.v), end = "")
                temp = temp.next
            print("\n")

class Node:
    def __init__(self, key):
        self.v = key
        self.next = None



if __name__ == "__main__":
    adjacencyMap = [[0,1,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,0],
                    [1,1,0,0,0],
                    [1,0,0,1,0]]

    V = 5
    graph = Graph(V)
    for i in range(V):
        for j in range(V):
            if adjacencyMap[i][j] == 1:
                graph.add_directed_edge(i, j)

    graph.print_graph()


