class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index, path):
            if index == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(index + 1, path)

            path.pop()
            backtrack(index + 1, path)
        
        backtrack(0, path)
        return res