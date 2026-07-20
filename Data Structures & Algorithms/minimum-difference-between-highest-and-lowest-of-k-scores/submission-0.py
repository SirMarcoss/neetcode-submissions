class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        # sort the array 
        # [2,5,3,1,6,3] --> sorting operation --> [6,5,3,3,2,1], k = 3
        # method of the fixed window
        # [6,5,3] --> 6 - 3 = 3
        # [5,3,3] --> 5 - 3 = 2 
        # [3,3,2] --> 3 - 2 = 1 
        # Time complexity = O(NlogN)
        # Space Complexity = O(1)

        nums.sort(reverse=True)
        print(nums)
        res = 10000

        l = 0
        r = k -1

        while r <= len(nums) - 1:
            diff = nums[l] - nums[r]
            res = min(res, diff)
            l  += 1
            r += 1
        return res
        



        

            


        