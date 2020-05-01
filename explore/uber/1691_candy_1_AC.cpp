// It's greedy.
class Solution {
public:
    int candy(vector<int>& ratings) {
        auto &r = ratings;
        int n = r.size();
        vector<int> v(n, 1);
        
        int i;
        for (i = n - 2; i >= 0; --i) {
            if (r[i] > r[i + 1] && v[i] <= v[i + 1]) {
                v[i] = v[i + 1] + 1;
            }
        }
        for (i = 1; i <= n - 1; ++i) {
            if (r[i] > r[i - 1] && v[i] <= v[i - 1]) {
                v[i] = v[i - 1] + 1;
            }
        }
        
        int res = 0;
        for (i = 0; i < n; ++i) {
            res += v[i];
        }
        v.clear();
        
        return res;
    }
};
