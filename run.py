### Test

from dados import arquivo
from busca_em_profundidade import dfs

graph = arquivo.extract_data('grafo.txt')

if __name__ == '__main__':
    path = dfs.dfs(graph, 'Salinas')
    print(graph)
    print(path)