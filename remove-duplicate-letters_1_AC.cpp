// https://discuss.leetcode.com/topic/74326/c-solution-using-counting-sort-o-n
// I feel it's greedy, but I can't write down a clean solution.
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        static const int DICT_SIZE = 26;
        int ls = s.size();
        if (ls < 2) {
            return s;
        }
        
        string res = "";
        vector<int> c1(DICT_SIZE, 0), c2(DICT_SIZE, 0);
        int i;
        for (i = 0; i < ls; ++i) {
            ++c1[s[i] - 'a'];
        }
        
        int j;
        for (i = 0; i < ls; ++i) {
            j = s[i] - 'a';
            if (c2[j] > 0) {
                --c1[j];
                continue;
            }
            while (res.size() > 0 && res.back() >= s[i] && 
                c1[res.back() - 'a'] > 0) {
                --c2[res.back() - 'a'];
                res.pop_back();
            }
            res.push_back(s[i]);
            --c1[j];
            ++c2[j];
        }
        c1.clear();
        c2.clear();
        
        return res;
    }
};
