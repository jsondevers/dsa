#include <bits/stdc++.h>
using namespace std;
class Solution {
 public:
  bool halvesAreAlike(string s) {
    set<char> vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'};
    int left = 0, right = s.size() - 1;
    int first = 0, second = 0;
    while (left <= right) {
      if (vowels.find(s[left]) != vowels.end()) {
        first++;
      }
      if (vowels.find(s[right]) != vowels.end()) {
        second++;
      }
      left++;
      right--;
    }

    return first == second;
  }
};