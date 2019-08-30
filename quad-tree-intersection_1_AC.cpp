// https://leetcode.com/problems/quad-tree-intersection/
// ugly solution
/*
// Definition for a QuadTree node.
class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node() {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};
*/
class Solution {
public:
    Node* intersect(Node* quadTree1, Node* quadTree2) {
        if (quadTree1 == nullptr) {
            return quadTree2;
        }
        if (quadTree2 == nullptr) {
            return quadTree1;
        }
        return intersectRecursive(quadTree1, quadTree1->val, quadTree2, quadTree2->val);
    }
private:
    Node* intersectRecursive(Node* t1, bool v1, Node* t2, bool v2) {
        bool leaf1 = (t1 == nullptr || t1->isLeaf);
        bool leaf2 = (t2 == nullptr || t2->isLeaf);
        Node* t = new Node(v1 || v2, true, nullptr, nullptr, nullptr, nullptr);
        if (leaf1 && leaf2) {
            return t;
        }
        t->isLeaf = false;
        Node* ttl = (t->topLeft = intersectRecursive(leaf1 ? nullptr : t1->topLeft, leaf1 ? v1 : t1->topLeft->val,
                leaf2 ? nullptr : t2->topLeft, leaf2 ? v2 : t2->topLeft->val));
        Node* ttr = (t->topRight = intersectRecursive(leaf1 ? nullptr : t1->topRight, leaf1 ? v1 : t1->topRight->val,
                leaf2 ? nullptr : t2->topRight, leaf2 ? v2 : t2->topRight->val));
        Node* tbl = (t->bottomLeft = intersectRecursive(leaf1 ? nullptr : t1->bottomLeft, leaf1 ? v1 : t1->bottomLeft->val,
                leaf2 ? nullptr : t2->bottomLeft, leaf2 ? v2 : t2->bottomLeft->val));
        Node* tbr = (t->bottomRight = intersectRecursive(leaf1 ? nullptr : t1->bottomRight, leaf1 ? v1 : t1->bottomRight->val,
                leaf2 ? nullptr : t2->bottomRight, leaf2 ? v2 : t2->bottomRight->val));
        bool v = ttl->val;
        t->val = v;
        if (ttl->isLeaf && ttr->isLeaf && tbl->isLeaf && tbr->isLeaf &&
                v == ttr->val && v == tbl->val && v == tbr->val) {
            t->isLeaf = true;
            deleteRecursive(t->topLeft);
            deleteRecursive(t->topRight);
            deleteRecursive(t->bottomLeft);
            deleteRecursive(t->bottomRight);
        } else {
            t->isLeaf = false;
        }
        return t;
    }

    void deleteRecursive(Node* &t) {
        if (t == nullptr) {
            return;
        }
        deleteRecursive(t->topLeft);
        deleteRecursive(t->topRight);
        deleteRecursive(t->bottomLeft);
        deleteRecursive(t->bottomRight);
        delete t;
        t = nullptr;
    }
};
