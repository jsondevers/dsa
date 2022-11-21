/*
Time: O(n)
Space: O(1)  (In other languages this is O(n))
Because Strings in C++ are mutable, we don't have to create any
additional data structures to make a string mutable.
*/

#include <iostream>
using std::string;

class Solution {
 public:
  string reverseWords(string s) {
    // reverse the whole string
    reverse(s.begin(), s.end());

    int n = s.size();
    int idx = 0;
    for (int start = 0; start < n; start++) {
      if (s[start] != ' ') {
        // go to the beginning of the word
        if (idx != 0) s[idx++] = ' ';

        // go to the end of the word
        int end = start;
        while (end < n && s[end] != ' ') {
          s[idx++] = s[end++];
        }
        // reverse the word
        reverse(s.begin() + idx - (end - start), s.begin() + idx);

        // move to the next word
        start = end;
      }
    }
    s.erase(s.begin() + idx, s.end());
    return s;
  }
};