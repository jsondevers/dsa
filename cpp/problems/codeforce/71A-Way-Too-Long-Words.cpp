#include <bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  while (n != 0) {
    string s;
    cin >> s;
    if (s.size() > 10) {
      char first = s[0];
      char last = s[s.size() - 1];
      cout << first << (s.size() - 2) << last << "\n";
    } else {
      cout << s << "\n";
    }

    n--;
  }
}