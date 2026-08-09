class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(Index, path):
            if Index == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[Index])
            backtrack(Index + 1, path)

            path.pop()
            backtrack(Index + 1, path)
        backtrack(0, path)
        return res
        