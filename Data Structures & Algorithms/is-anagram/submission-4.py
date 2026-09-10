class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashtable1 = {}
        hashtable2 = {}

        for char in s:
            if char not in hashtable1:
                hashtable1[char] = 1
            else:
                hashtable1[char] += 1
        
        for char in t:
            if char not in hashtable2:
                hashtable2[char] = 1
            else:
                hashtable2[char] += 1
        

        return hashtable1 == hashtable2

        

        