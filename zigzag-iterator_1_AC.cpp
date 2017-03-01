#include <vector>
using std::vector;

class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        v.push_back(v1);
        v.push_back(v2);
        c.resize(NUM_ARRAY, 0);
        n.resize(NUM_ARRAY);
        int i;
        cs = ns = 0;
        for (i = 0; i < NUM_ARRAY; ++i) {
            n[i] = v[i].size();
            ns += n[i];
        }
        idx = 0;
    }

    int next() {
        while (c[idx] == n[idx]) {
            idx = (idx + 1) % NUM_ARRAY;
        }
        
        int val = v[idx][c[idx]++];
        idx = (idx + 1) % NUM_ARRAY;
        ++cs;
        return val;
    }

    bool hasNext() {
        return cs < ns;
    };
    
    ~ZigzagIterator() {
        c.clear();
        n.clear();
        v.clear();
    }
private:
    static const int NUM_ARRAY = 2;
    
    int idx;
    vector<int> c, n;
    int cs, ns;
    vector<vector<int>> v;
};

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i(v1, v2);
 * while (i.hasNext()) cout << i.next();
 */
