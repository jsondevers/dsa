#include <bits/stdc++.h>
using namespace std;
int arr[5][5];
int x, y;
int main() {
  int value;
  int moves = 0;

  for (int row = 0; row < 5; row++) {
    for (int col = 0; col < 5; col++) {
      cin >> value;
      if (value == 1) {
        x = row;
        y = col;
      }
      arr[row][col] = value;
    }
  }

  while (x != 2) {
    if (x < 2) {
      x++;
    } else {
      x--;
    }
    moves++;
  }
  while (y != 2) {
    if (y < 2) {
      y++;
    } else {
      y--;
    }
    moves++;
  }
  cout << moves;
}