class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {len(s): 1}

        def dfs(n):

            if n in memo:
                return memo[n]
            if s[n] == '0':
                return 0
            
            res = dfs(n + 1)
            if n + 1 < len(s) and (s[n] == '1' or s[n] == '2' and
            s[n + 1] in '0123456'):
                res += dfs(n + 2)
            
            memo[n] = res
            return res
        return dfs(0)

        