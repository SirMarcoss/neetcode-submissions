class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute force Solution:
        # 3 nested loops:
        #[-1, 0, 1, 2, -1, -4]
        # ^ --> first loop
        #   ^ --> secondo loop
        #     ^ --> third loop
        # Time complexity = O(N^3): we have three different nested loops
        # Space complexity = O(1) = Costant 
        # THIS IS NOT THE OPTIMAL SOLUTION

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res