class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}

        for index, num in enumerate(nums):
            complementary = target - num
            if complementary in hashtable:
                return [hashtable[complementary], index]
            else:
                hashtable[num] = index