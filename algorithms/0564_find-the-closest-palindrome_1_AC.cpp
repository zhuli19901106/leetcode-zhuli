#include <cmath>
#include <cstdint>
#include <cstdio>
#include <string>
using std::log10;
using std::sscanf;
using std::string;
using std::to_string;

class Solution {
public:
    string nearestPalindromic(string n) {
        int64_t n0;
        sscanf(n.data(), "%lld", &n0);
        
        int64_t n1 = nextPal(n0 + 1);
        int64_t n2 = prevPal(n0 - 1);
        
        if (n1 - n0 < n0 - n2) {
            return to_string(n1);
        } else {
            return to_string(n2);
        }
    }
private:
    int64_t nextPal(int64_t n) {
        if (isPal(n)) {
            return n;
        }
        
        int nd = (int)log10(n) + 1;
        int64_t b10 = pow(10, nd >> 1);
        int64_t p1, p2, p3;
        
        if (nd & 1) {
            p1 = n / (b10 * 10);
            p2 = n % b10;
            p3 = n / b10 % 10;
        } else {
            p1 = n / b10;
            p2 = n % b10;
        }
        
        int64_t rp1 = reverseDigits(p1);
        if (rp1 < p2) {
            if ((nd & 1) && p3 < 9) {
                ++p3;
            } else {
                ++p1;
                rp1 = reverseDigits(p1);
                if (nd & 1) {
                    p3 = 0;
                }
            }
        }
        p2 = rp1;
        
        if (nd & 1) {
            n = p1 * (b10 * 10) + p3 * b10 + p2;
        } else {
            n = p1 * b10 + p2;
        }
        return n;
    }
    
    int64_t prevPal(int64_t n) {
        if (isPal(n)) {
            return n;
        }
        if (isPal(n - 1)) {
            return n - 1;
        }
        
        int nd = (int)log10(n) + 1;
        int64_t b10 = pow(10, nd >> 1);
        int64_t p1, p2, p3;
        
        if (nd & 1) {
            p1 = n / (b10 * 10);
            p2 = n % b10;
            p3 = n / b10 % 10;
        } else {
            p1 = n / b10;
            p2 = n % b10;
        }
        
        int64_t rp1 = reverseDigits(p1);
        if (rp1 > p2) {
            if ((nd & 1) && p3 > 0) {
                --p3;
            } else {
                --p1;
                rp1 = reverseDigits(p1);
                if (nd & 1) {
                    p3 = 9;
                }
            }
        }
        p2 = rp1;
        
        if (nd & 1) {
            n = p1 * (b10 * 10) + p3 * b10 + p2;
        } else {
            n = p1 * b10 + p2;
        }
        return n;
    }
    
    bool isPal(int64_t n) {
        int64_t n0 = n;
        int64_t n1 = 0;
        while (n != 0) {
            n1 = n1 * 10 + n % 10;
            n /= 10;
        }
        return n1 == n0;
    }
    
    int64_t reverseDigits(int64_t n) {
        int64_t n1 = 0;
        while (n != 0) {
            n1 = n1 * 10 + n % 10;
            n /= 10;
        }
        return n1;
    }
};
