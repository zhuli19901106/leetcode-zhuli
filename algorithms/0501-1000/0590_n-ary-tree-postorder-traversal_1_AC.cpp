// easy
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/
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
class Solution {
public:
    vector<int> postorder(Node* root) {
        vector<int> result;
        postorderRecursive(root, result);

        return result;
    }
private:
    void postorderRecursive(Node* root, vector<int> &result) {
        if (root == nullptr) {
            return;
        }

        vector<Node*> &children = root->children;
        for (vector<Node*>::iterator vit = children.begin(); vit != children.end(); ++vit) {
            postorderRecursive(*vit, result);
        }
        result.push_back(root->val);
    }
};
