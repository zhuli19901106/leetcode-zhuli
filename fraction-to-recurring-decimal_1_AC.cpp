// F the edge cases
#include <cmath>
#include <cstdint>
#include <unordered_map>
#include <vector>
using std::abs;
using std::unordered_map;
using std::vector;

class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        static const int R = 10;
        
        int64_t n1 = numerator;
        int64_t n2 = denominator;
        int flag = 1;
        
        if (n1 < 0) {
            flag = -flag;
            n1 = -n1;
        }
        if (n2 < 0) {
            flag = -flag;
            n2 = -n2;
        }
        
        if (n1 == 0) {
            return "0";
        }
        
        vector<int64_t> v;
        unordered_map<int64_t, int64_t> um;
        
        string res = (flag == -1 ? "-" : "") + to_string(n1 / n2);
        n1 %= n2;
        
        if (n1 == 0) {
            return res;
        }
        
        int i, j;
        int64_t d;
        
        i = 0;
        while (n1 != 0 && um.find(n1) == um.end()) {
            um[n1] = i++;
            n1 *= R;
            d = n1 / n2;
            n1 %= n2;
            v.push_back(d);
        }
        int n = v.size();
        j = (n1 != 0) ? um[n1] : n;
        
        res.push_back('.');
        i = 0;
        while (i < j) {
            res.push_back(v[i++] + '0');
        }
        if (n1 == 0) {
            um.clear();
            v.clear();
            return res;
        }
        res.push_back('(');
        while (i < n) {
            res.push_back(v[i++] + '0');
        }
        res.push_back(')');
        
        um.clear();
        v.clear();
        return res;
    }
};
