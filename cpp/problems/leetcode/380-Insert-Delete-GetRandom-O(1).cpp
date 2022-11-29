#include <bits/stdc++.h>
using namespace std;
class RandomizedSet {
  // Average Time O(1) & Auxiliary Space O(N)
 private:
  vector<int> a;
  unordered_map<int, int> m;

 public:
  /** Initialize your data structure here. */
  RandomizedSet() {}

  bool insert(int val) {
    if (m.find(val) != m.end())

      return false;
    else {
      a.push_back(val);
      m[val] = a.size() - 1;
      return true;
    }
  }

  /** Removes a value from the array vector. Returns true if the array contained
   * the specified element. */
  bool remove(int val) {
    if (m.find(val) == m.end())
      return false;
    else {
      int last = a.back();

      a.pop_back();
      m[last] = m[val];

      m.erase(val);
      return true;
    }
  }

  /** Get a random element from the array vector */
  int getRandom() { return a[rand() % a.size()]; }
};