class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for number in nums:
            if number not in dictionary:
                dictionary[number] = 1
            else:
                dictionary[number] +=1
        for k, v in dictionary.items():
            if v > 1:
                return True
        return False



            
        