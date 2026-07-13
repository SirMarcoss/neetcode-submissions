class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                indice = ord(char) - ord('a')
                count[indice] += 1
            
            if tuple(count) not in anagram_map:
                anagram_map[tuple(count)] = []

            anagram_map[tuple(count)].append(word)
        return list(anagram_map.values())
           



        





        # 1. sort the array:
        # act --> act (sorted)
        # is act inside the hastable? no, let's we add it:
        # dictionary[act] = [act]
        # O(N logN)
            

            





        