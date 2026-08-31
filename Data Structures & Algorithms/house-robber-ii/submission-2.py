class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top down

        def dfs(n, nums, current_memo):
            if n >= len(nums):
                return 0
            elif n in current_memo:
                return current_memo[n]
            else:
                current_memo[n] = max(nums[n] + dfs(n + 2, nums,current_memo ), dfs(n + 1, nums, current_memo))
                return current_memo[n]
        

        # bottom up space optimized

        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def helper(start, end):

            rob1, rob2 = 0, 0

            for i in range(start, end):
                temp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2


        return max(helper(1, len(nums)),helper(0, len(nums) - 1))

        
        # in realtà la space complexity anche così rimane O(n) perchè stiamo
        # utilizzando slicing dell'array --> tempo O(N) guarda solution.
        # per passare ad O(1) dobbiamo utilizzare gli indici per definire
        #inizio array e fine array





        
        