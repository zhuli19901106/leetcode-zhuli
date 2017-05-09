/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <cstdint>
#include <string>
#include <vector>
using std::string;
using std::to_string;
using std::vector;

class Solution {
public:
    bool isSubtree(TreeNode *s, TreeNode *t) {
        string vs = "", vt = "";
        
        serialize(s, vs);
        vs.pop_back();
        serialize(t, vt);
        vt.pop_back();
        
        return strStr(vs, vt) != -1;
    }
private:
    static const uint64_t I_P = 31;
    
    void serialize(TreeNode *root, string &s) {
        if (root == NULL) {
            s.push_back('#');
            s.push_back(' ');
            return;
        }
        s.push_back('{');
        s += to_string(root->val);
        s.push_back(' ');
        serialize(root->left, s);
        serialize(root->right, s);
        s.push_back('}');
    }
    
    int strStr(const string &s, const string &p) {
        int ls = s.size();
        int lp = p.size();
        
        if (lp == 0) {
            return 0;
        }
        if (ls < lp) {
            return -1;
        }
        
        uint64_t hp = 0;
        int i;
        for (i = 0; i < lp; ++i) {
            hp = hp * I_P + p[i];
        }
        
        uint64_t b = 1;
        for (i = 0; i < lp; ++i) {
            b *= I_P;
        }
        b = ~b + 1;
        
        uint64_t hs = 0;
        for (i = 0; i < lp; ++i) {
            hs = hs * I_P + s[i];
        }
        while (i < ls) {
            if (hs == hp) {
                return i - lp;
            }
            hs = hs * I_P + s[i] + s[i - lp] * b;
            ++i;
        }
        if (hs == hp) {
            return i - lp;
        }
        return -1;
    }
};
