// A math problem can be dead hard if you take it the wrong way.
// Give up and try a flanking route when things start to get ugly.
class Solution {
public:
    Solution() {
        dp.push_back(1);
        dp.push_back(10);
    }
    
    int countNumbersWithUniqueDigits(int n) {
        if (n > 10) {
            n = 10;
        }
        while (dp.size() <= n) {
            dp.push_back(calc(dp.size()));
        }
        return dp[n];
    }
    
    ~Solution() {
        dp.clear();
    }
private:
    vector<int> dp;
    
    int permutation(int n, int k) {
        int sum = 1;
        int i;
        for (i = n; i > n - k; --i) {
            sum *= i;
        }
        return sum;
    }
    
    int calc(int n) {
        return dp[n - 1] + permutation(10, n) - permutation(9, n - 1);
    }
};
