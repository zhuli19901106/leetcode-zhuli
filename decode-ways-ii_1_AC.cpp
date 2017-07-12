// Too ugly
#include <cstdint>
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    int numDecodings(string s) {
        int ls = s.size();
        if (ls == 0) {
            return 0;
        }
        
        vector<int64_t> v1(11, 0), v2(11, 0), v3(11, 0);
        v1[10] = 1;
        
        int i;
        char c1_start, c1_end, c1;
        if (s[0] == '*') {
            c1_start = '1';
            c1_end = '9';
        } else {
            c1_start = c1_end = s[0];
        }
        for (c1 = c1_start; c1 > '0' && c1 <= c1_end; ++c1) {
            v2[c1 - '0'] = 1 % MOD;
            v2[10] = (v2[10] + 1) % MOD;
        }
        if (ls == 1) {
            return v2[10];
        }
        
        int j;
        char c2_start, c2_end, c2;
        for (i = 1; i < ls; ++i) {
            c1 = s[i];
            if (c1 == '*') {
                c1_start = '1';
                c1_end = '9';
            } else {
                c1_start = c1_end = c1;
            }
            
            c2 = (i > 0 ? s[i - 1] : '0');
            if (c2 == '*') {
                c2_start = '1';
                c2_end = '9';
            } else {
                c2_start = c2_end = c2;
            }
            
            for (j = 0; j <= 10; ++j) {
                v3[j] = 0;
            }
            for (c1 = c1_start; c1 <= c1_end; ++c1) {
                for (c2 = c2_start; c2 <= c2_end; ++c2) {
                    calc(v1, v2, v3, c1 - '0', c2 - '0');
                }
            }
            v1 = v2;
            v2 = v3;
        }
        
        int64_t res = v3[10];
        return res;
    }
private:
    static const int64_t MOD = 1000000007;
    static const int64_t LOW = 1;
    static const int64_t HIGH = 26;
    
    void calc(vector<int64_t> &v1, vector<int64_t> &v2, vector<int64_t> &v3, int d1, int d2) {
        int d = d1;
        if (d >= LOW && d <= HIGH) {
            v3[d1] = (v3[d1] + v2[d2]) % MOD;
            v3[10] = (v3[10] + v2[d2]) % MOD;
        }
        
        if (d2 != 0) {
            d = d2 * 10 + d1;
            if (d >= LOW && d <= HIGH) {
                v3[d1] = (v3[d1] + v1[10]) % MOD;
                v3[10] = (v3[10] + v1[10]) % MOD;
            }
        }
    }
};
