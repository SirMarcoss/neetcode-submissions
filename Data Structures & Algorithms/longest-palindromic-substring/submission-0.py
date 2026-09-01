class Solution:
    def longestPalindrome(self, s: str) -> str:
        final = 0
        res = ''

        # odd palindrome
        for k in range(len(s)):
            i, j = k , k

            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > final:
                    res = s[i : j + 1]
                    final = j - i + 1
                i -= 1
                j += 1
            
        # even palindrome
            i, j = k, k + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > final:
                    res = s[i : j + 1]
                    final = j - i + 1
                i -= 1
                j += 1
        
        return res
