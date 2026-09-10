class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # [1,7,2,5,4,7,3,6] --> the output : 36 
        # 7 and 6 but we must do the minimum between these two values --> min(height[1], height[7])


        #Two pointers pattern
        #[1,7,2,5,4,7,3,6] --> nums
        # ^             ^ 
        # i             j

        # area = 0 --> we are going to return this value

        #for loop --> for num in nums:

        # local_area = min(nums[i], nums[j]) * (j - i) = 7    nums[i], nums[j] = height     (j-i) = lenght 
        # if local area > area --> area = local_area
        # if nums[i] < nums[j] --> i += 1
        # if nums[i] > nums[j] --> j -= 1
        
        # Time complexity = O(N)
        #Space Complexity = O(1) --> we are not using a specific data structure. We're only initializing variables


        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            currArea = (r - l) * min(heights[r], heights[l])

            area = max(area, currArea)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return area




# TEST

# area = 0
#[2,2,2]
# ^   ^ The first is 'i' and the last one is 'j'
#first iteration: min(2,2) * (2-0) = 4 = local_area
# local_area > area --> area = local_area

# heights[j] = 2 >= heights[i] = 2 --> j = 1




        
