class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin = 1
        curMax = 1

        for num in nums:
            
            if num == 0:
                curMin, curMax = 1, 1
                continue

            temp = curMax
            curMax = max(num, curMax * num, curMin * num)
            curMin = min(num, temp * num, curMin * num)
            res = max(res, curMax, curMin)

        return res


# DRY TEST
# [-4, -3, -2]
# curMax = max(-4, 1 * -4, 1 * -4) = -4
# curMin = min(-4, 1 * -4, 1 * -4) = -4
# res = -2

# second iteration
#curMax = max(-3, -4 * -3, -4 * -3) = 12
# curMin = min(-3, -4 * -3, -4 * -3) -3

        