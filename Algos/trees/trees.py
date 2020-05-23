# bfs traversal


class Tree(object):

    def bfs(self, graph, start):
        visited = list()
        queue = list()
        visited.append(start)
        queue.append(start)

        while queue:
            val = queue.pop(0)
            print(val)

            for neighbour in graph[val]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def dfs(self, graph, start):
        visited = list()
        stack = list()
        visited.append(start)
        stack.append(start)
        while stack:
            val = stack.pop()
            print(val)

            for neighbour in reversed(graph[val]):
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)


if __name__ == "__main__":
    tree = Tree()

    # graph as a Adjacency List
    graph = {'A': ['B', 'C'],
             'B': ['D', 'E', 'A'],
             'C': ['F', 'G', 'A'],
             'D': ['B'],
             'E': ['B'],
             'F': ['C'],
             'G': ['C']
             }

    #tree.bfs(graph, 'A')
    tree.dfs(graph, 'A')
