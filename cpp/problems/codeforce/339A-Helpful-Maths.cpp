#include <bits/stdc++.h>
using namespace std;
string s;
string hold;
int main() {
  cin >> s;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] != '+') {
      hold.push_back(s[i]);
    }
  }
  sort(hold.begin(), hold.end());
  cout << hold[0];

  for (int i = 1; i < hold.size(); i++) {
    cout << "+" << hold[i];
  }
}