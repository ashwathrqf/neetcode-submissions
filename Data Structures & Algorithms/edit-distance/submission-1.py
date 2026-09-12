class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for r in range(m+1):
            dp[r][n]=m-r
        for c in range(n+1):
            dp[m][c]=n-c
        for c in range(n-1,-1,-1):
            for r in range(m-1,-1,-1):
                if word1[c]!=word2[r]:
                    dp[r][c]=1+min(dp[r+1][c+1],dp[r][c+1],dp[r+1][c])
                else:
                    dp[r][c]=dp[r+1][c+1]
        return dp[0][0]

        