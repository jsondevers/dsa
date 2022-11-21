#include <bits/stdc++.h>
using namespace std;
int n, k, i = 0, advances = 0, arr[51];

int main() {
  cin >> n >> k;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  while (arr[advances] && arr[advances] >= arr[k - 1]) {
    ++advances;
  }
  cout << advances;
}