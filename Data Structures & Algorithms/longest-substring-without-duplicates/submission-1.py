class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashset = set()
        res = 0

        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, len(hashset))
        return res


# TEST
# "abcabcbb"
# 'a' not in hashset --> ('a'), res = 1
# 'b' not in hashset --> ('a','b') res = 2
# 'c' not in hashset --> ('a', 'b','c') res = 3
# 'a' in hashset -->   ('b','c') res = 3

