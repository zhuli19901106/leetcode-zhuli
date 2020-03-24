// Whimsical problem calls for weirdo solution.
#include <cstring>
using std::memset;

class Solution {
public:
    string originalDigits(string s) {
        const int N_CHAR = 26;
        const int N_DIGIT = 10;
        int cnt[N_CHAR];
        int dc[N_DIGIT];
        int ls = s.size();
        int i;
        string res = "";
        
        memset(cnt, 0, N_CHAR * sizeof(int));
        memset(dc, 0, N_DIGIT * sizeof(int));
        for (i = 0; i < ls; ++i) {
            ++cnt[s[i] - 'a'];
        }
        
        static const string nums[] = {
            "zero", "two", "eight", "six", "seven", 
            "five", "three", "four", "one", "nine"
        };
        static const int idx[] = {
            0, 1, 2, 2, 0, 
            2, 0, 0, 0, 1
        };
        static const int digit[] = {
            0, 2, 8, 6, 7, 
            5, 3, 4, 1, 9
        };
        
        int j;
        int k;
        int len;
        for (i = 0; i < N_DIGIT; ++i) {
            k = cnt[nums[i][idx[i]] - 'a'];
            dc[digit[i]] = k;
            len = nums[i].size();
            for (j = 0; j < len; ++j) {
                cnt[nums[i][j] - 'a'] -= k;
            }
        }
        for (i = 0; i < N_DIGIT; ++i) {
            for (j = 0; j < dc[i]; ++j) {
                res.push_back('0' + i);
            }
        }
        return res;
    }
};
