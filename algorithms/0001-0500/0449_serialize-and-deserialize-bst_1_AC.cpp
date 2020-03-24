// Make sure your code compiles and runs before trying anything, wise guy.
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
#include <sstream>
using std::stringstream;
using std::to_string;

// NULL is represented as a '#', values are split by a ' '.
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string s = "";
        serialPreorder(root, s);
        s.pop_back();
        return s;
    }
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int idx = 0;
        return deserialPreorder(data, idx);
    }
private:
    static const char CHAR_NULL = '#';
    static const char CHAR_SPACE = ' ';
    
    void serialPreorder(TreeNode* root, string &s) {
        if (root == NULL) {
            s.push_back(CHAR_NULL);
            s.push_back(CHAR_SPACE);
            return;
        }
        s += to_string(root->val);
        s.push_back(CHAR_SPACE);
        serialPreorder(root->left, s);
        serialPreorder(root->right, s);
    }
    
    TreeNode* deserialPreorder(const string &s, int &idx) {
        if (idx >= s.size()) {
            return NULL;
        }
        string tk = "";
        int ls = s.size();
        while (idx < ls && s[idx] != CHAR_SPACE) {
            tk.push_back(s[idx++]);
        }
        while (idx < ls && s[idx] == CHAR_SPACE) {
            ++idx;
        }
        if (tk[0] == CHAR_NULL) {
            return NULL;
        }
        
        stringstream ss;
        ss << tk;
        int val;
        ss >> val;
        
        TreeNode *root = new TreeNode(val);
        root->left = deserialPreorder(s, idx);
        root->right = deserialPreorder(s, idx);
        return root;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
