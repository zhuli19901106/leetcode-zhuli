class Solution {
public:
    string getPermutation(int n, int k) {
        --k;
        string s;
        string res;
        int i;
        int fac = 1;
        for (i = 1; i <= n; ++i) {
            s.push_back(i + '0');
            fac *= i;
        }
        
        int cnt;
        int idx;
        
        cnt = n;
        while (s.size() > 0) {
            fac /= cnt--;
            idx = k / fac;
            k %= fac;
            res.push_back(s[idx]);
            for (i = idx; i < s.size() - 1; ++i) {
                s[i] = s[i + 1];
            }
            s.pop_back();
        }
        return res;
    }
};
