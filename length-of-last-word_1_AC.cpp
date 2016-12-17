class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        int i = n - 1;
        while (i >= 0 && s[i] == ' ') {
            --i;
        }
        int j = i;
        while (j >= 0 && s[j] != ' ') {
            --j;
        }
        return i - j;
    }
};
