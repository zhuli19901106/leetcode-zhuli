// I don't know why such boring problems should appear one after one on Leetcode.
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
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if (d <= 0) {
            return root;
        }
        
        TreeNode *p;
        if (d == 1) {
            p = new TreeNode(v);
            p->left = root;
            return p;
        }
        
        queue<pair<TreeNode *, int>> q;
        q.push(make_pair(root, 1));
        
        TreeNode *p1, *p2;
        pair<TreeNode *, int> pr;
        while (!q.empty()) {
            pr = q.front();
            q.pop();
            
            p = pr.first;
            if (pr.second < d - 1) {
                if (p->left != NULL) {
                    q.push(make_pair(p->left, pr.second + 1));
                }
                if (p->right != NULL) {
                    q.push(make_pair(p->right, pr.second + 1));
                }
            } else {
                p1 = p->left;
                p->left = new TreeNode(v);
                p->left->left = p1;
                
                p2 = p->right;
                p->right = new TreeNode(v);
                p->right->right = p2;
            }
        }
        
        return root;
    }
};
