// The code is a bit messy.
#include <algorithm>
#include <cmath>
#include <vector>
using std::sort;
using std::sqrt;
using std::vector;

class Solution {
public:
    vector<vector<int>> getFactors(int n) {
        vector<vector<int>> res;
        if (n < 4) {
            return res;
        }
        combination(n, 2, res);
        
        return res;
    }
private:
    void combination(int n, int d, vector<vector<int>> &res) {
        int rt = sqrt(n);
        vector<int> dv;
        int i;
        for (i = 1; i <= rt; ++i) {
            if (n % i == 0 && i >= d) {
                dv.push_back(i);
            }
            if (i != n / i && n / i >= d) {
                dv.push_back(n / i);
            }
        }
		sort(dv.begin(), dv.end());
        
        vector<vector<int>> res1;
        int nr;
        for (auto &d1: dv) {
            if (n / d1 < d1) {
                break;
            }
            combination(n / d1, d1, res1);
            res1.push_back(vector<int>());
            res1.back().push_back(n / d1);
            
            nr = res1.size();
            for (auto &rv: res1) {
                res.push_back(vector<int>());
                res.back().push_back(d1);
                for (auto &val: rv) {
                    res.back().push_back(val);
                }
            }
            res1.clear();
        }
    }
};
