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
#include <unordered_map>
using std::abs;
using std::unordered_map;

class Solution {
public:
    Solution() {
        tilt[NULL] = 0;
        sum[NULL] = 0;
        tiltSum[NULL] = 0;
    }
    
    int findTilt(TreeNode *root) {
        if (tiltSum.find(root) == tiltSum.end()) {
            int sl = findSum(root->left);
            int sr = findSum(root->right);
            tilt[root] = abs(sl - sr);
            tiltSum[root] = tilt[root] + findTilt(root->left) + findTilt(root->right);
        }
        return tiltSum[root];
    }
    
    ~Solution() {
        tilt.clear();
        sum.clear();
        tiltSum.clear();
    }
private:
    unordered_map<TreeNode *, int> tilt, sum, tiltSum;
    
    int findSum(TreeNode *root) {
        if (sum.find(root) == sum.end()) {
            sum[root] = root->val + findSum(root->left) + findSum(root->right);
        }
        return sum[root];
    }
};
