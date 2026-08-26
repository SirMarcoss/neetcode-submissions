class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        hashtable = {i: [] for i in range(n)}
        for i, j in edges:
            hashtable[i].append(j)
            hashtable[j].append(i)
        
        def dfs(node):
            for nei in hashtable[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                res += 1
        return res
        

        

        
  
        
            


        



        