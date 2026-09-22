class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        hashtable = {crs : [] for crs in range(numCourses)}
        for crs, pre in prerequisites:
            hashtable[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if hashtable[crs] == []:
                return True
            
            visited.add(crs)

            for pre in hashtable[crs]:
                if not dfs(pre):
                    return False
            
            visited.remove(crs)
            hashtable[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        # In questo codice, visited NON rappresenta "tutti i nodi visitati nella storia", ma rappresenta il percorso corrente
        # (la sequenza di chiamate ricorsive attualmente attive nello stack).

        