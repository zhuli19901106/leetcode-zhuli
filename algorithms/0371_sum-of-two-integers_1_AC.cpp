// Adder design.
class Solution {
public:
    int getSum(int a, int b) {
        int s;
        int c;
        // Look out for the precedence problem.
        while ((a & b) != 0) {
            s = a ^ b;
            c = (a & b) << 1;
            a = s;
            b = c;
        }
        return a | b;
    }
};
