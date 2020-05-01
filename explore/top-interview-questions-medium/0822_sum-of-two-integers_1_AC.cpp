// Adder design.
class Solution {
public:
    int getSum(int a, int b) {
        uint32_t s, c;
        uint32_t aa, bb;
        // Look out for the precedence problem.
        aa = a;
        bb = b;
        while ((aa & bb) != 0) {
            s = aa ^ bb;
            c = (aa & bb) << 1;
            aa = s;
            bb = c;
        }
        return int(aa | bb);
    }
};
