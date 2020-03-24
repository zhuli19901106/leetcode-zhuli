#include <algorithm>
#include <string>
using std::reverse;
using std::string;

class Solution {
public:
    string multiply(string num1, string num2) {
        static const int R = 10;
        
        int n1 = num1.size();
        int n2 = num2.size();
        int i;
        int j;
        string num3 = "";
        int sum;
        int carry;
        int low, high;
        
        carry = 0;
        for (i = 0; i < n1 + n2 - 1; ++i) {
            low = i > n2 - 1 ? i - (n2 - 1) : 0;
            high = i < n1 - 1 ? i : n1 - 1;
            sum = carry;
            for (j = low; j <= high; ++j) {
                sum += (num1[n1 - 1 - j] - '0') * (num2[n2 - 1 - (i - j)] - '0');
            }
            carry = sum / R;
            sum %= R;
            num3.push_back(sum + '0');
        }
        num3.push_back(carry + '0');
        while (num3.size() > 1 && num3.back() == '0') {
            num3.pop_back();
        }
        reverse(num3.begin(), num3.end());
        return num3;
    }
};
