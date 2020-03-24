class Solution {
public:
    string licenseKeyFormatting(string S, int K) {
        string res = "";
        int cnt = 0;
        int ls = S.size();
        int i;
        for (i = 0; i < ls; ++i) {
            if (S[i] == '-') {
                continue;
            }
            ++cnt;
            if (S[i] >= 'a' && S[i] <= 'z') {
                S[i] = S[i] - 'a' + 'A';
            }
        }
        int len = cnt % K;
        if (len == 0) {
            len = K;
        }
        
        int j = 0;
        for (i = 0; i < ls; ++i) {
            if (S[i] == '-') {
                continue;
            }
            res.push_back(S[i]);
            ++j;
            if (j == len) {
                res.push_back('-');
                j = 0;
                len = K;
            }
        }
        res.pop_back();
        return res;
    }
};
