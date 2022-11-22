#include <bits/stdc++.h>
using namespace std;
int n;
int main() {
  int res = 0;
  cin >> n;

  while (n) {
    string statement;
    cin >> statement;
    if (statement[0] == '+' || statement[2] == '+') {
      res++;
    } else if (statement[0] == '-' || statement[2] == '-') {
      res--;
    }
    n--;
  }
  cout << res;
}