// It took me quite a while to understand the problem.
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    string findContestMatch(int n) {
        vector<int> v(n, 0);
        
        int sum;
        int d;
        int i, j;
        
        v[0] = 1;
        sum = 2;
        d = n;
        i = (d >> 1);
        while (d > 1) {
            j = i;
            while (j < n) {
                v[j] = sum + 1 - v[j - (d >> 1)];
                j += d;
            }
            
            sum <<= 1;
            d >>= 1;
            i >>= 1;
        }
        
        string res = format(v, 0, n);
        v.clear();
        
        return res;
    }
private:
    string format(vector<int> &v, int i, int len) {
        if (len == 2) {
            return '(' + to_string(v[i]) + ',' + to_string(v[i + 1]) + ')';
        }
        return '(' + format(v, i, len >> 1) + ',' + 
            format(v, i + (len >> 1), len >> 1) + ')';
    }
};
