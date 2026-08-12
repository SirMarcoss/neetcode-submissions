class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def backtrack(Index):
            if Index == len(s):
                res.append(path[:])
                return
            
            for j in range(Index, len(s)):
                if self.isPalindrome(s, Index, j):
                    path.append(s[Index: j + 1])
                    backtrack(j + 1)
                    path.pop()
        
        backtrack(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        return True
            
            

        