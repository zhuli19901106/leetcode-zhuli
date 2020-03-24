/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <cctype>
#include <stack>
#include <string>
using std::isdigit;
using std::stack;
using std::string;

class Solution {
public:
    TreeNode* str2tree(string s) {
        int ls = s.size();
        if (ls == 0) {
            return NULL;
        }
        
        stack<TreeNode *> sp;
        stack<int> si;
        
        int i;
        int n, f;
        TreeNode *p;
        
        i = 0;
        while (i < ls) {
            if (s[i] == '+' || s[i] == '-' || isdigit(s[i])) {
                f = (s[i] == '-' ? -1 : +1);
                n = (isdigit(s[i]) ? s[i] - '0' : 0);
                ++i;
                while (i < ls && isdigit(s[i])) {
                    n = n * 10 + (s[i++] - '0');
                }
                p = new TreeNode(f * n);
                if (sp.empty()) {
                    // Do nothing
                } else if (si.top() == 0) {
                    sp.top()->left = p;
                } else {
                    sp.top()->right = p;
                }
                sp.push(p);
                si.push(0);
            } else if (s[i] == '(') {
                ++i;
            } else if (s[i] == ')') {
                sp.pop();
                si.pop();
                ++si.top();
                ++i;
            } else {
                ++i;
            }
        }
        p = sp.top();
        
        while (!sp.empty()) {
            sp.pop();
            si.pop();
        }
        
        return p;
    }
};
