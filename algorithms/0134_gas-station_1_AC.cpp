class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        if (n == 0) {
            return true;
        }
        int sum = 0;
        int i, j;
        
        j = 0;
        for (i = 0; i < 2 * n - 1; ++i) {
            if (i - j == n) {
                break;
            }
            sum += gas[i % n] - cost[i % n];
            if (sum < 0) {
                j = i + 1;
                sum = 0;
            }
        }
        return i - j == n ? j : -1;
    }
};
