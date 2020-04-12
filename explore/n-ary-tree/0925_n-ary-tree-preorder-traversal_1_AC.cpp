// https://leetcode.com/problems/n-ary-tree-preorder-traversal/
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/
#include <vector>
using std::vector;

class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> result;
        preorderRecursive(root, result);

        return result;
    }
private:
    void preorderRecursive(Node* root, vector<int> &result) {
        if (root == nullptr) {
            return;
        }

        result.push_back(root->val);
        vector<Node*> &children = root->children;
        for (vector<Node*>::iterator vit = children.begin(); vit != children.end(); ++vit) {
            preorderRecursive(*vit, result);
        }
    }
};
