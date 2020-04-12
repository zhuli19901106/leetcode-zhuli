#include <algorithm>
using std::swap;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int n = s.size();
        int i = 0;
        int j = n - 1;
        while (i < j) {
            swap(s[i++], s[j--]);
        }
    }
};
