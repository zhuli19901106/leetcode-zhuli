#include <algorithm>
using std::reverse;

class Solution {
public:
    string toHex(int num) {
        if (num == 0) {
            return "0";
        }
        
        // Pointer manipulation.
        unsigned int n = *(unsigned int *)(&num);
        string res = "";
        while (n != 0) {
            res.push_back(hex[n & 0xf]);
            n >>= 4;
        }
        reverse(res.begin(), res.end());
        return res;
    }
private:
    const string hex = "0123456789abcdef";
};
