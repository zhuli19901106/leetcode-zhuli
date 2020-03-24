#include <algorithm>
#include <vector>
using std::reverse;
using std::upper_bound;
using std::vector;

class Solution {
public:
    vector<int> sortTransformedArray(vector<int>& nums, int a, int b, int c) {
        auto &v = nums;
        int n = v.size();
        vector<int> res;
        if (n == 0) {
            return res;
        }
        
        if (a == 0) {
            oneToOne(v, res, a, b, c);
            if (b < 0) {
                reverse(res.begin(), res.end());
            }
            return res;
        }
        
        double mid = -1.0 * b / (2 * a);
        if ((a < 0 && mid >= v[n - 1]) || (a > 0 && mid <= v[0])) {
            oneToOne(v, res, a, b, c);
            return res;
        } else if ((a < 0 && mid <= v[0]) || (a > 0 && mid >= v[n - 1])) {
            oneToOne(v, res, a, b, c);
            reverse(res.begin(), res.end());
            return res;
        }
        
        int i, j;
        int y1, y2;
        
        j = upper_bound(v.begin(), v.end(), mid) - v.begin();
        i = j - 1;
        while (i >= 0 || j <= n - 1) {
            if (i >= 0) {
                y1 = (a * v[i] + b) * v[i] + c;
            }
            if (j <= n - 1) {
                y2 = (a * v[j] + b) * v[j] + c;
            }
            if (i < 0) {
                res.push_back(y2);
                ++j;
            } else if (j > n - 1) {
                res.push_back(y1);
                --i;
            } else if ((a > 0 && y1 < y2) || (a < 0 && y1 > y2)) {
                res.push_back(y1);
                --i;
            } else {
                res.push_back(y2);
                ++j;
            }
        }
        if (a < 0) {
            reverse(res.begin(), res.end());
        }
        
        return res;
    }
private:
    void oneToOne(vector<int> &v, vector<int> &res, int a, int b, int c) {
        int n = v.size();
        int i;
        for (i = 0; i < n; ++i) {
            res.push_back((a * v[i] + b) * v[i] + c);
        }
    }
};
