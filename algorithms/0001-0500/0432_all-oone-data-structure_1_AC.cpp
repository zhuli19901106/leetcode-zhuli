// I don't wanna lay my eyes on this code for one more second.
// Too complicated, too sloppy, although the idea is simple.
// std::list is a doubly linked list, so why bother writing your own?
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>
using std::list;
using std::string;
using std::unordered_map;
using std::unordered_set;

typedef unordered_set<string> USS;

class AllOne {
public:
    /** Initialize your data structure here. */
    AllOne() {}
    
    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    void inc(string key) {
        int val = m1.find(key) != m1.end() ? m1[key] : 0;
        ++m1[key];
        
        list<USS>::iterator it1, it2;
        it1 = val > 0 ? m2[val] : a.begin();
        if (m2.find(val + 1) == m2.end()) {
            it2 = a.insert(val > 0 ? next(it1) : a.begin(), USS());
            m2[val + 1] = it2;
        } else {
            it2 = m2[val + 1];
        }
        it2->insert(key);
        
        if (val > 0) {
            it1->erase(key);
            if (it1->size() == 0) {
                a.erase(it1);
                m2.erase(val);
            }
        }
    }
    
    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    void dec(string key) {
        int val = m1.find(key) != m1.end() ? m1[key] : 0;
        if (val == 0) {
            return;
        }
        if (val > 1) {
            --m1[key];
        } else {
            m1.erase(key);
        }
        
        list<USS>::iterator it1, it2;
        it1 = m2[val];
        if (val > 1) {
            if (m2.find(val - 1) == m2.end()) {
                it2 = a.insert(it1, USS());
                m2[val - 1] = it2;
            } else {
                it2 = m2[val - 1];
            }
            it2->insert(key);
        }
        
        it1->erase(key);
        if (it1->size() == 0) {
            a.erase(it1);
            m2.erase(val);
        }
    }
    
    /** Returns one of the keys with maximal value. */
    string getMaxKey() {
        if (a.size() == 0) {
            return "";
        }
        return *(a.back().begin());
    }
    
    /** Returns one of the keys with Minimal value. */
    string getMinKey() {
        if (a.size() == 0) {
            return "";
        }
        return *(a.front().begin());
    }
    
    ~AllOne() {
        a.clear();
        m1.clear();
        m2.clear();
    }
private:
    list<USS> a;
    unordered_map<string, int> m1;
    unordered_map<int, list<USS>::iterator> m2;
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne obj = new AllOne();
 * obj.inc(key);
 * obj.dec(key);
 * string param_3 = obj.getMaxKey();
 * string param_4 = obj.getMinKey();
 */
