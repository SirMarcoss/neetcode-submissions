class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums1 = nums[1:]
        nums2 = nums[:-1]

        def dfs(n, nums, current_memo):
            if n >= len(nums):
                return 0
            elif n in current_memo:
                return current_memo[n]
            else:
                current_memo[n] = max(nums[n] + dfs(n + 2, nums,current_memo ), dfs(n + 1, nums, current_memo))
                return current_memo[n]
        
        return max(dfs(0,nums1, {}), dfs(0, nums2, {}))

        
        