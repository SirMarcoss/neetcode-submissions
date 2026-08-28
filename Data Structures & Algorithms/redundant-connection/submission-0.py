class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        graph = {i + 1: [] for i in range(len(edges))}
        
        # Questa DFS controlla se esiste GIA' un percorso tra 'node' e 'target'
        def dfs(node, target, visited):
            if node == target:
                return False
            
            visited.add(node)
            
            # Esploro i neighbours
            for nei in graph[node]:
                if nei not in visited:
                    if not dfs(nei, target, visited):
                        return False
            return True

        # Analizziamo un arco alla volta seguendo l'ordine di input
        for u, v in edges:
            # Se entrambi i nodi sono già nel grafo, c'è il rischio di un ciclo
            if u in graph and v in graph:
                if  not dfs(u, v, set()):
                    # Se c'è già un percorso, questo arco chiude il ciclo!
                    return [u, v]
            
            # Se non c'è ciclo, aggiungiamo l'arco al nostro grafo
            graph[u].append(v)
            graph[v].append(u)