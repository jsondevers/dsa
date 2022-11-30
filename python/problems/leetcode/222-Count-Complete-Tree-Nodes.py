"""
Given the root of a complete binary tree, return the 
number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, 
is completely filled in a complete binary tree, and all nodes in the 
last level are as far left as possible. It can have between 1 and 2^h 
nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
"""

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root:
            q.append(root)
        else:
            return 0

        complete = 1
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    complete += 1
                if curr.right:
                    q.append(curr.right)
                    complete += 1
                else:
                    break

        return complete


"""
Time: O(N) -> BFS
Space: O(N) -> Size of deque
"""


# recursive
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return (
            1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0
        )


"""
Time: O(N) -> reach all nodes 
Space: O(logN) -> size of tree
"""

# really interesting binary search solution from leetcode
class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2**d - 1) + left


"""
Time: O(d^2) = O(log^2 N) where d is tree depth
Space: O(1)
"""


"""
Binary Search Explanation:
In a complete binary tree every level, 
except possibly the last, is completely filled, 
and all nodes in the last level are as far left as possible.

That means that complete tree has 2^k nodes in the kth level 
if the kth level is not the last one. The last level may be not 
filled completely, and hence in the last level the number of nodes could 
vary from 1 to 2^d where d is a tree depth.

Compute the number of nodes in all levels but the last one, reducing the problem
to 2^d - 1, reducing the problem to the simple check of how 
many nodes the tree has in the last level.

Tree has 2^d nodes on all levels but the last one

Last Level: 1 <= nodes <= 2^d

Total number of nodes: 2^d - 1 + last_level_nodes

2 Questions:
1.) How many nodes in the last level have to be checked?
    a.) We know it's a complete tree meaning that all nodes are as far left as
    possible. Meaning that checking the existence of all 2^d possible leafs,
    one could use binary search and check log(2^d) = d leafs only

2.) What is the best time performance for each check?
    a.) enumerate potential nodes in the last level from 0 to 2^d - 1. How to check
    if node index exists? -> Binary search to reconstruct the sequence of moves 
    from root to index node. Time complexity for one check is O(d)

1 and 2 result in O(d) checks, each check at a price of O(d). That means that the 
overall time complexity would be O(d^2)

Algorithm:
    1.) Return tree if its empty
    2.) compute tree depth d
    3.) return 1 if d == 0
    4.) number of nodes on all levels but last is 2^d - 1. The number of nodes can
        vary from  1 to 2^d. Enumerate potential nodes from 0 to 2^d - 1 and perform
        binary search by the node index to check how many nodes are in the last level.
        Use function exists(index, d, root) to check if the node with index exists.
    5.) binary search to implement exists(index, d, root)
    6.) return 2^d - 1 + last_level_nodes


"""
