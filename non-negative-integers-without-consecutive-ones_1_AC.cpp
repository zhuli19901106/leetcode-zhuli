// That was an ugly one.
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    int findIntegers(int num) {
        if (num <= 1) {
            return num + 1;
        }
        
        vector<int> v;
        v.push_back(1);
        v.push_back(1);
        v.push_back(1);
        
        int i;
        for (i = 3; i <= 31; ++i) {
            v.push_back(v[i - 1] + v[i - 2]);
        }
        
        string s = "";
        while (num > 0) {
            s.push_back('0' + (num & 1));
            num >>= 1;
        }
        
        int ls = s.size();
        int j;
        i = ls - 1;
        while (i > 0) {
            if (s[i] == '1' && s[i - 1] == '1') {
                s[i - 1] = '0';
                j = i - 2;
                while (j >= 0) {
                    if (s[j] == '0') {
                        s[j] = '1';
                    }
                    --j;
                }
            }
            --i;
        }
        
        int res = 1;
        i = ls;
        while (i > 0) {
            if (s[i - 1] == '1') {
                res += v[i + 1];
            }
            --i;
        }
        
        return res;
    }
};
