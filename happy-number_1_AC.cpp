#include <unordered_set>
using std::unordered_set;

class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> us;
        while (us.find(n) == us.end()) {
            us.insert(n);
            n = dss(n);
        }
        us.clear();
        return n == 1;
    }
private:
    // Sum of squares of digits.
    int dss(int n) {
        int sum = 0;
        int d;
        while (n != 0) {
            d = n % 10;
            n /= 10;
            sum += d * d;
        }
        return sum;
    }
};
