class Solution {
public:
    int fib(int N) {
        if (N < 2) {
            return N;
        }
        int i;
        int f1 = 0, f2 = 1, f3;
        for (i = 2; i <= N; ++i) {
            f3 = f1 + f2;
            f1 = f2;
            f2 = f3;
        }
        return f3;
    }
};
