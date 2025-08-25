class Solution:
    
    def climbStairs(self, n: int) -> int:
        self.dp = [-1]*(n+1)
        return self.memoization(n)

    def memoization(self, n: int) -> int:
        if n <= 3:
            return n
        if self.dp[n] != -1:
            return self.dp[n]
        self.dp[n] = self.memoization(n-1) + self.memoization(n-2)
        return self.dp[n]