/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
#include <map>
#include <unordered_set>
#include <vector>
using std::map;
using std::unordered_set;
using std::vector;

class SummaryRanges {
public:
    /** Initialize your data structure here. */
    SummaryRanges() {}
    
    void addNum(int val) {
        if (hash.find(val) != hash.end()) {
            return;
        }
        hash.insert(val);
        
        bool has_left = false;
        bool has_right = false;
        int left, right;
        
        if (m2.find(val - 1) != m2.end()) {
            has_left = true;
            left = m2[val - 1];
        }
        if (m1.find(val + 1) != m1.end()) {
            has_right = true;
            right = m1[val + 1];
        }
        
        if (has_left) {
            if (has_right) {
                m1[left] = right;
                m1.erase(val + 1);
                
                m2[right] = left;
                m2.erase(val - 1);
            } else {
                m1[left] = val;
                
                m2[val] = left;
                m2.erase(val - 1);
            }
        } else {
            if (has_right) {
                m1[val] = right;
                m1.erase(val + 1);
                
                m2[right] = val;
            } else {
                m1[val] = val;
                m2[val] = val;
            }
        }
    }
    
    vector<Interval> getIntervals() {
        vector<Interval> res;
        for (auto it = m1.begin(); it != m1.end(); ++it) {
            res.push_back(Interval(it->first, it->second));
        }
        return res;
    }
    
    ~SummaryRanges() {
        hash.clear();
        m1.clear();
        m2.clear();
    }
private:
    map<int, int> m1, m2;
    unordered_set<int> hash;
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * vector<Interval> param_2 = obj.getIntervals();
 */
 