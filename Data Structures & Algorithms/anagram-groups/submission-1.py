class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for original_word in strs:
            count = [0] * 26
            
            for char in original_word:
                indice = ord(char) - ord('a')
                count[indice] += 1
            
            
            magic_key = tuple(count)
            
            
            anagram_map[magic_key].append(original_word)
            
        return list(anagram_map.values())
           



        





        # 1. sort the array:
        # act --> act (sorted)
        # is act inside the hastable? no, let's we add it:
        # dictionary[act] = [act]
        # O(N logN)
            

            





        