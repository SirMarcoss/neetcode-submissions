class Solution:

    def longestSubarray(self, nums: list[int], limit: int) -> int:
        l = 0
        res = 0

        for r in range(len(nums)):
            while max(nums[l : r + 1]) - min(nums[l : r + 1]) > limit:
                l += 1

            res = max(res, r - l + 1)

        return res