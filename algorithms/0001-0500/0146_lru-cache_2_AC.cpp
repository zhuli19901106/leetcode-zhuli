#include <list>
#include <unordered_map>
#include <utility>
using std::list;
using std::make_pair;
using std::pair;
using std::unordered_map;

typedef list<pair<int, int>> LPII;

class LRUCache {
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if (um.find(key) == um.end()) {
            return -1;
        }
        
        LPII::iterator it = um[key];
        int value = it->second;
        if (it != v.begin()) {
            v.erase(it);
            it = v.insert(v.begin(), make_pair(key, value));
            um[key] = it;
        }
        
        return value;
    }
    
    void put(int key, int value) {
        if (cap == 0) {
            return;
        }
        
        LPII::iterator it;
        if (um.find(key) == um.end()) {
            if (um.size() == cap) {
                int old_key = v.back().first;
                it = um[old_key];
                v.erase(it);
                um.erase(old_key);
            }
            it = v.insert(v.begin(), make_pair(key, value));
            um[key] = it;
        } else {
            it = um[key];
            
            if (it != v.begin()) {
                v.erase(it);
                
                it = v.insert(v.begin(), make_pair(key, value));
                um[key] = it;
            } else {
                it->second = value;
            }
        }
    }
    
    ~LRUCache() {
        um.clear();
        v.clear();
    }
private:
    int cap;
    unordered_map<int, LPII::iterator> um;
    LPII v;
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
