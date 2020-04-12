// Iterative solution using <queue>
#include <queue>
#include <utility>
using std::make_pair;
using std::pair;
using std::queue;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> v;
        if (root == NULL) {
            return v;
        }
        queue<pair<int, TreeNode*>> q;
        pair<int, TreeNode*> p;
        
        q.push(make_pair(0, root));
        TreeNode* ptr;
        while (!q.empty()) {
            p = q.front();
            ptr = p.second;
            q.pop();
            
            while (v.size() <= p.first) {
                v.push_back(vector<int>());
            }
            v[p.first].push_back(ptr->val);
            
            if (ptr->left != NULL) {
                q.push(make_pair(p.first + 1, ptr->left));
            }
            if (ptr->right != NULL) {
                q.push(make_pair(p.first + 1, ptr->right));
            }
        }
        return v;
   }
};
