// Just how many ways do you need to traverse a binary tree?
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
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>
using std::max;
using std::make_pair;
using std::min;
using std::pair;
using std::queue;
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<vector<int>> verticalOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root == NULL) {
            return res;
        }
        
        unordered_map<int, vector<int>> um;
        int min_i = 0;
        int max_i = 0;
        
        // Level-order traversal
        queue<pair<int, TreeNode *>> q;
        q.push(make_pair(0, root));
        
        TreeNode *p;
        int i;
        while (!q.empty()) {
            i = q.front().first;
            min_i = min(min_i, i);
            max_i = max(max_i, i);
            
            p = q.front().second;
            q.pop();
            um[i].push_back(p->val);
            
            if (p->left != NULL) {
                q.push(make_pair(i - 1, p->left));
            }
            if (p->right != NULL) {
                q.push(make_pair(i + 1, p->right));
            }
        }
        
        for (i = min_i; i <= max_i; ++i) {
            res.push_back(um[i]);
        }
        um.clear();
        
        return res;
    }
};
