from typing import List

"""
Union Find
Time: O(N + E) for T operations the amortized time complexity of union find is 
O(alpha(T)) where (alpha(T)) is the inverse ackerman function that grows super slowly and usually considered to be O(1), thus the E operations (iterating over each edge) we perform results in O(E) time

We initialize parent and rank arrays that each need O(N) time
We loop through all nodes, which is O(N) time

Space: O(N + E) parent and rank arrays take up O(N) space search 
O(E) space is also required for adj list
"""


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union_set(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1


"""
DFS
Time: O(N + E) visit N nodes, adds E edges
Spaec: Recursive call stack worst case is O(N), required O(E) and O(N) space
for the adj list and the color array 
"""


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        dsu = UnionFind(n + 1)
        for node in range(1, n + 1):
            for neighbor in adj[node]:
                # Check if the node and its neighbor is in the same set.
                if dsu.find(node) == dsu.find(neighbor):
                    return False
                # Move all the neighbours into same set as the first neighbour.
                dsu.union_set(adj[node][0], neighbor)

        return True


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, node_color):
            color[node] = node_color
            for neighbor in adj[node]:
                if color[neighbor] == color[node]:
                    return False
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - node_color):
                        return False

            return True

        adj = [[] for _ in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])

        color = [-1] * (n + 1)  # 0 stands for red and 1 stands for blue.
        for i in range(1, n + 1):
            if color[i] == -1:
                # For each pending component, run DFS.
                if not dfs(i, 0):
                    # Return false, if there is conflict in the component.
                    return False

        return True
