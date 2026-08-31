class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dfs(n):
            # Base case

            if n >= len(nums):
                return 0
            
            elif n in memo:
                return memo[n]

            else:
                memo[n] =  max(dfs(n+1), nums[n] + dfs(n+2))
                return memo[n]


        return dfs(0)
            




        