class Solution:
    # Function to return max value that can be put in knapsack of capacity.
    def knapSack(self, capacity, val, wt):
        n = len(wt)
        dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

        # Build table dp[][] in bottom-up manner
        for i in range(n + 1):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n][capacity]

    
    # O(n x W) Time and O(W) Space