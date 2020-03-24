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
    vector<vector<int>> levelOrder(Node* root) {
        vector<vector<int>> result;
        traverse(root, 0, result);
        return result;
    }
private:
    void traverse(Node *root, int depth, vector<vector<int>> &result) {
        if (root == nullptr) {
            return;
        }
        if (depth >= result.size()) {
            result.emplace_back(vector<int>());
        }
        result[depth].emplace_back(root->val);
        for (auto &node: root->children) {
            traverse(node, depth + 1, result);
        }
    }
};
