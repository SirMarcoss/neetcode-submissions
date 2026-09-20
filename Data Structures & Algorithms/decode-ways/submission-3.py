class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1} # base case: se abbiamo raggiunto l'ultima lettera della stringa
        # abbiamo un solo modo per decodificarla

        def dfs(n):
            if n in dp:
                return dp[n]
            if s[n] == '0':
                return 0
            
            res = dfs(n + 1)
            if n + 1 < len(s) and (s[n] == '1' or s[n]== '2' and s[n + 1] in '0123456'):
                res += dfs(n + 2)
            
            dp[n] = res
            return res
        
        return dfs(0)



        # dfs(i + 1)   "Mangio 1 cifra (la '1') e lascio da analizzare "02"".
        # dfs(i + 2)   "Mangio 2 cifre insieme (il "10") e lascio da analizzare solo il "2"".    