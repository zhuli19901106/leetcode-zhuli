#include <algorithm>
#include <map>
#include <utility>
#include <vector>
using std::map;
using std::make_pair;
using std::pair;
using std::sort;
using std::vector;

typedef struct Term {
    int x, y;
    bool start;
    
    bool operator < (const Term &t) const {
        if (x != t.x) {
            return x < t.x;
        }
        if (start && t.start) {
            return y > t.y;
        } else if (!start && !t.start) {
            return y < t.y;
        } else {
            return start;
        }
    }
} Term;

class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        Term t;
        auto &bd = buildings;
        int n = bd.size();
        int i;
        
        vector<Term> v;
        for (i = 0; i < n; ++i) {
            // Start of a building
            t.x = bd[i][0];
            t.y = bd[i][2];
            t.start = true;
            v.push_back(t);
            
            // End of a building
            t.x = bd[i][1];
            t.y = bd[i][2];
            t.start = false;
            v.push_back(t);
        }
        sort(v.begin(), v.end());
        n = v.size();
        
        map<int, int> mm;
        vector<pair<int, int>> res;
        int max_val;
        
        ++mm[0];
        max_val = mm.rbegin()->first;
        for (i = 0; i < n; ++i) {
            if (v[i].start) {
                if (v[i].y > max_val) {
                    max_val = v[i].y;
                    res.push_back(make_pair(v[i].x, max_val));
                }
                ++mm[v[i].y];
            } else {
                if (v[i].y == max_val && mm[max_val] == 1) {
                    mm.erase(v[i].y);
                    max_val = mm.rbegin()->first;
                    res.push_back(make_pair(v[i].x, max_val));
                } else {
                    if (mm[v[i].y] == 1) {
                        mm.erase(v[i].y);
                    } else {
                        --mm[v[i].y];
                    }
                }
            }
        }
        v.clear();
        mm.clear();
        
        return res;
    }
};
