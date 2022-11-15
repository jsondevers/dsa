#include <iostream>
#include <vector>
using namespace std;
class Solution {
   public:
    // Constant to map y-coordinates of stones
    const int K = 10001;  // this is the size of constraints
    void dfs(vector<vector<int>>& stones, vector<int> adj[], vector<int>& visited, int src) {
        // Mark the stone as visited
        visited[src] = 1;

        // Iterate over the adjacent, and iterate over it if not visited yet
        for (int adjacent : adj[src]) {
            if (visited[adjacent] == 0) {
                dfs(stones, adj, visited, adjacent);
            }
        }
    }

    int removeStones(vector<vector<int>>& stones) {
        // Adjacency list to store edges
        vector<int> adj[2 * K + 1];
        for (int i = 0; i < stones.size(); i++) {
            int x = stones[i][0];
            int y = stones[i][1] + K;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        // Array to mark visited stones
        vector<int> visited(2 * K + 1, 0);
        // Counter for connected components
        int componentCount = 0;
        for (int i = 0; i < 2 * K + 1; i++) {
            if (visited[i] == 0 && adj[i].size() > 0) {
                // If the stone is not visited yet,
                // Start the DFS and increment the counter
                componentCount++;
                dfs(stones, adj, visited, i);
            }
        }

        // Return the maximum stone that can be removed
        return stones.size() - componentCount;
    }
};