// I got stuck on this problem for an hour.
// This solution is from https://discuss.leetcode.com/topic/31015/very-easy-to-understand-one-pass-o-n-solution-with-no-extra-space
// If DP doesn't seem to make sense, turn to a more generalized model.
// Finite state machine, you guessed it right?
// Presentation might be in different form, but thoughts are one.
#include <algorithm>
using std::max;

typedef struct State {
    int has0_buy;
    int has0_stay;
    int has1_stay;
    int has1_sell;
} State;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n < 2) {
            return 0;
        }
        int i;
        State s0, s1;
        
        s0.has0_buy = -prices[0];
        s0.has0_stay = 0;
        s0.has1_stay = -prices[0];
        s0.has1_sell = 0;
        for (i = 1; i < n; ++i) {
            s1.has0_buy = s0.has0_stay - prices[i];
            // 你一无所有，脚下的地在抖，身边的水在流。你的手在颤抖，心中的泪在流。
            s1.has0_stay = max(s0.has0_stay, s0.has1_sell);
            s1.has1_stay = max(s0.has1_stay, s0.has0_buy);
            // s1.has1_stay, think about why?
            s1.has1_sell = s1.has1_stay + prices[i];
            s0 = s1;
        }
        return max(s0.has0_stay, s0.has1_sell);
    }
};
