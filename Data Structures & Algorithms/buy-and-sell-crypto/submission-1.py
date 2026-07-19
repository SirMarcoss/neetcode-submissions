class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # edge cases:
        # l, r = 0, len(prices) -1
        # if prices[l] < prices[r]: return prices[r] - prices[l]
        # On the other hand if we have a decreasing array:
        # return 0 thus the max profit is 0.

        #brute force solution: double nested for loops:
        # time complexity = O(N^2) this is not the optimal way to resolve this type of problem

        # [10,1,5,6,7,1] --> slinding window composed by two elements of the input array
        # [10,1] 10 > 1 --> we are in loss, so we have to step over
        # [1,5] 1 > 5? no, so we must check the profit: 5 -1 = 4 and then we can store this value
        # [1,5,6] 1 > 6 no --> 6 -1 = 5  5 > 4 ? yes so store this value
        # [1,5,6,7] 1 > 7 no --> 7 - 1 = 6  6 > 5 ye so store this value
        # [1,5,6,7,1] 1 > 1 no --> reduce the slinding window
        # [5,6,7,1] 5 > 1 no --> redue
        # ecc.
        #time complexity: O(N) iterating throught every value only one time
        # space complexity: O(1)

        l, r = 0, 1
        res  = 0
        while r <= len(prices) -1:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > res:
                    res = profit
            else:
                l = r
            r += 1
        return res
        


        