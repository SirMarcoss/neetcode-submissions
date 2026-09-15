class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set() # usefull for finding the cycle
        hashset = set() # usefull for every course that we have already inserted into res

        hashtable = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashtable[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if hashtable[crs] == [] and crs not in hashset:
                hashset.add(crs)
                res.append(crs)
                return True
            if crs in hashset:
                return True
            
            visited.add(crs)

            for pre in hashtable[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            hashset.add(crs)
            hashtable[crs] = []
            res.append(crs)
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res



                    
            



        