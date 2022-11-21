/*
You are given an m x n matrix maze (0-indexed) with empty cells (represented as
'.') and walls (represented as '+'). You are also given the entrance of the
maze, where entrance = [entrancerow, entrancecol] denotes the row and column of
the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step
into a cell with a wall, and you cannot step outside the maze. Your goal is to
find the nearest exit from the entrance. An exit is defined as an empty cell
that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest
exit, or -1 if no such path exists.


Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance=
[1,2] Output: 1 Explanation: There are 3 exits in this maze at [1,0], [0,2], and
[2,3]. Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
*/

// BFS
#include <array>
#include <queue>
#include <vector>
using std::array;
using std::queue;
using std::vector;
class Solution {
 public:
  int dirx[4] = {-1, 0, 0, 1};
  int diry[4] = {0, 1, -1, 0};
  int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
    int m = maze.size(), n = maze[0].size();
    queue<array<int, 3>> q;  // {i, j, steps}
    // push the starting point (i, j) with initial step 0
    q.push({entrance[0], entrance[1], 0});
    // BFS
    while (!q.empty()) {
      auto [i, j, steps] = q.front();
      q.pop();
      // handle exit condition, we can exit if
      // 1. the current position is not the entrance
      bool isAtTheEntrance = i == entrance[0] && j == entrance[1];
      // 2. and the current position is at the border
      bool isAtTheBorder = i == 0 || j == 0 || i == m - 1 || j == n - 1;
      if (!isAtTheEntrance && isAtTheBorder) return steps;
      // try for 4 directions
      for (int d = 0; d < 4; d++) {
        int next_i = i + dirx[d];
        int next_j = j + diry[d];
        // check if we can move to (next_i, next_j)
        if (next_i >= 0 && next_j >= 0 && next_i < m && next_j < n &&
            maze[next_i][next_j] == '.') {
          // if so, we mark the next cell to `+` so that we won't visit it again
          maze[next_i][next_j] = '+';
          // add the next position to the queue with steps + 1
          q.push({next_i, next_j, steps + 1});
        }
      }
    }
    return -1;
  }
};

/* Time complexity: O(m \cdot n)O(m⋅n)

For each visited cell, we add it to queue and pop it from queue once, which
takes constant time as the operation on queue requires O(1)O(1) time. For each
cell in queue, we mark it as visited in maze, and check if it has any unvisited
neighbors in all four directions. This also takes constant time. In the
worst-case scenario, we may have to visit O(m \cdot n)O(m⋅n) cells before the
iteration stops. To sum up, the overall time complexity is O(m \cdot n)O(m⋅n).
Space complexity: O(max(m, n))O(max(m,n))

We modify the input matrix maze in-place to mark each visited cell, it requires
constant space. We use a queue queue to store the cells to be visited. In the
worst-case scenario, there may be O(m + n)O(m+n) cells stored in queue. The
space complexity is O(m + n) + O(max(m, n))O(m+n)+O(max(m,n)).*/