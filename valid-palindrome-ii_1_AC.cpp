class Solution {
public:
    bool validPalindrome(string s) {
        int ls = s.size();
        int i = 0;
        int j = ls - 1;
        
        while (i < j) {
            if (s[i] == s[j]) {
                ++i;
                --j;
                continue;
            }
            return isPal(s, i, j - 1) || isPal(s, i + 1, j);
        }
        return true;
    }
private:
    bool isPal(const string &s, int i, int j) {
        while (i < j && s[i] == s[j]) {
            ++i;
            --j;
        }
        return i >= j;
    }
};
