#include <algorithm>
#include <climits>
#include <cstdio>
#include <cstdint>
#include <string>
using std::next_permutation;
using std::string;
using std::to_string;

class Solution {
public:
    int nextGreaterElement(int n) {
        string s = to_string(n);
        if (!next_permutation(s.begin(), s.end())) {
            return -1;
        }
        int64_t n1;
        sscanf(s.data(), "%lld", &n1);
        if (n1 > INT_MAX) {
            return -1;
        }
        
        return n1;
    }
};
