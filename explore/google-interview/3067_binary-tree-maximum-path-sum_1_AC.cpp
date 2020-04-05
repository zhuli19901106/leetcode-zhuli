// Recursion is fine, just don't repeat it too many times.
// Your stack is gonna blow.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    int maxPathSum(TreeNode* root) {
        if (root == NULL) {
            return 0;
        }
        
        oneSum(root);
        twoSum(root);
        return sum_two[root];
    }
    
    ~Solution() {
        
    }
private:
    unordered_map<TreeNode *, int> sum_one, sum_two;
    
    int twoSum(TreeNode *root) {
        if (sum_one.find(root) == sum_one.end()) {
            oneSum(root);
        }
        if (sum_two.find(root) != sum_two.end()) {
            return sum_two[root];
        }
        
        int res = root->val;
        if (root->left != NULL) {
            res += max(0, sum_one[root->left]);
        }
        if (root->right != NULL) {
            res += max(0, sum_one[root->right]);
        }
        
        if (root->left != NULL) {
            res = max(res, twoSum(root->left));
        }
        if (root->right != NULL) {
            res = max(res, twoSum(root->right));
        }
        sum_two[root] = res;
        
        return sum_two[root];
    }
    
    int oneSum(TreeNode *root) {
        if (sum_one.find(root) != sum_one.end()) {
            return sum_one[root];
        }
        
        int s = 0;
        if (root->left != NULL) {
            s = max(s, oneSum(root->left));
        }
        if (root->right != NULL) {
            s = max(s, oneSum(root->right));
        }
        sum_one[root] = root->val + s;
        
        return sum_one[root];
    }
};
