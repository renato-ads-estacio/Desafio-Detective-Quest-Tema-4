
# Desafio Detective Quest

## Descrição da solução
Grafo não direcionado representado por dicionário de adjacências. Implementado BFS para encontrar o menor caminho entre dois locais.
Além disso, cada local pode ter pistas (clues) associadas; é possível agregar pistas encontradas ao longo de um caminho.

### Estruturas usadas
- `dict` para adjacências (grafo) -> lista de vizinhos.
- `deque` para BFS (fila).

### Complexidade
- BFS: O(V + E) tempo e O(V) espaço para estruturas auxiliares.
- Coleta de pistas ao longo de um caminho: O(length of path + number of clues).

### Execução
```bash
python3 main.py
```
