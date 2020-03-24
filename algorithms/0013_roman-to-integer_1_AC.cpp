#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    Solution() {
        dict['I'] = 1;
        dict['V'] = 5;
        dict['X'] = 10;
        dict['L'] = 50;
        dict['C'] = 100;
        dict['D'] = 500;
        dict['M'] = 1000;
    }
    
    int romanToInt(string s) {
        int n = s.size();
        int res = 0;
        int i = 0; 
        while (i < n) {
            if (i < n - 1 && dict[s[i]] < dict[s[i + 1]]) {
                res -= dict[s[i]];
                res += dict[s[i + 1]];
                i += 2;
            } else {
                res += dict[s[i]];
                i += 1;
            }
        }
        return res;
    }
    
    ~Solution() {
        dict.clear();
    }
private:
    unordered_map<char, int> dict;
};
