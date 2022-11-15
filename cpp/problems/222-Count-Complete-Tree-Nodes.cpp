/*
Given the root of a complete binary tree, return the number of the nodes in the
tree.

According to Wikipedia, every level, except possibly the last, is completely
filled in a complete binary tree, and all nodes in the last level are as far
left as possible. It can have between 1 and 2h nodes inclusive at the last level
h.

Design an algorithm that runs in less than O(n) time complexity.
*/

// Definition for a binary tree node.
#include <iostream>
#include <queue>
using std::queue;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

/* My solution, BFS
Time: O(n)
Space: O(n) -> size of queue
*/
class Solution {
   public:
    int countNodes(TreeNode *root) {
        queue<TreeNode *> queue;

        if (root) {
            queue.push(root);
        } else {
            return 0;
        }

        int complete = 1;
        while (queue.size() > 0) {
            int length = queue.size();
            for (int i = 0; i < length; i++) {
                TreeNode *curr = queue.front();
                queue.pop();
                if (curr->left) {
                    queue.push(curr->left);
                    complete++;
                }
                if (curr->right) {
                    queue.push(curr->right);
                    complete++;
                }
            }
        }
        return complete;
    }
};

/* Recursive
Time: O(n)
Space: O(n) -> size of callstack
*/
class Solution {
   public:
    int countNodes(TreeNode *root) {
        return root != NULL
                   ? 1 + countNodes(root->right) + countNodes(root->left)
                   : 0;
    }
};