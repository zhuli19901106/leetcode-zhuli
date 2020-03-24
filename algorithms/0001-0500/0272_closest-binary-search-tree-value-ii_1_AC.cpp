// 1AC, think about iterator and reverse iterator.
// The difficult part is to locate the target position in O(log(n)) time.
// This is what we call OOP.
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
#include <cmath>
#include <stack>
#include <vector>
using std::abs;
using std::reverse;
using std::stack;
using std::vector;

class TreeIterator {
public:
    TreeIterator(TreeNode *root) {
        TreeNode *p = root;
        while (p != NULL) {
            st.push(p);
            p = p->left;
        }
    }
    
    TreeIterator(TreeNode *root, double target) {
        TreeNode *p = root;
        while (p != NULL) {
            if (p->val < target) {
                p = p->right;
            } else {
                st.push(p);
                p = p->left;
            }
        }
    }
    
    bool hasNext() {
        return !st.empty();
    }
    
    int next() {
        TreeNode *p = st.top();
        st.pop();
        
        TreeNode *q = p->right;
        while (q != NULL) {
            st.push(q);
            q = q->left;
        }
        
        return p->val;
    }
    
    int peek() {
        return st.top()->val;
    }
    
    ~TreeIterator() {
        while (!st.empty()) {
            st.pop();
        }
    }
private:
    stack<TreeNode *> st;
};

class TreeReverseIterator {
public:
    TreeReverseIterator(TreeNode *root) {
        TreeNode *p = root;
        while (p != NULL) {
            st.push(p);
            p = p->right;
        }
    }
    
    TreeReverseIterator(TreeNode *root, double target) {
        TreeNode *p = root;
        while (p != NULL) {
            if (p->val > target) {
                p = p->left;
            } else {
                st.push(p);
                p = p->right;
            }
        }
    }
    
    bool hasNext() {
        return !st.empty();
    }
    
    int next() {
        TreeNode *p = st.top();
        st.pop();
        
        TreeNode *q = p->left;
        while (q != NULL) {
            st.push(q);
            q = q->right;
        }
        
        return p->val;
    }
    
    int peek() {
        return st.top()->val;
    }
    
    ~TreeReverseIterator() {
        while (!st.empty()) {
            st.pop();
        }
    }
private:
    stack<TreeNode *> st;
};

class Solution {
public:
    vector<int> closestKValues(TreeNode* root, double target, int k) {
        TreeIterator it1(root, target);
        TreeReverseIterator it2(root, target);
        
        if (it1.hasNext() && it2.hasNext() && it1.peek() == it2.peek()) {
            (void)it1.next();
        }
        
        vector<int> v1, v2;
        vector<int> res;
        int i;
        int c1, c2;
        for (i = 0; i < k; ++i) {
            if (!it1.hasNext() && !it2.hasNext()) {
                break;
            }
            if (!it1.hasNext()) {
                v2.push_back(it2.next());
                continue;
            }
            if (!it2.hasNext()) {
                v1.push_back(it1.next());
                continue;
            }
            
            c1 = it1.peek();
            c2 = it2.peek();
            if (abs(c1 - target) < abs(c2 - target)) {
                v1.push_back(it1.next());
            } else {
                v2.push_back(it2.next());
            }
        }
        reverse(v1.begin(), v1.end());
        res.insert(res.end(), v1.begin(), v1.end());
        res.insert(res.end(), v2.begin(), v2.end());
        
        v1.clear();
        v2.clear();
        return res;
    }
};
