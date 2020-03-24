// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
	Data* data;
public:
	Iterator(const vector<int>& nums);
	Iterator(const Iterator& iter);
	virtual ~Iterator();
	// Returns the next element in the iteration.
	int next();
	// Returns true if the iteration has more elements.
	bool hasNext() const;
};

class PeekingIterator : public Iterator {
    bool has_peek;
    int peek_item;
public:
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    has_peek = false;
	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if (!has_peek) {
            peek_item = Iterator::next();
            has_peek = true;
        }
        return peek_item;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
        if (has_peek) {
            has_peek = false;
            return peek_item;
        }
        return Iterator::next();
	}
    
	bool hasNext() const {
        return has_peek || Iterator::hasNext();
	}
};
