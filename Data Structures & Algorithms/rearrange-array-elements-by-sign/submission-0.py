class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = 0
        res = [0] * len(nums)
        r = 1

        for k in range(len(nums)):
            if nums[k] > 0:
                res[l] = nums[k]
                l += 2
            else:
                res[r] = nums[k]
                r += 2
        return res


    
    #  . .
    # [3,1,-2,-5,2,-4]
    # res --> [3]
        