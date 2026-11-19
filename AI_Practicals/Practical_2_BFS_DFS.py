print("IAR/17360")

# Create graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Graph:")
print(graph)

# Breadth First Search (BFS)
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited and neighbour not in queue:
                    queue.append(neighbour)

    return visited


# Depth First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

    return visited


print("\nBFS starting from A:")
print(bfs(graph, 'A'))

print("\nDFS starting from A:")
print(dfs(graph, 'A'))
