// https://discuss.leetcode.com/topic/25913/my-easy-understood-solution-with-o-n-time-and-o-1-space-without-modifying-the-array-with-clear-explanation
// Linked list with a cycle.
// This solution is most brilliant.
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int i1, i2;
        
        i1 = nums[0];
        i2 = nums[nums[0]];
        while (i1 != i2) {
            // Cat and mouse
            i1 = nums[i1];
            i2 = nums[nums[i2]];
        }
        i2 = 0;
        while (i1 != i2) {
            i1 = nums[i1];
            i2 = nums[i2];
        }
        return i1;
    }
};
