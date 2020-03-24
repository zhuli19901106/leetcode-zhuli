// O(n) time and O(1) space.
#include <cstdlib>
using std::rand;

class Solution {
public:
    Solution(vector<int> nums) {
        a = nums;
        n = nums.size();
    }
    
    int pick(int target) {
        // Reservoir sampling
        int i;
        int val = -1;
        int cnt = 0;
        for (i = 0; i < n; ++i) {
            if (a[i] != target) {
                continue;
            }
            ++cnt;
            if (rand() % cnt == 0) {
                val = i;
            }
        }
        return val;
    }
    
    ~Solution() {
        a.clear();
        n = 0;
    }
private:
    vector<int> a;
    int n;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */