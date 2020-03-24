#include <vector>
using std::vector;

class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        sum = 0;
        idx = -1;
        window = size;
    }
    
    double next(int val) {
        if (window == 0) {
            return 0;
        }
        sum += val;
        if (v.size() < window) {
            ++idx;
            v.push_back(val);
        } else {
            idx = (idx + 1) % window;
            sum -= v[idx];
            v[idx] = val;
        }
        
        return sum * 1.0 / v.size();
    }
    
    ~MovingAverage() {
        v.clear();
    }
private:
    vector<int> v;
    int sum;
    int idx;
    int window;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
