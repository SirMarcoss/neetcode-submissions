class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # sorted non-decreasing order
        # brute force solution:

        # [1,2,3,4]   : target = 3
        #  ^ --> for loop for n in numbers
        #    ^ --> for t in numbers 1+2 = 3 --> return [n, t]
        # Time Complexity = O(N^2)
        # Space complexity = O(1) --> costant

    
        l, r = 0, len(numbers) - 1

        while l < r :
            currentSum = numbers[l] + numbers[r]

            if currentSum == target:
                return [l+1, r+1]
            
            elif currentSum > target:
                r -= 1
            else:
                l += 1
                



