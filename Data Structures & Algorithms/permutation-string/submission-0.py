class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # sliding windows: fixed window composed by three elements
        # Time complexity: O(N) 
        # "lecabee"
        #  l-r --> ['l','e','c']
        # Space Complexity = O(N) 

        if len(s1) > len(s2):
            return False

        hashmap_s1 = {}
        hashmap_res = {}

        for char in s1:
            if char not in hashmap_s1:
                hashmap_s1[char] = 1
            else:
                hashmap_s1[char] += 1
        
        l = 0
        for r in range(len(s2)):
            if s2[r] not in hashmap_res:
                hashmap_res[s2[r]] = 1
            else:
                hashmap_res[s2[r]] +=1
            
            if (r - l + 1) > len(s1):
                hashmap_res[s2[l]] -=1

                if hashmap_res[s2[l]] == 0:
                    del hashmap_res[s2[l]]

                l +=1

            if hashmap_res == hashmap_s1:
                return True

        return False



        