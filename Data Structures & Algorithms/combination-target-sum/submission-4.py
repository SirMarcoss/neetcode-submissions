class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        def backtrack(index, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target or index == len(nums):
                return
            
            path.append(nums[index])
            backtrack(index, path, total +nums[index])

            path.pop()
            backtrack(index + 1, path, total)
            
        backtrack(0, path, 0)
        return res


# Space complexity = O(2N + N) --> 2 array + call stack which in teh worst case is long N --> O(N)
# Time Complexity = O(2^N)