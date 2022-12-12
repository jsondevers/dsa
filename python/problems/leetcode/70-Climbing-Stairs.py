# Time: O(N), Space: O(N) because we create a cache
class Solution:
    def climbStairs(self, n: int) -> int:
        def memo(n, cache):
            if n <= 2:
                return n
            if n in cache:
                return cache[n]
            cache[n] = memo(n - 1, cache) + memo(n - 2, cache)
            return cache[n]

        return memo(n, {})


# Time: O(N), Space: O(1) because we create a array of size 2 and we only track those 2 values
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 1
        dp = [1] * 2
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
        return dp[1]
