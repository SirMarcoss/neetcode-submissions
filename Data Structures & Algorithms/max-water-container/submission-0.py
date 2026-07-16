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
        #Space Complexity = O(1) --> we are not using a specific data structure. We're only initialize variables

        i = 0
        j = len(heights) - 1 # the end of the array

        area = 0

        while i < j:
            local_area = min(heights[i], heights[j]) * (j - i)
            if local_area > area:
                area = local_area
            
            if heights[i] < heights[j]:
                i += 1
        
            elif heights[i] >= heights[j]:
                j -= 1

        return area


# TEST

# area = 0
#[2,2,2]
# ^   ^ The first is 'i' and the last one is 'j'
#first iteration: min(2,2) * (2-0) = 4 = local_area
# local_area > area --> area = local_area

# heights[j] = 2 >= heights[i] = 2 --> j = 1




        
