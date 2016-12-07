class Solution {
public:
    int countSegments(string s) {
        int res = 0;
        int i;
        int n = s.size();
        
        i = 0;
        while (true) {
            while (i < n && s[i] == ' ') {
                ++i;
            }
            if (i >= n) {
                break;
            }
            while (i < n && s[i] != ' ') {
                ++i;
            }
            ++res;
            if (i >= n) {
                break;
            }
        }
        return res;
    }
};
