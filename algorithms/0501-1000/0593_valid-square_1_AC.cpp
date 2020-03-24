#include <algorithm>
#include <vector>
using std::sort;
using std::vector;

class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        vector<int> vd;
        
        vd.push_back(dist2(p1, p2));
        vd.push_back(dist2(p1, p3));
        vd.push_back(dist2(p1, p4));
        vd.push_back(dist2(p2, p3));
        vd.push_back(dist2(p2, p4));
        vd.push_back(dist2(p3, p4));
        
        sort(vd.begin(), vd.end());
        int i;
        for (i = 1; i < 4; ++i) {
            if (vd[i] != vd[0]) {
                return false;
            }
        }
        return vd[0] > 0 && vd[4] == 2 * vd[0] && vd[5] == vd[4];
    }
private:
    int dist2(vector<int> &p1, vector<int> &p2) {
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + 
            (p1[1] - p2[1]) * (p1[1] - p2[1]);
    }
};
