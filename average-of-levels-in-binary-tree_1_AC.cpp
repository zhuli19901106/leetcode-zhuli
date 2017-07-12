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
using std::queue;
using std::pair;

class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        queue<pair<int, TreeNode *>> q;
        vector<double> res;
        vector<int> c;
        
        if (root == NULL) {
            return res;
        }
        
        pair<int, TreeNode *> p;
        int dep;
        TreeNode *node;
        
        q.push(make_pair(0, root));
        while (!q.empty()) {
            p = q.front();
            q.pop();
            
            dep = p.first;
            node = p.second;
            while (res.size() <= dep) {
                res.push_back(0);
                c.push_back(0);
            }
            res[dep] += node->val;
            c[dep] += 1;
            
            if (node->left != NULL) {
                q.push(make_pair(dep + 1, node->left));
            }
            if (node->right != NULL) {
                q.push(make_pair(dep + 1, node->right));
            }
        }
        
        int n = res.size();
        int i;
        for (i = 0; i < n; ++i) {
            res[i] /= c[i];
        }
        c.clear();
        
        return res;
    }
};
