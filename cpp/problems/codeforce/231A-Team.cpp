#include <bits/stdc++.h>
using namespace std;
int main() {
  int sure = 0;
  int n;
  cin >> n;
  while (n != 0) {
    int p, v, t;
    cin >> p >> v >> t;
    if (p + v + t >= 2) {
      sure++;
    }
    n--;
  }
  cout << sure;
}