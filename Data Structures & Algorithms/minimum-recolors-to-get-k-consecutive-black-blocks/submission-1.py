class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        # brute force solution:
        # 2 nested for loops
        # time complexity = O(N^2)
        # Not the optimal way to resolve this problem

        # sliding window:
        # "WBBWWBBWBW"
        # ['W'] --> first window 
        # 'B' != 'W' so we must change it --> op += 1
        # ... at the end return the number of op occured
        # Time complexity: O(N) --> Each value enters and
        # leaves the window only once.
        # Space complexity : O(1) --> costant not other Data structure

        l = 0
        recolor = 0
        res = k

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                recolor += 1
            if r - l + 1 == k:
                res = min(res, recolor)
                if blocks[l] == 'W':
                    recolor -=1
                l += 1
        return res
        


    
            

            
        