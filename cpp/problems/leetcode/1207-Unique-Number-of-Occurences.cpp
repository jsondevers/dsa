#include <bits/stdc++.h>
using namespace std;

class Solution {
 public:
  bool uniqueOccurrences(vector<int>& arr) {
    unordered_map<int, int> count;

    for (int val : arr) {
      if (count.find(val) != count.end()) {
        count[val]++;
      } else {
        count[val] = 1;
      }
    }
    unordered_set<int> set_count;
    for (auto [key, value] : count) {
      set_count.insert(value);
    }

    cout << count.size() << " " << set_count.size() << "\n";
    return count.size() == set_count.size();
  }
};