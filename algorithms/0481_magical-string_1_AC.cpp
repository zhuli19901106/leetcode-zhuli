// Kolakoski sequence
class Solution {
public:
    int magicalString(int n) {
        string s = "122";
        string d = "021";
        int idx = 2;
        char ch;
        while (s.size() < n) {
            ch = d[s.back() - '0'];
            s.push_back(ch);
            if (s[idx] == '2') {
                s.push_back(ch);
            }
            ++idx;
        }
        int res = 0;
        for (idx = 0; idx < n; ++idx) {
            if (s[idx] == '1') {
                ++res;
            }
        }
        return res;
    }
};
