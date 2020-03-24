// When it comes to pattern matching in structured data, you need serialization.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::to_string;
using std::unordered_map;
using std::vector;

class Solution {
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        vector<TreeNode *> res;
        if (root == NULL) {
            return res;
        }
        
        serialize(root);
        for (auto &p: um) {
            if (p.second.size() > 1) {
                res.push_back(p.second[0]);
            }
        }
        um.clear();
        
        return res;
    }
private:
    unordered_map<string, vector<TreeNode *>> um;
    
    string serialize(TreeNode *root) {
        if (root == NULL) {
            return "null";
        }
        string sl = serialize(root->left);
        string sr = serialize(root->right);
        string s = "{" + to_string(root->val) + "," + sl + "," + sr + "}";
        um[s].push_back(root);
        
        return s;
    }
};
