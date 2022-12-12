#include <bits/stdc++.h>
// Time: O(N), Space: O(N) bc we create a cache
class Solution {
public:
  int memo(int n, map<int, int> &cache) {
    if (n <= 2) {
      return n;
    } else if (cache.find(n) != cache.end()) {
      return cache[n];
    }
    cache[n] = memo(n - 1, cache) + memo(n - 2, cache);
    return cache[n];
  }

  int climbStairs(int n) {
    map<int, int> cache;
    return memo(n, cache);
  }
};

// Time: O(N), Space: O(1), no arrays
class Solution {
public:
  int climbStairs(int n) {
    if (n == 1) {
      return 1;
    }
    if (n == 2) {
      return 2;
    }

    int first = 1;
    int second = 2;

    int result = 0;

    for (int i = 2; i < n; i++) {
      result = first + second;
      first = second;
      second = result;
    }

    return result;
  }
};