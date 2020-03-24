// Next combination
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> v;
        int i;
        for (i = 1; i <= k; ++i) {
            v.push_back(i);
        }
        do {
            res.push_back(v);
        } while (nextCombination(v, n, k));
        return res;
    }
private:
    bool nextCombination(vector<int> &v, int n, int k) {
        int i;
        for (i = k - 1; i >= 0; --i) {
            if (v[i] < i + n + 1 - k) {
                break;
            }
        }
        if (i < 0) {
            return false;
        }
        ++v[i++];
        while (i < k) {
            v[i] = v[i - 1] + 1;
            ++i;
        }
        return true;
    }
};
