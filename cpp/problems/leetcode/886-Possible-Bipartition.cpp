#include <bits/stdc++.h>
using namespace std;

/*
Union Find
Time: O(N + E) for T operations the amortized time complexity of union find is
O(alpha(T)) where (alpha(T)) is the inverse ackerman function that grows super
slowly and usually considered to be O(1), thus the E operations (iterating over
each edge) we perform results in O(E) time

We initialize parent and rank arrays that each need O(N) time
We loop through all nodes, which is O(N) time

Space: O(N + E) parent and rank arrays take up O(N) space search
O(E) space is also required for adj list
*/
class UnionFind {
private:
  vector<int> parent, rank;

public:
  UnionFind(int size) {
    parent.resize(size);
    rank.resize(size, 0);

    for (int i = 0; i < size; i++) {
      parent[i] = i;
    }
  }

  int find(int x) {
    if (parent[x] != x)
      parent[x] = find(parent[x]);
    return parent[x];
  }

  void union_set(int x, int y) {
    int xset = find(x), yset = find(y);
    if (xset == yset) {
      return;
    } else if (rank[xset] < rank[yset]) {
      parent[xset] = yset;
    } else if (rank[xset] > rank[yset]) {
      parent[yset] = xset;
    } else {
      parent[yset] = xset;
      rank[xset]++;
    }
  }
};

class Solution {
public:
  bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
    vector<vector<int>> adj(n + 1);
    for (auto &dislike : dislikes) {
      adj[dislike[0]].push_back(dislike[1]);
      adj[dislike[1]].push_back(dislike[0]);
    }

    UnionFind dsu(n + 1);
    for (int node = 1; node <= n; node++) {
      for (int neighbor : adj[node]) {
        // Check if the node and its neighbor is in the same set.
        if (dsu.find(node) == dsu.find(neighbor))
          return false;
        // Move all the neighbours into same set as the first neighbour.
        dsu.union_set(adj[node][0], neighbor);
      }
    }
    return true;
  }
};

/*
DFS
Time: O(N + E) visit N nodes, adds E edges
Spaec: Recursive call stack worst case is O(N), required O(E) and O(N) space
for the adj list and the color array
*/
class Solution {
public:
  bool dfs(int node, int nodeColor, vector<vector<int>> &adj,
           vector<int> &color) {
    color[node] = nodeColor;
    for (auto &neighbor : adj[node]) {
      if (color[neighbor] == color[node])
        return false;
      if (color[neighbor] == -1) {
        if (!dfs(neighbor, 1 - color[node], adj, color))
          return false;
      }
    }
    return true;
  }

  bool possibleBipartition(int n, vector<vector<int>> &dislikes) {
    vector<vector<int>> adj(n + 1);
    for (auto &dislike : dislikes) {
      adj[dislike[0]].push_back(dislike[1]);
      adj[dislike[1]].push_back(dislike[0]);
    }
    vector<int> color(n + 1, -1); // 0 stands for red and 1 stands for blue.
    for (int i = 1; i <= n; i++) {
      if (color[i] == -1) {
        // For each pending component, run DFS.
        if (!dfs(i, 0, adj, color))
          // Return false, if there is conflict in the component.
          return false;
      }
    }
    return true;
  }
};