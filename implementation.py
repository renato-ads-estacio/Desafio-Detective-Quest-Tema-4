
from collections import deque
from typing import Dict, List, Optional

class DetectiveGraph:
    """
    Grafo simples para investigação.
    Permite adicionar arestas (não direcionadas), fazer BFS para menor caminho,
    e buscar objetos/pistas associados a nós.
    """
    def __init__(self):
        self.adj: Dict[str, List[str]] = {}
        self.clues: Dict[str, List[str]] = {}

    def add_edge(self, a: str, b: str):
        self.adj.setdefault(a, []).append(b)
        self.adj.setdefault(b, []).append(a)

    def add_clue(self, location: str, clue: str):
        self.clues.setdefault(location, []).append(clue)

    def bfs_path(self, start: str, target: str) -> Optional[List[str]]:
        if start == target:
            return [start]
        q = deque([start])
        visited = {start}
        parent = {start: None}
        while q:
            node = q.popleft()
            for nb in self.adj.get(node, []):
                if nb not in visited:
                    visited.add(nb)
                    parent[nb] = node
                    if nb == target:
                        # reconstruct path
                        path = [nb]
                        cur = nb
                        while parent[cur] is not None:
                            cur = parent[cur]
                            path.append(cur)
                        return list(reversed(path))
                    q.append(nb)
        return None

    def collect_clues_along_path(self, path: List[str]) -> List[str]:
        found = []
        for p in path:
            found.extend(self.clues.get(p, []))
        return found

if __name__ == '__main__':
    g = DetectiveGraph()
    edges = [('Casa','Rua'),('Rua','Loja'),('Loja','Escola'),('Escola','Parque')]
    for a,b in edges:
        g.add_edge(a,b)
    g.add_clue('Loja','Pegada') 
    g.add_clue('Parque','Fio de cabelo')
    print('Path:', g.bfs_path('Casa','Parque'))
    print('Clues:', g.collect_clues_along_path(['Casa','Rua','Loja','Escola','Parque']))
