class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def h(self, node):
        heuristic_values = {
            'A': 1,
            'B': 2,
            'C': 4,
            'D': 0  
        }
        return heuristic_values.get(node, 0)

    def a_star_algorithm(self, start, goal):
        open_list = set([start])
        closed_list = set()

        g = {start: 0}
        parents = {start: None}

        while open_list:
            current_node = None

            for node in open_list:
                if current_node is None or g[node] + self.h(node) < g[current_node] + self.h(current_node):
                    current_node = node

            if current_node == goal:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parents[current_node]
                path.reverse()
                return path

            open_list.remove(current_node)
            closed_list.add(current_node)

            for (neighbor, weight) in self.get_neighbors(current_node):
                if neighbor in closed_list:
                    continue

                tentative_g = g[current_node] + weight

                if neighbor not in open_list or tentative_g < g.get(neighbor, float('inf')):
                    parents[neighbor] = current_node
                    g[neighbor] = tentative_g
                    open_list.add(neighbor)

        print("Path does not exist!")
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}

graph = Graph(adjacency_list)
path = graph.a_star_algorithm('A', 'D')
print("Path found:", path)



