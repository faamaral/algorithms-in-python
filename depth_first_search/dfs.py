__author__ = 'Fabiano'


def dfs(graph, init):
    ''' Lista de vertices visitados '''
    visited = []
    ''' Pilha de vertices espandidos'''
    stack = [init]

    while stack:
        ''' Retira o elemento do topo da pilha '''
        current = stack.pop()
        ''' Espande a lista de vizinhos do vertice atual '''
        adj = graph[current]
        ''' Percorre a lista de visinhos '''
        for neighbor in adj:
            for k in neighbor.keys():
                ''' Se o vertice não foi marcado como visitado '''
                if k not in visited:
                    ''' Adiciona ele no topo da pilha '''
                    stack.append(k)
        ''' Marca o vertice atual como visitado '''
        visited.append(current)
    ''' Retorna a lista de visitados '''
    return visited


