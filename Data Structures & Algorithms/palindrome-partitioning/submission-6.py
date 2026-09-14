class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(Index, path):
            if Index == len(s):
                res.append(path[:])
            
            for j in range(Index, len(s)):
                if self.isPalindrome(s, Index, j):
                    path.append(s[Index : j + 1])
                    backtrack(j + 1, path)
                    path.pop()
        
        backtrack(0, path)
        return res
    
    def isPalindrome(self, s: str, l: int, r: int) -> bool:

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True