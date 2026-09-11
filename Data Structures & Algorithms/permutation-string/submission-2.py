class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # sliding windows: fixed window composed by three elements
        # Time complexity: O(N) 
        # "lecabee"
        #  l-r --> ['l','e','c']
        # Space Complexity = O(N) 

        if len(s2) < len(s1):
            return False
        
        dictionary1 = {}
        dictionary2 = {}

        for char in s1:
            if char not in dictionary1:
                dictionary1[char] = 1
            else:
                dictionary1[char] += 1
        
        l = 0
        for r in range(len(s2)):
            if s2[r] not in dictionary2:
                dictionary2[s2[r]] = 1
            else:
                dictionary2[s2[r]] += 1
            
            if (r - l + 1) > len(s1):
                dictionary2[s2[l]] -= 1

                if dictionary2[s2[l]] == 0:
                    del dictionary2[s2[l]]
                l += 1

            if dictionary1 == dictionary2:
                return True
        
        return False


