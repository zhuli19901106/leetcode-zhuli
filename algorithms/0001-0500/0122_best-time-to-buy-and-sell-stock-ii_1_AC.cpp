class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int i;
        int res = 0;
        for (i = 1; i < n; ++i) {
            if (prices[i] > prices[i - 1]) {
                res += prices[i] - prices[i - 1];
            }
        }
        return res;
    }
};
