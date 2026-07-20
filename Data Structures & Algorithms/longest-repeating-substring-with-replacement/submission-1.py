class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        # brute force solution:
        # double iteration through the s string
        # trying the different cases of replacments:
        # Time complexity = O(N^2) not very good even though
        # the costraint allowed that algorithm

        # Sliding window
        #  use a window method to identify how long is the substring
        # "AAABABB"
        # 'A'== stack[-1]? --> ['A']
        # 'A'== stack[-1]? --> ['A', 'A']
        # 'A' == stack[-1]? --> ['A','A','A']
        #
        # Time complexity = O(N) --> while loop that iterate through to N values
        # Space complexity = O(N) --> we're using a stack to store
        # all the values 

        dictionary = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in dictionary:
                dictionary[s[r]] = 1
            else:
                dictionary[s[r]] += 1
            
            while (r - l + 1) - max(dictionary.values()) > k:
                dictionary[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res



# "AAABABB"
# not stack --> ['A']
# 'A' == 'A' ? yes --> ['A','A']
# 'A' == 'A' ? --> ['A','A','A']
# 'B' == 'A' ? no --> 'B' = 'A' (replace = 1) --> ['A','A','A','A']
# 'A' == 'A? ? --> ['A','A','A','A','A']
# B == 'A' 
        
        