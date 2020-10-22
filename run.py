### Test

from dados import arquivo
from depth_first_search import dfs

graph = arquivo.extract_data('grafo.txt')

if __name__ == '__main__':
    path = dfs.dfs(graph, 'Salinas')
    print(graph)
    print(path)