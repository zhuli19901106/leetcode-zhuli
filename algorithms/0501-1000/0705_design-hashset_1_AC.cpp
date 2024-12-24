// easy
// https://leetcode.com/problems/design-hashset/
#include <cmath>
using std::abs;

static const double LOAD_FACTOR_CAP = 0.4;
static const int IDX_NOT_FOUND = -1;

class MyHashSet {
public:
    /** Initialize your data structure here. */
    MyHashSet() {
        _init(100000);
    }

    void add(int key) {
        _add(key, true);
    }

    void remove(int key) {
        int idx = _get_index(key);
        if (!_used[idx]) {
            return;
        }
        _used[idx] = false;
        --_size;
    }

    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int idx = _get_index(key);
        return _used[idx];
    }
private:
    vector<int> _data;
    vector<bool> _used;
    int _cap;
    int _size;

    void _init(int cap) {
        _cap = cap;
        _data.clear();
        _used.clear();
        _data.resize(_cap);
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
        for (int i = 0; i < _cap; ++i) {
            if (_used[i]) {
                keys.push_back(_data[i]);
            }
        }

        _init(_cap * 2);
        int n = keys.size();
        for (int i = 0; i < n; ++i) {
            _add(keys[i], false);
        }
    }

    void _add(int key, bool rehash) {
        if (rehash && (_load_factor() >= LOAD_FACTOR_CAP)) {
            _rehash();
        }

        int idx = _get_index(key);
        if (_used[idx]) {
            return;
        }
        _data[idx] = key;
        _used[idx] = true;
        ++_size;
    }

    double _load_factor() {
        return 1.0 * _size / _cap;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */;
