// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
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
#include <algorithm>
#include <vector>
using std::max;
using std::vector;

class Solution {
public:
    int maxDepth(Node* root) {
        if (root == nullptr) {
            return 0;
        }
        int res = 1;
        for (vector<Node*>::iterator vit = root->children.begin(); vit != root->children.end(); ++vit) {
            res = max(res, maxDepth(*vit) + 1);
        }
        return res;
    }
};
