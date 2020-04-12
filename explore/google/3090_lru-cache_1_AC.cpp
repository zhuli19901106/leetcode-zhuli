// Write your own doubly linked list.
#include <unordered_map>
using std::unordered_map;

typedef struct DoubleListNode {
    int key, val;
    struct DoubleListNode *prev, *next;
    
    DoubleListNode(int _key, int _val):key(_key), val(_val) {
        prev = next = NULL;
    }
} DLN;

class LRUCache {
public:
    LRUCache(int capacity) {
        head = tail = NULL;
        cap = capacity;
    }
    
    int get(int key) {
        if (um.find(key) == um.end()) {
            return -1;
        }
        DLN *t = um[key];
        insertHead(remove(t));
        
        return t->val;
    }
    
    void put(int key, int value) {
        if (cap == 0) {
            return;
        }
        
        DLN *t;
        int old_key;
        if (um.find(key) == um.end()) {
            if (um.size() < cap) {
                t = new DLN(key, value);
                um[key] = t;
                
                insertHead(t);
            } else {
                old_key = tail->key;
                um.erase(old_key);
                
                t = remove(tail);
                t->key = key;
                t->val = value;
                um[key] = t;
                
                insertHead(t);
            }
        } else {
            t = um[key];
            t->val = value;
            
            insertHead(remove(t));
        }
    }
    
    ~LRUCache() {
        um.clear();
        DLN *p = head;
        while (p != NULL) {
            head = head->next;
            delete p;
            p = head;
        }
        tail = NULL;
    }
private:
    unordered_map<int, DLN *> um;
    DLN *head, *tail;
    int cap;
    
    void insertHead(DLN *p) {
        if (head == NULL) {
            tail = p;
        } else {
            p->next = head;
            head->prev = p;
        }
        head = p;
    }
    
    DLN *remove(DLN *p) {
        if (head == p && tail == p) {
            head = tail = NULL;
            
            return p;
        }
        
        if (head == p) {
            head = p->next;
            head->prev = NULL;
            p->next = NULL;
            
            return p;
        }
        
        if (tail == p) {
            tail = p->prev;
            tail->next = NULL;
            p->prev = NULL;
            
            return p;
        }
        
        DLN *p1, *p2;
        p1 = p->prev;
        p2 = p->next;
        p1->next = p2;
        p2->prev = p1;
        p->prev = NULL;
        p->next = NULL;
        
        return p;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
