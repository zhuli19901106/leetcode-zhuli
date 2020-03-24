#include <algorithm>
#include <string>
using std::reverse;
using std::string;

class Solution {
public:
    string convertToBase7(int num) {
        static const int R = 7;
        
        if (num < 0) {
            return "-" +convertToBase7(-num);
        }
        if (num == 0) {
            return "0";
        }
        string s = "";
        while (num > 0) {
            s.push_back(num % R + '0');
            num /= R;
        }
        reverse(s.begin(), s.end());
        
        return s;
    }
};
