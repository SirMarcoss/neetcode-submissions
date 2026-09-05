class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True # caso base, sasso già raggiungibile

        for i in range(len(s)):
            if dp[i]:
                for w in wordDict:
                    if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                        dp[i + len(w)] = True
        return dp[-1]




