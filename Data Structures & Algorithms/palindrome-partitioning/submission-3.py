class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []

        def backtrack(Index):
            if Index == len(s):
                res.append(path[:])
                return
            
            for i in range(Index, len(s)):
                if self.isPali(s, Index, i):
                    path.append(s[Index : i + 1])
                    backtrack(i + 1)
                    path.pop()
        
        backtrack(0)
        return res

    
    def isPali(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -=1
        return True

