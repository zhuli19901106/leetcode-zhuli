class Solution {
public:
    vector<int> lexicalOrder(int n) {
        vector<int> res;
        int i;
        int num = 1;
        for (i = 1; i <= n; ++i) {
            res.push_back(num);
            num = nextNum(num, n);
        }
        return res;
    }
private:
    const int R = 10;
    
    int nextNum(int num, const int &n) {
        if (num <= n / R) {
            num *= R;
            return num;
        }
        if (num == n) {
            num /= R;
        }
        while (num % R == R - 1) {
            num /= R;
        }
        num += 1;
        return num;
    }
};
