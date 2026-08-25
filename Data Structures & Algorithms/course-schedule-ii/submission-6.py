class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []
        hashset = set() # a set is usefull to analyze if we have a cycle 
        visited = set()
        hashtable = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashtable[crs].append(pre)
        
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
            visited.add(crs)
            hashtable[crs] = []
            res.append(crs)
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res  

                    
            



        