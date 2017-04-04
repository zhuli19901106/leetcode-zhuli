// Is this April Fool's present?
#include <algorithm>
#include <string>
using std::max;
using std::string;

class Solution {
public:
    int findLUSlength(string a, string b) {
        int la = a.size();
        int lb = b.size();
        
        if (la != lb) {
            return max(la, lb);
        } else {
            return a == b ? -1 : la;
        }
    }
};
