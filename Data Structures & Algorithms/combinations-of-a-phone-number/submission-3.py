class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        path = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(Index):

            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            for char in phone[digits[Index]]:
                path.append(char)
                backtrack(Index + 1)
                path.pop()
        
        if digits:
            backtrack(0)
        return res
                
 