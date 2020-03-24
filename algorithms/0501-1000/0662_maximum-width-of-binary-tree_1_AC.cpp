/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <algorithm>
#include <cstdint>
#include <unordered_map>
using std::max;
using std::min;
using std::unordered_map;

class Solution {
public:
    int widthOfBinaryTree(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        traverse(root, 0, 0);
        
        int64_t res = 0;
        int dep;
        for (auto &p: um_max) {
            dep = p.first;
            res = max(res, um_max[dep] - um_min[dep]);
        }
        um_max.clear();
        um_min.clear();
        
        return res + 1;
    }
private:
    unordered_map<int, int64_t> um_max, um_min;
    
    void traverse(TreeNode *root, int dep, int64_t path) {
        if (root == NULL) {
            return;
        }
        
        int64_t cur;
        if (um_max.find(dep) == um_max.end()) {
            um_max[dep] = path;
        } else {
            cur = um_max[dep];
            um_max[dep] = max(cur, path);
        }
        
        if (um_min.find(dep) == um_min.end()) {
            um_min[dep] = path;
        } else {
            cur = um_min[dep];
            um_min[dep] = min(cur, path);
        }
        
        traverse(root->left, dep + 1, path << 1);
        traverse(root->right, dep + 1, (path << 1) | 1);
    }
};
