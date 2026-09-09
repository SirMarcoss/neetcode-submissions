class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        res = max(nums)

        maxCurr = 0

        for num in nums:
            temp = maxCurr
            maxCurr = max(num,  maxCurr + num)
            res = max(res, maxCurr)
        
        return res

    


        
        

        
        

        