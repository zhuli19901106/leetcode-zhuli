#include <cstdlib>
#include <unordered_map>
#include <vector>
using std::rand;
using std::unordered_map;
using std::vector;

class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {}
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (um.find(val) != um.end()) {
            return false;
        }
        int n = v.size();
        um[val] = n;
        v.push_back(val);
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (um.find(val) == um.end()) {
            return false;
        }
        int n = v.size();
        um[v.back()] = um[val];
        v[um[val]] = v.back();
        v.pop_back();
        um.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int r = rand() % v.size();
        return v[r];
    }
    
    ~RandomizedSet() {
        um.clear();
        v.clear();
    }
private:
    unordered_map<int, int> um;
    vector<int> v;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * bool param_1 = obj.insert(val);
 * bool param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
