#include <algorithm>
#include <string>
#include <vector>
using std::reverse;
using std::string;
using std::vector;

class Solution {
public:
    vector<string> generatePalindromes(string s) {
        static const int DICT_SIZE = 256;
        vector<int> c(DICT_SIZE, 0);
        
        int ls = s.size();
        int i;
        for (i = 0; i < ls; ++i) {
            ++c[s[i]];
        }
        
        char odd_char;
        int odd_cnt = 0;
        for (i = 0; i < DICT_SIZE; ++i) {
            if (c[i] & 1) {
                ++odd_cnt;
                odd_char = i;
            }
        }
        
        vector<string> res;
        if (odd_cnt > 1) {
            return res;
        }
        
        string h1, h2;
        int j;
        for (i = 0; i < DICT_SIZE; ++i) {
            for (j = 1; j < c[i]; j += 2) {
                h1.push_back(i);
            }
        }
        c.clear();
        
        do {
            h2 = h1;
            reverse(h2.begin(), h2.end());
            if (odd_cnt == 1) {
                res.push_back(h1 + odd_char + h2);
            } else {
                res.push_back(h1 + h2);
            }
        } while (nextPermutation(h1));
        
        return res;
    }
private:
    bool nextPermutation(string &s) {
        int ls = s.size();
        int i, j;
        for (i = ls - 2; i >= 0 && s[i] >= s[i + 1]; --i) {}
        if (i < 0) {
            return false;
        }
        
        for (j = i + 1; j + 1 <= ls - 1 && s[i] < s[j + 1]; ++j) {}
        swap(s[i], s[j]);
        reverse(s.begin() + i + 1, s.end());
        return true;
    }
};
