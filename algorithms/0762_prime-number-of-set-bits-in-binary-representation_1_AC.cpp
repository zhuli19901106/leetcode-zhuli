#include <vector>
using std::vector;

class Solution {
public:
    Solution() {
        int MAX_BITS = 65;
        is_prime.resize(MAX_BITS + 1);
        int i;
        for (i = 0; i <= MAX_BITS; ++i) {
            is_prime[i] = isPrime(i);
        }
    }
    
    ~Solution() {
        is_prime.clear();
    }
    
    int countPrimeSetBits(int L, int R) {
        int res = 0;
        int i;
        int cnt;
        for (i = L; i <= R; ++i) {
            cnt = countOne(i);
            if (is_prime[cnt]) {
                ++res;
            }
        }
        return res;
    }
private:
    vector<bool> is_prime;

    bool isPrime(int n) {
        if (n < 2) {
            return false;
        }
        int i;
        for (i = 2; i <= n / i; ++i) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
    
    int countOne(int n) {
        int cnt = 0;
        while (n != 0) {
            n = (n & n - 1);
            ++cnt;
        }
        return cnt;
    }
};