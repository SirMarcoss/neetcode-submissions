class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        hashmap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            hashmap[crs].append(pre)

        def dfs(crs):
            if crs in visited:
                return False
            if hashmap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in hashmap[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            hashmap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        