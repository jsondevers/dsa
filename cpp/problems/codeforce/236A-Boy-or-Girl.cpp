#include <bits/stdc++.h>
using namespace std;
string s;
int main() {
  cin >> s;
  set<char> gender(begin(s), end(s));
  if (gender.size() % 2) {
    cout << "IGNORE HIM!";
  } else {
    cout << "CHAT WITH HER!";
  }
}