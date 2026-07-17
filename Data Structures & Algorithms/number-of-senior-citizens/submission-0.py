class Solution:
    def countSeniors(self, details: List[str]) -> int:

        res = 0

        for char in details:
            if int(char[11:13]) > 60:
                res += 1
        
        return res

            
        