class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int n = A.size();
        int i = 0;
        int j;
        int res = 0;
        while (i < n) {
            j = i + 2;
            while (j < n && A[j] - A[j - 1] == A[i + 1] - A[i]) {
                ++j;
            }
            res += (j - i - 1) * (j - i - 2) / 2;
            i = j - 1;
        }
        return res;
    }
};
