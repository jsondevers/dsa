#include <bits/stdc++.h>
class Solution {
public:
  int longestCommonSubsequence(string text1, string text2) {
    int dp[text1.size() + 1][text2.size() + 1];

    for (int i = 0; i < text1.size() + 1; i++) {
      for (int j = 0; j < text2.size() + 1; j++) {
        dp[i][j] = 0;
      }
    }
    for (int i = text1.size() - 1; i >= 0; i--) {
      for (int j = text2.size() - 1; j >= 0; j--) {
        if (text1[i] == text2[j]) {
          dp[i][j] = 1 + dp[i + 1][j + 1];
        } else {
          dp[i][j] = max(dp[i][j + 1], dp[i + 1][j]);
        }
      }
    }
    return dp[0][0];
  }
};