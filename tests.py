
from implementation import DetectiveGraph
if __name__ == '__main__':
    g = DetectiveGraph()
    edges = [('A','B'),('B','C'),('C','D'),('B','E')]
    for a,b in edges:
        g.add_edge(a,b)
    g.add_clue('C','Badge')
    path = g.bfs_path('A','D')
    print('Path A->D:', path)
    print('Clues along path:', g.collect_clues_along_path(path))
