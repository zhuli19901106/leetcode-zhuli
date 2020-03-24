#include <vector>
using std::vector;

class Solution {
public:
    Solution() {
        int n = 10000;
        b.resize(n + 1);
        int i;
        for (i = 0; i <= n; ++i) {
            b[i] = isSD(i);
        }
    }
    
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        int i;
        for (i = left; i <= right; ++i) {
            if (b[i]) {
                res.push_back(i);
            }
        }
        return res;
    }
private:
    vector<bool> b;
    
    bool isSD(int n) {
        if (n <= 0) {
            return false;
        }
        
        int n0 = n;
        int d;
        while (n > 0) {
            d = n % 10;
            if (d == 0 || n0 % d != 0) {
                return false;
            }
            n = n / 10;
        }
        return true;
    }
};
