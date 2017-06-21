// Ugly...
#include <algorithm>
#include <climits>
#include <cstdint>
#include <string>
using std::min;
using std::sort;
using std::string;

class Solution {
public:
    int smallestFactorization(int a) {
        if (a < 0) {
            return 0;
        }
        if (a <= 9) {
            return a;
        }
        
        const int NP = 4;
        const int ND = 10;
        int p[NP] = {2, 3, 5, 7};
        int c[NP] = {0, 0, 0, 0};
        int m[ND][NP] = {
            {0, 0, 0, 0}, 
            {0, 0, 0, 0}, 
            {1, 0, 0, 0}, 
            {0, 1, 0, 0}, 
            {2, 0, 0, 0}, 
            {0, 0, 1, 0}, 
            {1, 1, 0, 0}, 
            {0, 0, 0, 1}, 
            {3, 0, 0, 0}, 
            {0, 2, 0, 0} 
        };
        
        int i;
        for (i = 0; i < NP; ++i) {
            while (a % p[i] == 0) {
                a /= p[i];
                ++c[i];
            }
        }
        if (a > 1) {
            return 0;
        }
        
        string s = "";
        int n;
        int j;
        for (i = 9; i >= 2; --i) {
            n = INT_MAX;
            for (j = 0; j < NP; ++j) {
                if (m[i][j] > 0) {
                    n = min(n, c[j] / m[i][j]);
                }
            }
            if (n == 0) {
                continue;
            }
            for (j = 0; j < n; ++j) {
                s.push_back('0' + i);
            }
            for (j = 0; j < NP; ++j) {
                if (m[i][j] > 0) {
                    c[j] -= n * m[i][j];
                }
            }
        }
        sort(s.begin(), s.end());
        
        int64_t res;
        sscanf(s.data(), "%lld", &res);
        return res <= INT_MAX ? res : 0;
    }
};
