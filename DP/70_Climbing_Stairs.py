class Solution:
    def __init__(self):
        self.dp = [-1] * 46
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        if self.dp[n] == -1:
            self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
