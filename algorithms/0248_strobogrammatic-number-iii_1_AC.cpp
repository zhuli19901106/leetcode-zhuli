// I hate all kinds of counting problems.
// Especially this one.
#include <string>
using std::string;

static const int d[10] = {0, 1, -1, -1, -1, -1, 9, -1, 8, 6};
static const int c1[11] = {0, 1, 2, 2, 2, 2, 2, 3, 3, 4, 5};
static const int c2[11] = {0, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3};

class Solution {
public:
    int strobogrammaticInRange(string low, string high) {
        if (low.size() > high.size() || (low.size() == high.size() && low > 
            high)) {
            return 0;
        }
        if (low[0] == '-') {
            low = "0";
        }
        
        if (low == "0") {
            return count(high);
        } else {
            low = minusOne(low);
            return count(high) - count(low);
        }
    }
private:
    string minusOne(string s) {
        int ls = s.size();
        int i = ls - 1;
        while (i >= 0 && s[i] == '0') {
            s[i--] = '9';
        }
        --s[i];
        if (ls > 1 && s[0] == '0') {
            return s.substr(1, ls - 1);
        } else {
            return s;
        }
    }
    
    int count(string s) {
        int ls = s.size();
        if (ls == 1) {
            return c2[s[0] - '0' + 1];
		}

        int res = 0;
        int cnt;
        int i;
        for (i = 1; i < ls; ++i) {
            cnt = countAll(i);
            if (i > 1) {
                cnt = cnt / c1[10] * (c1[10] - 1);
            }
            res += cnt;
        }
        
        int j, k;
        int di, dj;
        
        i = 0;
        j = ls - 1;
        while (i <= j) {
            di = s[i] - '0';
            cnt = (i < j ? c1[di] : c2[di]);
            if (ls > 1 && i == 0) {
                --cnt;
            }
            res += cnt * countAll(j - i - 1);
            if (d[di] == -1) {
                break;
            }
            
            dj = s[j] - '0';
            if (dj < d[di]) {
                k = j - 1;
                while (k > i && s[k] == '0') {
                    --k;
                }
                if (k == i) {
                    break;
                }
                --s[k++];
                while (k < j) {
                    s[k++] = '9';
                }
                s[k] = '0' + d[di];
            }
            ++i;
            --j;
        }
		if (i > j) {
			++res;
		}
        return res;
    }
    
    int countAll(int n) {
        if (n <= 0) {
            return 1;
        }
        int res = 1;
        int i;
        for (i = 1; i < n; i += 2) {
            res *= c1[10];
        }
        if (n & 1) {
            res *= c2[10];
        }
        return res;
    }
};
