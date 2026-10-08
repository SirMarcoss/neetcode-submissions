class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(index, total, path):
            if total == target:
                res.append(path[:])
                return
            
            if total > target or index == len(nums):
                return
            
            path.append(nums[index])
            backtrack(index, total + nums[index], path)

            path.pop()
            backtrack(index + 1, total, path)
        
        backtrack(0, 0, path)
        return res