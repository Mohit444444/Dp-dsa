class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # Initializing a matrix of size (m+1)*(n+1)
        dp = [[0] * (n + 1) for x in range(m + 1)]

        # Building dp[m+1][n+1] in bottom-up fashion
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j],
                    dp[i][j - 1])

        # dp[m][n] contains length of LCS for S1[0..m-1]
        # and S2[0..n-1]
        return dp[m][n]

        # time O(m * n)
        # space O(m * n)