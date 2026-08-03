class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(Index, path, total):

            if total == target:
                res.append(path[:])
                return
            if Index == len(nums) or total > target:
                return

            path.append(nums[Index])
            backtrack(Index, path, total + nums[Index])   

            path.pop()
            backtrack(Index +1, path, total)

        backtrack(0, path, 0)
        return res       
