class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        current_prefix = 1
        for i in range(n):
            res[i] = current_prefix
            current_prefix *= nums[i]
        
        current_postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= current_postfix
            current_postfix *= nums[i]
        
        return res




        # [1,2,4,6]
        #      ^

        #prefix sum: --> [1, 2, 8, 12]
        #postfix sum: --> [48, 8, 2, ]

        