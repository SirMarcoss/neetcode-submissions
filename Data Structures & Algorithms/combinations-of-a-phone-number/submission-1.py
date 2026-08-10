class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hashdigits = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
    
        def backtrack(Index, CurStr):
            if len(CurStr) == len(digits):
                res.append(CurStr)
                return
            
            for i in hashdigits[digits[Index]]:
                backtrack(Index + 1, CurStr + i)
            
        
        if digits:
            backtrack(0, "")
        return res