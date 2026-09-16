class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]


        def dfs(i, nums, memo):
            if i >= len(nums):
                return 0
            elif i in memo:
                return memo[i]
            else:
                memo[i] = max(nums[i] + dfs(i + 2, nums, memo), dfs(i + 1, nums, memo))
            return memo[i]
        
        return max(dfs(0, nums[:len(nums) - 1], {}), dfs(0, nums[1:], {}))