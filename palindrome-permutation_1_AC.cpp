#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    bool canPermutePalindrome(string s) {
        static const int DICT_SIZE = 256;
        vector<int> c(DICT_SIZE, 0);
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            ++c[s[i]];
        }
        
        int odd_cnt = 0;
        for (i = 0; i < DICT_SIZE; ++i) {
            if (c[i] & 1) {
                ++odd_cnt;
            }
        }
        c.clear();
        
        return odd_cnt <= 1;
    }
};
