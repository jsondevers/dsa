# Time: O(n * m) where n is len(text1) and m is len(text2)
# Space: O(n * m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D DP, careful brute-force, bottom-up (solve in reverse)

        # we need + 1 to fill the rows/cols wiht zeroes, see grid below
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        # iterate in reverse order
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]  # add diagonal
                else:
                    # smart brute-force
                    # max(right, bottom)
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # res will be in dp[0][0]
        return dp[0][0]


"""
The path in our 2d grid to get to three (bottom-up)
            j
        a   c   e
    a   3           0

    b       2       0

i   c       2       0

    d           1   0

    e           1   0
        0   0   0   0
"""
