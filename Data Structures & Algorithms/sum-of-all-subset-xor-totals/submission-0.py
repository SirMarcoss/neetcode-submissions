class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        res = []
        path = []

        def backtrack(Index, path):
            nonlocal total

            if Index == len(nums):
                total += self.xor_sum_iterative(path)
                return
            
            path.append(nums[Index])
            backtrack(Index + 1, path)
            path.pop()
            backtrack(Index + 1, path)

        backtrack(0, path)
        return total
    


    
    def xor_sum_iterative(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            total ^= num  
        return total

        