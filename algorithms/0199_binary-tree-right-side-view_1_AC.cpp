// Level-order traversal
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <queue>
#include <utility>
using std::make_pair;
using std::pair;
using std::queue;

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (root == NULL) {
            return res;
        }
        
        pair<TreeNode *, int> p1, p2;
        queue<pair<TreeNode *, int>> q;
        TreeNode *ptr;
        
        q.push(make_pair(root, 0));
        while (!q.empty()) {
            p1 = q.front();
            q.pop();
            if (q.empty() || q.front().second > p1.second) {
                res.push_back((p1.first)->val);
            }
            ptr = p1.first;
            p2.second = p1.second + 1;
            if (ptr->left != NULL) {
                p2.first = ptr->left;
                q.push(p2);
            }
            if (ptr->right != NULL) {
                p2.first = ptr->right;
                q.push(p2);
            }
        }
        return res;
    }
};
