class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        l = 0
        r = 1

        ascendent = False

        if nums[l] <= nums[r]:
            ascendent = True

        while r <= len(nums) -1:
            if ascendent == True:
                if nums[l] <= nums[r]:
                    l += 1
                    r += 1
                else:
                    return False

            else:
                if nums[l] >= nums[r]:
                    l += 1
                    r += 1
                else:
                    return False
        return True
                    
        