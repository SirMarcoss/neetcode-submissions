class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):

            p = par[node]
            while p != par[p]:
                p = par[par[p]]

            return p
        
        def union(p1, p2):
            p1, p2 = find(p1), find(p2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            

