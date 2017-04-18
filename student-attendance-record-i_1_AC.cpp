#include <string>
using std::string;

class Solution {
public:
    bool checkRecord(string s) {
        int ls = s.size();
        int i;
        int na;
        int cl;
        
        na = 0;
        cl = 0;
        for (i = 0; i < ls; ++i) {
            if (s[i] == 'A') {
                ++na;
            }
            if (s[i] == 'L') {
                ++cl;
            } else {
                cl = 0;
            }
            
            if (na > 1) {
                return false;
            }
            
            if (cl > 2) {
                return false;
            }
        }
        
        return true;
    }
};
