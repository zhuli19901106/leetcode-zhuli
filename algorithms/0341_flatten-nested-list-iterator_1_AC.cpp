// That was pretty ugly.
// One of the most foolish feature in C++ is the write-once reference.
// I don't see why they forbid reference reassignent.
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        if (nestedList.size() == 0) {
            return;
        }
        
        arr.push(&nestedList);
        pos.push(0);
    }

    int next() {
        prepareNext();
        int res = (*arr.top())[pos.top()].getInteger();
        ++pos.top();
        return res;
    }

    bool hasNext() {
        prepareNext();
        return !arr.empty();
    }
private:
    stack<const vector<NestedInteger> *> arr;
    stack<int> pos;
    
    void prepareNext() {
        const vector<NestedInteger> *plist;
        while (!arr.empty()) {
            while (pos.top() < arr.top()->size() && !((*arr.top())[pos.top()].isInteger())) {
                plist = &((*arr.top())[pos.top()].getList());
                arr.push(plist);
                pos.push(0);
            }
            while (pos.top() == arr.top()->size()) {
                arr.pop();
                pos.pop();
				if (arr.empty()) {
					break;
				} else {
					++pos.top();
				}
            }
			if (arr.empty() || ((pos.top() < arr.top()->size() && (*arr.top())[pos.top()].isInteger()))) {
				break;
			}
        }
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
