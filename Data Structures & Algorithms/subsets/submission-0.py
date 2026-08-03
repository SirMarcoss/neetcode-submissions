class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtracking(CurIndex, path):
            if CurIndex == len(nums):
                res.append(path[:])
                return
            
            # BackTracking include
            path.append(nums[CurIndex])
            backtracking(CurIndex + 1, path)
            path.pop()

            backtracking(CurIndex + 1, path)
        
        backtracking(0, path)
        return res

        
        