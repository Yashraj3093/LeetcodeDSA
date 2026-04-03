class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n = len(coins)
        m = len(coins[0])

        dp = [[[-inf] * 3 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                for k in range(3):
                    val = coins[i][j]

                    if i == 0 and j == 0:
                        if val < 0 and k > 0: dp[i][j][k] = 0
                        else: dp[i][j][k] = val
                        continue
                    
                    result = -inf 
                    if i > 0:
                        result = max(result, val + dp[i - 1][j][k])
                        if val < 0 and k: result = max(result, dp[i - 1][j][k - 1])
                    
                    if j > 0:
                        result = max(result, val + dp[i][j - 1][k])
                        if val < 0 and k: result = max(result, dp[i][j - 1][k - 1])
                    
                    dp[i][j][k] = result
        
        return dp[-1][-1][2]