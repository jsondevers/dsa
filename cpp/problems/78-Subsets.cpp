#include <iostream>
#include <vector>
using std::vector;
class Solution {
 public:
  vector<vector<int>> subsets(vector<int>& nums) {
    vector<int> curSet;
    vector<vector<int>> subsets;
    helper(0, nums, curSet, subsets);
    return subsets;
  }

 private:
  void helper(int index, vector<int>& nums, vector<int>& curSet,
              vector<vector<int>>& subsets) {
    if (index == nums.size()) {
      subsets.push_back(curSet);
    } else {
      curSet.push_back(nums[index]);
      helper(index + 1, nums, curSet, subsets);
      curSet.pop_back();

      helper(index + 1, nums, curSet, subsets);
    }
  }
};