class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # brute force solution:
        # the costraints limit is 1000, so we can use 2 nested loops
        # to evaluate which is the substring without any duplicate.
        # Time complexity = O(N^2) cause every value of the string is checked twice
        # this is not the optimal solution

        # Sliding window
        # let's start with a window composed by only one element; two pointers
        # left and right 
        # as long as the rule is verified we can increment right. on the other hand,
        # we must stop right and increment left until the rule is satisfied
        # We can use a set to identify if a value is already inside
        # search in set = O(1) --> costant

        hashset = set()

        l = 0
        res = 0

        for r in range(len(s)):
            
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[r])
            res = max(res, len(hashset))
        return res





# test
# "pwwkew"
# not hashset --> ('p')
# 'w' in hashset? no --> ('p','w')
# 'w' in hashet= yes --> ('w')
# 'k in hashet? no --> ('w','k')
# 'e' in hashset= no --> ('w','k','e')
# 'w' in hashset? yes --> ('k','e','w')
#return len(hashset) =  3