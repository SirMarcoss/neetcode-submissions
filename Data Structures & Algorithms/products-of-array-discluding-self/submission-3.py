class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        l = len(nums)

        res = [1] * l


        total = 1
        for i in range(len(nums)):
            res[i] = total
            total *= nums[i]
        
        total = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= total
            total *= nums[i]
        
        return res
            
