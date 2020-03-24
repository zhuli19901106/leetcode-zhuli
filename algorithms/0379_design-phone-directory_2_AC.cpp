// Apparently the challenge is to make your design work for n as large as INT_MAX.
// So let's try replacing the bit vector with a hash table.
#include <unordered_map>
#include <unordered_set>
using std::unordered_map;
using std::unordered_set;

class PhoneDirectory {
public:
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    PhoneDirectory(int maxNumbers) {
        n = maxNumbers;
        na = n;
        m1[0] = n - 1;
        m2[n - 1] = 0;
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    int get() {
        if (na == 0) {
            return -1;
        }
        
        int i = m1.begin()->first;
        int j = m1[i];
        m1.erase(i);
        if (i == j) {
            m2.erase(j);
        } else {
            m1[i + 1] = j;
            m2[j] = i + 1;
        }
        
        b.insert(i);
        --na;
        
        return i;
    }
    
    /** Check if a number is available or not. */
    bool check(int number) {
        int i = number;
        return b.find(i) == b.end();
    }
    
    /** Recycle or release a number. */
    void release(int number) {
        int i = number;
        if (check(i)) {
            return;
        }
        
        int ll, rr;
        if (i - 1 >= 0 && check(i - 1)) {
            ll = m2[i - 1];
            m2.erase(i - 1);
        } else {
            ll = i;
        }
        if (i + 1 <= n - 1 && check(i + 1)) {
            rr = m1[i + 1];
            m1.erase(i + 1);
        } else {
            rr = i;
        }
        
        m1[ll] = rr;
        m2[rr] = ll;
        
        b.erase(i);
        ++na;
    }
    
    ~PhoneDirectory() {
        b.clear();
        m1.clear();
        m2.clear();
    }
private:
    int n;
    int na;
    unordered_set<int> b;
    unordered_map<int, int> m1, m2;
};

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * bool param_2 = obj.check(number);
 * obj.release(number);
 */
