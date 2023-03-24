class Graph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.adj_list = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                n1, n2, weight = edge
                self.adj_list[n1].append(n2)
                self.weight[n1].append(weight)
                if not self.directed:
                    self.adj_list[n2].append(n1)
                    self.weight[n2].append(weight)
            else:
                n1, n2 = edge
                self.adj_list[n1].append(n2)
                if not self.directed:
                    self.adj_list[n2].append(n1)

    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.adj_list, self.weight)):
                result += f"{i}: {list(zip(nodes, weights))}\n"
        else:
            for i, nodes in enumerate(self.adj_list):
                result += f"{i}: {nodes}\n"
        return result

    def __str__(self):
        return self.__repr__()

    # Time complexity: O(V + E)
    # Space complexity: O(V)
    def bfs(self, root):
        queue = [root]
        visited = [False] * self.num_nodes
        visited[root] = True
        idx = 0

        while idx < len(queue):
            current = queue[idx]
            idx += 1

            for node in self.adj_list[current]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

        return queue

    # Time complexity: O(V + E)
    # Space complexity: O(V)
    def dfs(self, root):
        stack = [root]
        visited = [False] * self.num_nodes
        result = []

        while stack:
            current = stack.pop()
            if not visited[current]:
                result.append(current)
                visited[current] = True
                for node in self.adj_list[current]:
                    if not visited[node]:
                        stack.append(node)

        return result

    def dijkstra(self, root, target):
        visited = [False] * self.num_nodes
        distance = [float("inf")] * self.num_nodes
        queue = []

        distance[root] = 0
        queue.append(root)
        idx = 0

        while idx < len(queue) and not visited[target]:
            current = queue[idx]
            visited[current] = True
            idx += 1
            self.__update_distances(current, distance)
            next_node = self.__pick_next_node(distance, visited)
            if next_node != None:
                queue.append(next_node)

        return distance[target]

    def __update_distances(self, current, distance):
        neighbors = self.adj_list[current]
        weights = self.weight[current]
        for i, node in enumerate(neighbors):
            weight = weights[i]
            if distance[current] + weight < distance[node]:
                distance[node] = distance[current] + weight

    def __pick_next_node(self, distance, visited):
        min_distance = float("inf")
        min_node = None
        for node in range(len(distance)):
            if not visited[node] and distance[node] < min_distance:
                min_node = node
                min_distance = distance[node]
        return min_node


if __name__ == "__main__":
    graph1 = Graph(5, [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)])
    print(graph1)
    print()

    graph2 = Graph(9, [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2),
                       (2, 3, 6), (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)],
                   weighted=True)
    print(graph2)
    print()

    graph3 = Graph(5, [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)], directed=True)
    print(graph3)
    print()
