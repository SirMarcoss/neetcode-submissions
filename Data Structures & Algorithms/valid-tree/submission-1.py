class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()

        if len(edges) > n - 1:
            return False
        
        hashtable = {i : [] for i in range(n)}
        for i, j in edges:
            hashtable[i].append(j)
            hashtable[j].append(i)
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbour in hashtable[node]:
                if neighbour == parent:
                    continue
                
                if not dfs(neighbour, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
            
            
        



        