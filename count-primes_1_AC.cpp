// In memory of Eratosthenes of Cyrene.
#include <vector>
using std::vector;

class Solution {
public:
    int countPrimes(int n) {
        vector<bool> is_prime(n + 1, true);
        int i, j;
        
        is_prime[0] = is_prime[1] = false;
        for (i = 2; i <= n / i; ++i) {
            if (!is_prime[i]) {
                continue;
            }
            for (j = i; j <= n / i; ++j) {
                is_prime[i * j] = false;
            }
        }
        int sum = 0;
        for (i = 0; i <= n - 1; ++i) {
            if (is_prime[i]) {
                ++sum;
            }
        }
        is_prime.clear();
        return sum;
    }
};
