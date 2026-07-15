class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        # sorted non-decreasing order
        # brute force solution:

        # [1,2,3,4]   : target = 3
        #  ^ --> for loop for n in numbers
        #    ^ --> for t in numbers 1+2 = 3 --> return [n, t]
        # Time Complexity = O(N^2)
        # Space complexity = O(1) --> costant

    
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i +1, j +1]
            
            elif numbers[i] + numbers[j] > target:
                j -= 1
            
            else:
                i += 1
    

