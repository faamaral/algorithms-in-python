

def bfs(graph, init):
    visited = []
    queue = [init]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.append(current)
            adj = graph[current]
            for neighbor in adj:
                for k in neighbor.keys():
                    queue.append(k)
    return visited