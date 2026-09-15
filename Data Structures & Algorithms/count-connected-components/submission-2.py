class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        hashtable = {i: [] for i in range(n)}

        for i, j in edges:
            hashtable[i].append(j)
            hashtable[j].append(i)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            
            for connected in hashtable[node]:
                dfs(connected)
        
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        
        return res

        
  
        
            


        



        