#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        int ls = s.size();
        int i;
        vector<string> res;
        for (i = 0; i + 1 < ls; ++i) {
            if (s[i] == '+'&& s[i + 1] == '+') {
                s[i] = '-';
                s[i + 1] = '-';
                res.push_back(s);
                s[i] = '+';
                s[i + 1] = '+';
            }
        }
        return res;
    }
};
