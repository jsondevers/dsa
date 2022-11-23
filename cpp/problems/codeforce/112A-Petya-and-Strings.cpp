#include <bits/stdc++.h>
using namespace std;

int main() {
  int count = 0;
  string one, two;
  cin >> one >> two;
  if (one.size() != two.size()) {
    cout << "-1";
  } else {
    for (int i = 0; i < one.size(); i++) {
      one[i] = tolower(one[i]);
      two[i] = tolower(two[i]);
    }
    if (one < two) {
      cout << "-1";
    } else if (one > two) {
      cout << "1";
    } else {
      cout << "0";
    }
  }
}