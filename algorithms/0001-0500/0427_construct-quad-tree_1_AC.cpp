// medium
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
    Solution() {
        offsets = vector<vector<int>>{{0, 0}, {0, 1}, {1, 0}, {1, 1}};
    }

    Node* construct(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n <= 0) {
            return nullptr;
        }
        return constructRecursive(grid, 0, 0, n >> 1);
    }
private:
    vector<vector<int>> offsets;

    bool isLeaf(vector<vector<int>>& grid, int x, int y, int i) {
        if (i == 0) {
            return true;
        }

        int x1, y1;
        for (auto &offset: offsets) {
            x1 = x + offset[0] * i;
            y1 = y + offset[1] * i;
            if (!isLeaf(grid, x1, y1, i >> 1)) {
                return false;
            }
            if (grid[x][y] != grid[x1][y1]) {
                return false;
            }
        }
        return true;
    }

    Node* constructRecursive(vector<vector<int>>& grid, int x, int y, int i) {
        Node* ptr;
        bool leaf = isLeaf(grid, x, y, i);
        if (i <= 0 || leaf) {
            ptr = new Node(
                (grid[x][y] != 0),
                leaf,
                nullptr,
                nullptr,
                nullptr,
                nullptr
            );
        } else {
            ptr = new Node(
                (grid[x][y] != 0),
                leaf,
                constructRecursive(grid, x, y, i >> 1),
                constructRecursive(grid, x, y + i, i >> 1),
                constructRecursive(grid, x + i, y, i >> 1),
                constructRecursive(grid, x + i, y + i, i >> 1)
            );
        }
        return ptr;
    }
};
