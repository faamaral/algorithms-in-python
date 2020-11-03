### Test

from dados import arquivo
from depth_first_search import dfs
from breadth_first_search.bfs import bfs

graph = arquivo.extract_data('grafo.txt')

if __name__ == '__main__':
    path = dfs.dfs(graph, 'Salinas')
    path_bfs = bfs(graph, 'Salinas')
    print(graph)
    print(path)
    print(path_bfs)