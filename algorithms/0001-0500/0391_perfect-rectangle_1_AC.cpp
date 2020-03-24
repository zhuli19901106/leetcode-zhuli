// Segment tree, BIT, whatever.
// Avoid any complications whenever you can.
#include <algorithm>
#include <climits>
#include <cstdint>
#include <functional>
#include <unordered_map>
#include <utility>
using std::hash;
using std::make_pair;
using std::max;
using std::min;
using std::pair;
using std::unordered_map;

typedef pair<int, int> PII;

namespace std {
template <>
class hash<PII> {
public:
    size_t operator () (const PII &p) const {
        return p.first * P + p.second;
    }
private:
    static const int P = 10007;
};
};

class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        unordered_map<PII, int> um;
        int x1, y1, x2, y2;
        int min_x, min_y, max_x, max_y;
        
        min_x = min_y = INT_MAX;
        max_x = max_y = INT_MIN;
        
        auto &v = rectangles;
        int n = v.size();
        int i;
        int64_t area = 0;
        for (i = 0; i < n; ++i) {
            x1 = v[i][0];
            y1 = v[i][1];
            x2 = v[i][2];
            y2 = v[i][3];
            
            min_x = min(min_x, x1);
            min_y = min(min_y, y1);
            max_x = max(max_x, x2);
            max_y = max(max_y, y2);
            
            area += 1LL * (x2 - x1) * (y2 - y1);
            
            ++um[make_pair(x1, y1)];
            ++um[make_pair(x1, y2)];
            ++um[make_pair(x2, y1)];
            ++um[make_pair(x2, y2)];
        }
        
        bool res = true;
        if (area != 1LL * (max_x - min_x) * (max_y - min_y)) {
            res = false;
        }
        
        int cc;
        for (auto it =um.begin(); res && it != um.end(); ++it) {
            x1 = it->first.first;
            y1 = it->first.second;
            
            if ((x1 == min_x || x1 == max_x) && (y1 == min_y || y1 == max_y)) {
                cc = 1;
            } else {
                cc = 0;
            }
            if (it->second % 2 != cc) {
                res = false;
            }
        }
        um.clear();
        
        return res;
    }
};
