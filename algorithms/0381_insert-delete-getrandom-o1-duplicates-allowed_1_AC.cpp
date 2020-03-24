// Same idea, different representation.
#include <cstdlib>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using std::rand;
using std::unordered_map;
using std::unordered_set;
using std::vector;

class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {}
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        bool found = (um.find(val) != um.end());
        int i = v.size();
        um[val].insert(i);
        v.push_back(val);
        
        return found;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        bool found = (um.find(val) != um.end());
        if (!found) {
            return found;
        }
        
        int i = *(um[val].begin());
        int j = v.size() - 1;
        int other_val = v[j];
        
        if (other_val == val) {
            um[val].erase(j);
        } else {
            um[other_val].erase(j);
            um[val].erase(i);
            um[other_val].insert(i);
            v[i] = other_val;
        }
        v.pop_back();
        
        if (um[val].size() == 0) {
            um.erase(val);
        }
        
        return found;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        return v[rand() % v.size()];
    }
    
    ~RandomizedCollection() {
        um.clear();
        v.clear();
    }
private:
    unordered_map<int, unordered_set<int>> um;
    vector<int> v;
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
