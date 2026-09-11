class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashtable = {}
        res = 0
        l = 0
        maxFreq = 0

        for r in range(len(s)):
            if s[r] not in hashtable:
                hashtable[s[r]] = 1
            else:
                hashtable[s[r]] += 1
            
            maxFreq = max(maxFreq, hashtable[s[r]])

            while (r - l + 1) - maxFreq > k:
                hashtable[s[l]] -= 1
                if hashtable[s[l]] == 0:
                    del hashtable[s[l]]
                
                l += 1
            
            res = max(res, r - l + 1)
        
        return res

