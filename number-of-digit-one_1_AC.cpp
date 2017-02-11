#include <cstdint>

class Solution {
public:
    Solution() {
        int64_t base = 1;
        int i;
        int MAXN = 11;
        
        c.push_back(0);
        for (i = 0; i < MAXN; ++i) {
            c.push_back(c.back() * R + base);
            base *= R;
        }
    }
    
    int countDigitOne(int n) {
        if (n <= 0) {
            return 0;
        }
        
        int64_t base = 1;
        int bc = 0;
        while (base * R <= n) {
            base *= R;
            ++bc;
        }
        
        int d = n / base;
        int res = d * c[bc] + countDigitOne(n % base);
        res += (d > 1 ? base : n % base + 1);
        return res;
    }
    
    ~Solution() {
        c.clear();
    }
private:
    static const int R = 10;
    
    vector<int64_t> c;
};
