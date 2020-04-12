// Brute-force
#include <vector>
using std::vector;

class Solution {
public:
    Solution() {
        res.push_back("1");
    }
    
    string countAndSay(int n) {
        while (res.size() < n) {
            res.push_back(count(res.back()));
        }
        return res[n - 1];
    }
    
    ~Solution() {
        res.clear();
    }
private:
    vector<string> res;
    
    string count(string s) {
        string s1 = "";
        int n = s.size();
        int i, j;
        
        i = 0;
        while (i < n) {
            j = i + 1;
            while (j < n && s[j] == s[i]) {
                ++j;
            }
            s1 += to_string(j - i) + s[i];
            i = j;
        }
        return s1;
    }
};
