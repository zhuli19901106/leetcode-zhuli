// easy
// https://leetcode.com/problems/design-hashmap/
#include <cmath>
using std::abs;

static const double LOAD_FACTOR_CAP = 0.4;
static const int IDX_NOT_FOUND = -1;

class MyHashMap {
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        _init(100000);
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        _put(key, value, true);
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int idx = _get_index(key);
        if (_used[idx]) {
            return _data_value[idx];
        } else {
            return IDX_NOT_FOUND;
        }
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int idx = _get_index(key);
        if (!_used[idx]) {
            return;
        }
        _used[idx] = false;
        --_size;
    }
private:
    vector<int> _data;
    vector<int> _data_value;
    vector<bool> _used;
    int _cap;
    int _size;

    void _init(int cap) {
        _cap = cap;

        _data.clear();
        _data_value.clear();
        _used.clear();

        _data.resize(_cap);
        _data_value.resize(_cap);
        _used.resize(_cap, false);

        _size = 0;
    }

    int _get_index(int key) {
        int probe = 0;
        int idx;
        while (true) {
            idx = abs(key + probe) % _cap;
            if (!_used[idx] || (key == _data[idx])) {
                return idx;
            } else {
                ++probe;
            }
        }
        // not supoosed to be here
        return IDX_NOT_FOUND;
    }

    // bugged
    void _rehash() {
        vector<int> keys;
        vector<int> values;
        for (int i = 0; i < _cap; ++i) {
            if (_used[i]) {
                keys.push_back(_data[i]);
                values.push_back(_data_value[i]);
            }
        }

        _init(_cap * 2);
        int n = keys.size();
        for (int i = 0; i < n; ++i) {
            _put(keys[i], values[i], false);
        }
    }

    void _put(int key, int value, bool rehash) {
        if (rehash && (_load_factor() >= LOAD_FACTOR_CAP)) {
            _rehash();
        }

        int idx = _get_index(key);
        _data[idx] = key;
        _data_value[idx] = value;
        if (!_used[idx]) {
            _used[idx] = true;
            ++_size;
        }
    }

    double _load_factor() {
        return 1.0 * _size / _cap;
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */
