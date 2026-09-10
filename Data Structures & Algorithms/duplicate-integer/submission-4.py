class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}

        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                return True
        return False
  