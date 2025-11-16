
from implementation import DetectiveGraph
g = DetectiveGraph()
edges = [('Casa','Rua'),('Rua','Loja'),('Loja','Escola'),('Escola','Parque'),('Parque','Estacao')]
for a,b in edges:
    g.add_edge(a,b)
g.add_clue('Loja','Pegada')
g.add_clue('Parque','Fio de cabelo')
print('Path Casa->Estacao:', g.bfs_path('Casa','Estacao'))
print('Clues Casa->Estacao:', g.collect_clues_along_path(['Casa','Rua','Loja','Escola','Parque','Estacao']))
