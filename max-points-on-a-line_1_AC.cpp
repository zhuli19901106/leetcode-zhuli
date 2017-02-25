// Write your own comparator and hasher.
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
#include <algorithm>
#include <unordered_map>
#include <utility>
using std::make_pair;
using std::max;
using std::pair;

typedef pair<int, int> PII;

struct PIIHash {
    size_t operator () (const PII &p) const {
        static const int P = 10007;
        return p.first * P + p.second;
    }
};

struct PIICompare {
    bool operator () (const PII &p1, const PII &p2) const {
        return p1.first == p2.first && p1.second == p2.second;
    }
};

class Solution {
public:
    int maxPoints(vector<Point>& points) {
        int res = 0;
        auto &vp = points;
        int np = vp.size();
        if (np < 3) {
            return np;
        }
        
        unordered_map<PII, int, PIIHash, PIICompare> um;
        int i, j;
        PII p, pz(0, 0);
        int zero;
        for (i = 0; i < np; ++i) {
            for (j = 0; j < np; ++j) {
                p.first = vp[i].x - vp[j].x;
                p.second = vp[i].y - vp[j].y;
                normalize(p);
                ++um[p];
            }
            zero = um[pz];
            res = max(res, zero);
            for (auto it = um.begin(); it != um.end(); ++it) {
                if (it->first == pz) {
                    continue;
                }
                res = max(res, it->second + zero);
            }
            um.clear();
        }
        
        return res;
    }
private:
    void normalize(PII &p) {
        if (p.first == 0 && p.second == 0) {
            return;
        }
        if (p.first == 0) {
            p.second = 1;
            return;
        }
        if (p.second == 0) {
            p.first = 1;
            return;
        }
        if (p.first < 0) {
            p.first = -p.first;
            p.second = -p.second;
        }
        
        int g = gcd(p.first, p.second);
        p.first /= g;
        p.second /= g;
    }
    
    int gcd(int x, int y) {
        if (x < 0) {
            x = -x;
        }
        if (y < 0) {
            y = -y;
        }
        
        int t;
        while (x % y != 0) {
            t = x;
            x = y;
            y = t % x;
        }
        
        return y;
    }
};
