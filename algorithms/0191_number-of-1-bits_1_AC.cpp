class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while (n != 0) {
            n &= n - 1;
            ++cnt;
        }
        return cnt;
    }
};
