class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.size();
        if (k >= n) {
            return string("0");
        }
        int i, j;
        int cnt;
        vector<bool> del(n, false);
        
        i = 0;
        j = 1;
        cnt = k;
        
        while (j <= n - 1 && cnt > 0) {
            if (i < 0 || num[i] <= num[j]) {
                i = j;
                j = next(del, i + 1);
            } else {
                del[i] = true;
                --cnt;
                i = last(del, i);
            }
        }
        
        for (i = n - 1; cnt > 0 && i >= 0; --i) {
            if (!del[i]) {
                del[i] = true;
                --cnt;
            }
        }
        
        string res = "";
        for (i = 0; i < n; ++i) {
            if (!del[i]) {
                res.push_back(num[i]);
            }
        }
        del.clear();
        
        n = res.size();
        i = 0;
        while (i < n - 1 && res[i] == '0') {
            ++i;
        }
        
        return res.substr(i, n - i);
    }
private:
    int last(vector<bool> &del, int i) {
        while (i >= 0 && del[i]) {
            --i;
        }
        return i;
    }
    
    int next(vector<bool> &del, int i) {
        int n = del.size();
        while (i <= n - 1 && del[i]) {
            ++i;
        }
        return i;
    }
};
