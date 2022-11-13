/*
You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters
and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
For example, in "abbaca" we could remove "bb" since the letters
are adjacent and equal, and this is the only possible move.
The result of this move is that the string is "aaca", of which only
 "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
*/
#include <algorithm>
#include <iostream>

using namespace std;
class Solution {
   public:
    string removeDuplicates(string s) {
        int i = 0, n = s.length();
        for (int j = 0; j < n; ++j, ++i) {
            s[i] = s[j];
            if (i > 0 && s[i - 1] == s[i])  // count = 2
                i -= 2;
        }
        return s.substr(0, i);
    }
};

/*
Time: O(n) for one pass
Space: O(n) for output, but if we don't consider output O(1)
*/