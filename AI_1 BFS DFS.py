def bfs(graph, start):
    visited = set()  
    queue = [start]  
    
    while queue:
        node = queue.pop(0)  
        if node not in visited:
            print(node, end=" ") 
            visited.add(node)  
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E'],
}

bfs(graph, 'S')


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()  
    
    print(node, end=" ")  
    visited.add(node)  
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    'S': ['A', 'B'],
    'A': ['S', 'C', 'D'],
    'B': ['S', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'B', 'E'],
    'E': ['B', 'D', 'F'],
    'F': ['C', 'E'],
}

dfs(graph, 'S')



