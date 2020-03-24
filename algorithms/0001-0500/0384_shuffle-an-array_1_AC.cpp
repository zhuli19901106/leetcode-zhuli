// O(n) time, O(1) space shuffling
#include <algorithm>
#include <cstdlib>
using std::rand;
using std::swap;

class Solution {
public:
    Solution(vector<int> nums) {
        this->v = nums;
        this->n = nums.size();
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return v;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        vector<int> v1 = v;
        int i;
        int j;
        for (i = 0; i < n; ++i) {
            j = rand() % (n - i);
            swap(v1[j], v1[n - 1 - i]);
        }
        return v1;
    }
private:
    vector<int> v;
    int n;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * vector<int> param_1 = obj.reset();
 * vector<int> param_2 = obj.shuffle();
 */
