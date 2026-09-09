class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = max(nums)

        minCurr, maxCurr = 0,0

        for num in nums:
            temp = maxCurr
            maxCurr = max(num, minCurr + num, maxCurr + num)
            minCurr = min(num, minCurr + num, temp + num)
            res = max(res, maxCurr, minCurr)
        
        return res
        
        

        
        

        