#include <cmath>
#include <string>
#include <vector>
using std::abs;
using std::string;
using std::vector;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        static const int DICT_SIZE = 26;
        
        int ls1 = s1.size();
        int ls2 = s2.size();
        if (ls2 < ls1) {
            return false;
        }
        
        vector<int> c1(DICT_SIZE, 0), c2(DICT_SIZE, 0);
        
        int i;
        for (i = 0; i < ls1; ++i) {
            ++c1[s1[i] - 'a'];
            ++c2[s2[i] - 'a'];
        }
        
        int diff = 0;
        for (i = 0; i < DICT_SIZE; ++i) {
            diff += abs(c1[i] - c2[i]);
        }
        if (diff == 0) {
            return true;
        }
        
        int idx;
        for (i = ls1; i < ls2; ++i) {
            idx = s2[i] - 'a';
            ++c2[idx];
            if (c2[idx] > c1[idx]) {
                ++diff;
            } else {
                --diff;
            }
            
            idx = s2[i - ls1] - 'a';
            --c2[idx];
            if (c2[idx] < c1[idx]) {
                ++diff;
            } else {
                --diff;
            }
            
            if (diff == 0) {
                return true;
            }
        }
        
        return false;
    }
};
