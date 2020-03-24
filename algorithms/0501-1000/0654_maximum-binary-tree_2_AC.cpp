// RMQ problem, very intuitive and efficient, but be careful with the coding.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <cmath>
#include <vector>
using std::log;
using std::vector;

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        auto &v = nums;
        int n = v.size();
        int dep = (int)(log(n) / log(2.0)) + 1;
        
        int i;
        max_idx.resize(dep, vector<int>(n));
        for (i = 0; i < n; ++i) {
            max_idx[0][i] = i;
        }
        
        int j;
        int b2 = 1;
        int i1, i2;
        for (i = 1; i < dep; ++i) {
            for (j = 0; j < n; ++j) {
                i1 = max_idx[i - 1][j];
                if (j + b2 < n) {
                    i2 = max_idx[i - 1][j + b2];
                    max_idx[i][j] = (v[i1] > v[i2]) ? i1 : i2;
                } else {
                    max_idx[i][j] = i1;
                }
            }
            b2 <<= 1;
        }
        
        TreeNode *root;
        traverse(root, nums, 0, n);
        max_idx.clear();
        
        return root;
    }
private:
    vector<vector<int>> max_idx;
    
    int rmq(vector<int> &v, int ll, int rr) {
        int d = 0;
        int b2 = 1;
        int lr, rl;
        while (true) {
            lr = ll + b2;
            rl = rr - b2;
            if (lr >= rl) {
                // two intervals overlap
                break;
            } else {
                // double the interval length
                d += 1;
                b2 <<= 1;
            }
        }
        int i1 = max_idx[d][ll];
        int i2 = max_idx[d][rl];
        return (v[i1] > v[i2]) ? i1 : i2;
    }
    
    void traverse(TreeNode *&root, vector<int> &v, int ll, int rr) {
        if (ll >= rr) {
            root = NULL;
            return;
        }
        int mm = rmq(v, ll, rr);
        root = new TreeNode(v[mm]);
        traverse(root->left, v, ll, mm);
        traverse(root->right, v, mm + 1, rr);
    }
};
