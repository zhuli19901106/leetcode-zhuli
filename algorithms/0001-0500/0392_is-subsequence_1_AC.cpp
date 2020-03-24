class Solution {
public:
    bool isSubsequence(string s, string t) {
        int ls = s.size();
        int lt = t.size();
        int i = 0;
        int j = 0;
        while (i < ls && j < lt) {
            if (s[i] == t[j]) {
                ++i;
            }
            ++j;
        }
        return i == ls;
    }
};
