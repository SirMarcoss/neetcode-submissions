class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dfs(n):
            if n >= len(nums):
                return 0
            elif n in memo:
                return memo[n]
            else:
                memo[n] = max(nums[n] + dfs(n + 2), dfs(n + 1))
                return memo[n]
            
        return dfs(0)

    



        