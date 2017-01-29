// https://discuss.leetcode.com/topic/76489/c-different-solution-no-linkedlist-loop-needed-o-n-time-complexity-o-1-space
// This solution is both concise and clever, although it modifies the input array.
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int i1, i2;
        
        i1 = i2 = 0;
        while (true) {
            i2 = nums[i1];
            if (i2 == -1) {
                return i1;
            }
            nums[i1] = -1;
            i1 = i2;
        }
    }
};
