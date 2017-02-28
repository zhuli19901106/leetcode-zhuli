// Trade time for space.
#include <algorithm>
#include <vector>
using std::lower_bound;
using std::vector;

class TwoSum {
public:
    /** Initialize your data structure here. */
    TwoSum() {}
    
    /** Add the number to an internal data structure.. */
    void add(int number) {
        v.insert(lower_bound(v.begin(), v.end(), number), number);
    }
    
    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        int n = v.size();
        int i = 0;
        int j = n - 1;
        int sum;
        while (i < j) {
            sum = v[i] + v[j];
            if (sum < value) {
                ++i;
            } else if (sum > value) {
                --j;
            } else {
                return true;
            }
        }
        return false;
    }
    
    ~TwoSum() {
        v.clear();
    }
private:
    vector<int> v;
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * bool param_2 = obj.find(value);
 */
