#include <map>
using std::map;

class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
        c1 = c2 = 0;
    }
    
    void addNum(int num) {
        insert(m1, c1, num);
        balance();
    }
    
    double findMedian() {
        double res;
        if (c1 > c2) {
            res = m1.rbegin()->first;
        } else {
            res = (1.0 * m1.rbegin()->first + m2.begin()->first) / 2.0;
        }
        return res;
    }
    
    ~MedianFinder() {
        m1.clear();
        c1 = 0;
        m2.clear();
        c2 = 0;
    }
private:
    map<int, int> m1, m2;
    int c1, c2;
    
    void insert(map<int, int> &mm, int &cnt, int val) {
        ++mm[val];
        ++cnt;
    }

    void remove(map<int, int> &mm, int &cnt, int val) {
        if (mm.find(val) == mm.end()) {
            return;
        }
        --mm[val];
        if (mm[val] == 0) {
            mm.erase(val);
        }
        --cnt;
    }
    
    void balance() {
        int n1, n2;
        
        while (c1 < c2) {
            n2 = m2.begin()->first;
            remove(m2, c2, n2);
            insert(m1, c1, n2);
        }
        
        while (c1 > c2 + 1) {
            n1 = m1.rbegin()->first;
            remove(m1, c1, n1);
            insert(m2, c2, n1);
        }
        
        while (c2 > 0) {
            n1 = m1.rbegin()->first;
            n2 = m2.begin()->first;
            if (n1 <= n2) {
                break;
            }
            remove(m1, c1, n1);
            insert(m1, c1, n2);
            remove(m2, c2, n2);
            insert(m2, c2, n1);
        }
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
