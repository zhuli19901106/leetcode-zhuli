#include <cstdint>
#include <sstream>
#include <string>
using std::string;
using std::stringstream;
using std::to_string;

typedef struct Fraction {
public:
    int64_t x, y;
    
    Fraction(int64_t _x, int64_t _y = 1) {
        x = _x;
        y = _y;
        normalize();
    }
    
    Fraction operator + (const Fraction &f) {
        return Fraction(x * f.y + y * f.x, y * f.y);
    }
    
    string toString() {
        return to_string(x) + "/" + to_string(y);
    }
private:
    void normalize() {
        if (x == 0) {
            y = 1;
            return;
        }
        if (y < 0) {
            x = -x;
            y = -y;
        }
        
        int64_t g = gcd(x, y);
        x /= g;
        y /= g;
    }
    
    int64_t gcd(int64_t x, int64_t y) {
        if (x < 0) {
            return gcd(-x, y);
        }
        if (y < 0) {
            return gcd(x, -y);
        }
        
        int64_t t;
        while (y != 0) {
            t = x % y;
            x = y;
            y = t;
        }
        return x;
    }
} Fraction;

class Solution {
public:
    string fractionAddition(string expression) {
        Fraction sum(0);
        int x, y;
        stringstream ss(expression);
        
        while (true) {
            if (!(ss >> x)) {
                break;
            }
            if (ss.peek() == '/') {
                ss.ignore();
            }
            ss >> y;
            sum = sum + Fraction(x, y);
        }
        return sum.toString();
    }
};
