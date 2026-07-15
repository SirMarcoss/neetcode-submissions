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

        # Optimal Solution: Time complexity O(N^2)
        # We can sort the array:

        nums.sort()
        
        #[-1, 0, 1, 2, -1, -4] --> sorting --> [-4, -1, -1, 0, 1, 2]
        # iterate the array: -4 = -(num[i] + nums[j]) --> return  number (for number in numbers), num[i], num[j]
        # we can use to find i and j --> two pointers.

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l = i+1
            r = len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -=1
                
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -=1
                    # avoid duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

        

        