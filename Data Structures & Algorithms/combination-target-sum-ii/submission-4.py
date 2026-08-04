class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        candidates.sort()

        def backtrack(Index, path, total):
            # Case Base
            if total == target:
                res.append(path[:])
                return
            if Index == len(candidates) or total > target:
                return
            
            # Including values
            path.append(candidates[Index])
            backtrack(Index + 1, path, total + candidates[Index])

            # Not including part
            path.pop()
            while Index + 1 < len(candidates) and candidates[Index] == candidates[Index +1]:
                Index += 1
            backtrack(Index + 1, path, total)
        backtrack(0, path, 0)
        return res


        