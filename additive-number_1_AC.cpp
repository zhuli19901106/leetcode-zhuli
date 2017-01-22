#include <algorithm>
using std::reverse;
using std::swap;

class Solution {
public:
    bool isAdditiveNumber(string s) {
        int ls = s.size();
        int i, j;
        for (i = 1; i < ls; ++i) {
            if (s[0] == '0' && i - 0 > 1) {
                // Leading zero
                continue;
            }
            for (j = i + 1; j < ls; ++j) {
                if (s[i] == '0' && j - i > 1) {
                    // Leading zero
                    continue;
                }
                if (checkAdditive(i, j, s)) {
                    return true;
                }
            }
        }
        return false;
    }
private:
    // Big integer addition
    string add(string s1, string s2) {
        if (s1.size() > s2.size()) {
            swap(s1, s2);
        }
        reverse(s1.begin(), s1.end());
        reverse(s2.begin(), s2.end());
        while (s1.size() < s2.size()) {
            s1.push_back('0');
        }
        
        int n = s1.size();
        string s3;
        s3.resize(n + 1, 0);
        int i;
        for (i = 0; i < n; ++i) {
            s3[i] = (s1[i] - '0') + (s2[i] - '0');
        }
        for (i = 0; i < n; ++i) {
            s3[i + 1] += s3[i] / 10;
            s3[i] %= 10;
            s3[i] += '0';
        }
        if (s3[n] > 0) {
            s3[n] += '0';
        } else {
            s3.pop_back();
        }
        reverse(s3.begin(), s3.end());
        return s3;
    }
    
    bool checkAdditive(int i1, int i2, string &s) {
        int ls = s.size();
        string s1 = s.substr(0, i1);
        string s2 = s.substr(i1, i2 - i1);
        string s3 = add(s1, s2);
        int i3 = i2 + s3.size();
        while (i3 < ls && s3 == s.substr(i2, s3.size())) {
            i1 = i2;
            i2 = i3;
            s1 = s2;
            s2 = s3;
            s3 = add(s1, s2);
            i3 = i2 + s3.size();
        }
        return i3 == ls && s3 == s.substr(i2, s3.size());
    }
};
