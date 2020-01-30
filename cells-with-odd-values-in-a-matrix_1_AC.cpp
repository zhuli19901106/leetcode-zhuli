// https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
#include <vector>
using std::vector;

class Solution {
public:
    int oddCells(int n, int m, vector<vector<int>>& indices) {
        vector<int> vr(n, 0), vc(m, 0);
        for (auto &p: indices) {
            ++vr[p[0]];
            ++vc[p[1]];
        }
        int oddr = 0;
        int oddc = 0;
        for (auto &x: vr) {
            if (x % 2 == 1) {
                ++oddr;
            }
        }
        for (auto &x: vc) {
            if (x % 2 == 1) {
                ++oddc;
            }
        }
        int res = oddr * (m - oddc) + oddc * (n - oddr);
        vr.clear();
        vc.clear();

        return res;
    }
};
