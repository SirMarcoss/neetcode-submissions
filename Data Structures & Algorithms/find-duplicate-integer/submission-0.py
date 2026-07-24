class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dictionary = {}

        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1

        for k, v in dictionary.items():
            if v > 1:
                return k            
        