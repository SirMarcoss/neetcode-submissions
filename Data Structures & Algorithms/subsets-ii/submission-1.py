class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def backtrack(Index, path):
            if Index == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[Index])
            backtrack(Index + 1, path)

            path.pop()
            while Index + 1 < len(nums) and nums[Index] == nums[Index + 1]:
                Index += 1
            backtrack(Index +1, path)
        
        backtrack(0, path)
        return res
        