// If hits/s is very high, process them in a batch.
// You can usually sacrifice some consistency for better availability.
#include <map>
using std::map;

class HitCounter {
public:
    /** Initialize your data structure here. */
    HitCounter() {}
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        ++mm[timestamp];
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        auto it1 = mm.upper_bound(timestamp - TIME_EXPIRE);
        auto it2 = mm.upper_bound(timestamp);
        int res = 0;
        for (auto it = it1; it != it2; ++it) {
            res += it->second;
        }
        return res;
    }
    
    ~HitCounter() {
        mm.clear();
    }
private:
    static const int TIME_EXPIRE = 300;
    
    map<int, int> mm;
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */
