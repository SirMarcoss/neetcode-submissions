class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False

        visited = set()

        hashtable = {i : [] for i in range(n)}
        for i, j in edges:
            hashtable[i].append(j)
            hashtable[j].append(i)

        
        def dfs(node, parent):

            if node in visited:
                return False
            
            visited.add(node)

            for child in hashtable[node]:
                if child == parent:
                    continue
                
                if not dfs(child, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n 
            



        # utilizzo -1 perchè tanto è un nodo che non esiste e posos fare finta che sia il padre del primo nodo
        # la verifica della lunghezza del set, serve per verificare che il grafo sia completamente connesso in un unico blocco 
        # Se hai meno di n-1 archi --> impossibile connettere tutti i nodi (isole staccate)
        # se hai più di n-1 archi --> 100% presenza di cicli
        # un albero deve avere esattamente n-1 archi

        # rules trees :  no cycles and fully connected --> we analyze if we have a cylce trought the hashset itself and if we have only 
        # a one connected component with the lenght of the hashset: if the lenght is equal to te number of nodes we can return True