#include <vector>
using std::vector;

class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) {
        v = vec2d;
        i = j = 0;
    }

    int next() {
        ready();
        return v[i][j++];
    }

    bool hasNext() {
        ready();
        return i < v.size();
    }
    
    ~Vector2D() {
        v.clear();
    }
private:
    int i, j;
    vector<vector<int>> v;
    
    void ready() {
        while (i < v.size() && j == v[i].size()) {
            ++i;
            j = 0;
        }
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */
