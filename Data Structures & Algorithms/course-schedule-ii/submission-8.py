class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        hashtable = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashtable[crs].append(pre)
        
        hashset = set() # prevent cycle
        visited = set() # already in res
        res = []

        def dfs(crs):
            if crs in hashset:
                return False
            
            if hashtable[crs] == [] and crs not in visited:
                visited.add(crs)
                res.append(crs)
                return True
            if crs in visited:
                return True
            
            hashset.add(crs)
            for pre in hashtable[crs]:
                if not dfs(pre):
                    return False
                
            hashset.remove(crs)
            hashtable[crs] = []
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
                






        