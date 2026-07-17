class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0
        max1 = 0

        for number in nums:
            if number == 1:
                res += 1
                if res > max1:
                    max1 = res
            else:
                res = 0
        return max(res, max1)

# time complexity = O(N)
# Space complexity = O(1)

# TEST
# [1,0,1,1,0,1]
# number = 1 --> res = 0+1 = 1
# number = 0 --> res = 0
# number = 1 --> res = 1
# number = 1 --> res = 1 + 1 = 2
# 
        