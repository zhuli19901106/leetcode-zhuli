// Damn, convex hull.
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
#include <vector>
using std::sort;
using std::vector;

int crossProduct(const Point &p1, const Point &p2, const Point &p3)
{
    return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y);
}

Point mp;
bool comparator(const Point &p1, const Point &p2)
{
    // Left turn
    int d = crossProduct(mp, p1, p2);
    if (d != 0) {
        return d > 0;
    }
    d = abs(p1.x - mp.x) + abs(p1.y - mp.y) - abs(p2.x - mp.x) - abs(p2.y - mp.y);
    if (d != 0) {
        return d < 0;
    }
    return false;
}

class Solution {
public:
    vector<Point> outerTrees(vector<Point> &points) {
        auto &vp = points;
        int n = vp.size();
        if (n < 3) {
            return vp;
        }
        
        int mi = 0;
        int i;
        for (i = 1; i < n; ++i) {
            if (vp[i].x < vp[mi].x || (vp[i].x == vp[mi].x && vp[i].y < vp[mi].y)) {
                mi = i;
            }
        }
        swap(vp[0], vp[mi]);
        mp = vp[0];
        sort(vp.begin() + 1, vp.end(), comparator);
        
        vector<Point> res;
        res.push_back(mp);
        
        int pr;
        for (i = 1; i <= n; ++i) {
            while (res.size() >= 2 && 
                (pr = crossProduct(res[res.size() - 2], res[res.size() - 1], vp[i % n])) < 0) {
                res.pop_back();
            }
            res.push_back(vp[i % n]);
        }
        res.pop_back();
        if (res.size() == n) {
            return res;
        }
        
        // Check for colinear points that have been left out.
        i = n - 2;
        while (i >= 1 && crossProduct(mp, vp[i], vp[n - 1]) == 0) {
            res.push_back(vp[i]);
            --i;
        }
        
        return res;
    }
};
