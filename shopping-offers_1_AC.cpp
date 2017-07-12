#include <vector>
using std::vector;

class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        int n = price.size();
        int m = 1;
        int i;
        for (i = 0; i < n; ++i) {
            m *= (needs[i] + 1);
        }
        
        vector<int> dp(m, -1);
        dp[0] = 0;
        
        vector<int> normal(n, 0);
        vector<int> v(n);
        for (i = 0; i < n; ++i) {
            normal[i] = 1;
            knapsack(0, v, normal, needs, dp, price[i]);
            normal[i] = 0;
        }
        
        int ns = special.size();
        for (i = 0; i < ns; ++i) {
            knapsack(0, v, special[i], needs, dp, special[i][n]);
        }
        
        int res = dp[m - 1];
        dp.clear();
        v.clear();
        
        return res;
    }
private:
    void knapsack(int cnt, vector<int> &v, const vector<int> &offer, const vector<int> &needs, vector<int> &dp, int pr) {
        if (cnt == needs.size()) {
            int idx = vtoi(v, needs);
            int idx1 = idx - vtoi(offer, needs);
            
            if (dp[idx1] != -1 && (dp[idx] == -1 || dp[idx] > dp[idx1] + pr)) {
                dp[idx] = dp[idx1] + pr;
            }
            return;
        }
        
        int i;
        for (i = offer[cnt]; i <= needs[cnt]; ++i) {
            v[cnt] = i;
            knapsack(cnt + 1, v, offer, needs, dp, pr);
            v[cnt] = 0;
        }
    }
    
    int vtoi(const vector<int> &v, const vector<int> &needs) {
        int n = needs.size();
        int i;
        int idx = 0;
        for (i = 0; i < n; ++i) {
            idx = idx * (needs[i] + 1) + v[i];
        }
        return idx;
    }
};
