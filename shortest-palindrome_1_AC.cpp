// Longest palindromic prefix
// Hashing is almighty.
#include <string>
#include <vector>
using std::string;
using std::vector;

class Solution {
public:
    Solution() {
        pw.push_back(1);
    }
    
    string shortestPalindrome(string s) {
        int ls = s.size();
        int lp = longestPalindromicPrefix(s);
        string s1 = s.substr(lp, ls - lp);
        reverse(s1.begin(), s1.end());
        
        return s1 + s;
    }
    
    ~Solution() {
        pw.clear();
    }
private:
    static const int64_t P = 31;
    vector<int64_t> pw;
    
    int64_t getPow(int i) {
        while (pw.size() <= i) {
            pw.push_back(pw.back() * P);
        }
        return pw[i];
    }
    
    int longestPalindromicPrefix(string s) {
        int ls = s.size();
        if (ls < 2) {
            return ls;
        }
        
        vector<int64_t> h(ls + 2, 0), rh(ls + 2, 0);
        int i;
        
        for (i = 1; i <= ls; ++i) {
            h[i] = h[i - 1] * P + (s[i - 1] - 'a' + 1);
        }
        for (i = ls; i >= 1; --i) {
            rh[i] = rh[i + 1] * P + (s[i - 1] - 'a' + 1);
        }
        
        int j;
        for (i = ls; i >= 1; --i) {
            // Check if s[1, i] is palindromic
            j = i >> 1;
            if (hash(h, 1, j) == rhash(rh, i - j + 1, i)) {
                break;
            }
        }
        int res = i;
        h.clear();
        rh.clear();
        
        return res;
    }
    
    int64_t hash(vector<int64_t> &h, int left, int right) {
        return h[right] - h[left - 1] * getPow(right - left + 1);
    }
    
    int64_t rhash(vector<int64_t> &rh, int left, int right) {
        return rh[left] - rh[right + 1] * getPow(right - left + 1);
    }
};
