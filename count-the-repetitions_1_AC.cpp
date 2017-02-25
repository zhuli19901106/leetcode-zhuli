// Basically brute-force, the running time is close to the limit.
#include <string>
using std::string;

class Solution {
public:
    int getMaxRepetitions(string s1, int n1, string s2, int n2) {
        int ls1 = s1.size();
        int ls2 = s2.size();
        if (ls1 == 0 || ls2 == 0) {
            return 0;
        }
        if (n1 == 0 || n2 == 0) {
            return 0;
        }
        
        int i, j;
        int c1, c2;
        
        i = j = 0;
        c1 = c2 = 0;
        while (c1 < n1) {
            if (s1[i] == s2[j]) {
                ++j;
            }
            ++i;
            
            if (i == ls1) {
                i = 0;
                ++c1;
            }
            if (j == ls2) {
                j = 0;
                ++c2;
            }
            if (i == 0 && j == 0) {
                // An exact match is found.
                // Like least common multiple, you know.
                break;
            }
        }
        
        // Actually both are the same.
        if (i == 0 && j == 0) {
            return (1LL * n1 * c2 / c1) / n2;
        } else {
            return c2 / n2;
        }
    }
};
