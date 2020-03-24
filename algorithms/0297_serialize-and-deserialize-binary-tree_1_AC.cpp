// Preorder traversal
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <cstdio>
#include <string>
using std::sscanf;
using std::string;
using std::to_string;

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s = "";
        serializeTraverse(root, s);
        s.pop_back();
        return s;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int idx = 0;
        return deserializeTraverse(data, idx);
    }
private:
    static const char CHAR_NULL = '#';
    static const char CHAR_SPC = ' ';
    
    void serializeTraverse(TreeNode *root, string &s) {
        if (root == NULL) {
            s.push_back(CHAR_NULL);
            s.push_back(CHAR_SPC);
            return;
        }
        s += to_string(root->val);
        s.push_back(CHAR_SPC);
        serializeTraverse(root->left, s);
        serializeTraverse(root->right, s);
    }
    
    TreeNode *deserializeTraverse(const string &s, int &idx) {
        int ls = s.size();
        if (idx >= ls) {
            return NULL;
        }
        
        TreeNode *root;
        
        if (s[idx] == CHAR_NULL) {
            root = NULL;
            idx += 2;
            return root;
        }
        
        int val = 0;
        string s1 = "";
        while (idx < ls && s[idx] != CHAR_SPC) {
            s1.push_back(s[idx++]);
        }
        sscanf(s1.data(), "%d", &val);
        ++idx;
        
        root = new TreeNode(val);
        root->left = deserializeTraverse(s, idx);
        root->right = deserializeTraverse(s, idx);
        
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
