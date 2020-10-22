__author__ = 'Fabiano'


def dfs(graph, init):
    visited = [] # Lista de vertices visitados
    stack = [init] # pilha de vertices espandidos

    while stack:
        current = stack.pop() # retira o elemento do topo da pilha
        adj = graph[current] # espande a lista de vizinhos do vertice atual
        for neighbor in adj: # percorre a lista de visinhos
            if neighbor not in visited: # se o vertice não foi marcado como visitado
                stack.append(neighbor) # adiciona ele no topo da pilha
        visited.append(current) # marca o vertice atual como visitado

    return visited # retorna a lista de visitados


