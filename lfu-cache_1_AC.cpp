// I haven't found a pure O(1) solution.
// Getting the lowest frequency doesn't seem to be an O(1) operation.
// If not a <map>, what should I do?
#include <map>
#include <unordered_map>
using std::map;
using std::unordered_map;

typedef struct DoubleListNode {
    int key, value;
    int freq;
    DoubleListNode *prev, *next;
    
    DoubleListNode(int _key, int _value): key(_key), value(_value), freq(1), 
        prev(NULL), next(NULL) {}
} DLN;

class LFUCache {
public:
    LFUCache(int capacity) {
        this->capacity = capacity;
        this->size = 0;
    }
    
    int get(int key) {
        if (m_node.find(key) == m_node.end()) {
            return -1;
        }
        DLN *p = m_node[key];
        removeNode(p);
        ++(p->freq);
        insertNode(p);
        
        return p->value;
    }
    
    void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        
        DLN *p;
        if (m_node.find(key) != m_node.end()) {
            p = m_node[key];
            removeNode(p);
            ++(p->freq);
            
            p->value = value;
            insertNode(p);
            return;
        }
        
        if (size < capacity) {
            p = new DLN(key, value);
            insertNode(p);
            m_node[key] = p;
            ++size;
            return;
        }
        
        p = m_tail.begin()->second;
        removeNode(p);
        m_node.erase(p->key);
        
        p->key = key;
        p->value = value;
        p->freq = 1;
        insertNode(p);
        m_node[key] = p;
    }
    
    ~LFUCache() {
        m_head.clear();
        m_tail.clear();
        m_node.clear();
        
        size = 0;
    }
private:
    int capacity;
    int size;
    map<int, DLN *> m_head, m_tail;
    unordered_map<int, DLN *> m_node;
    
    void insertNode(DLN *p) {
        if (p == NULL) {
            return;
        }
        
        int f = p->freq;
        if (m_head.find(f) == m_head.end()) {
            m_head[f] = m_tail[f] = p;
        }
        DLN *h = m_head[f];
        p->next = h;
        h->prev = p;
        m_head[f] = p;
    }
    
    void removeNode(DLN *p) {
        if (p == NULL) {
            return;
        }
        
        int f = p->freq;
        DLN *h = m_head[f];
        DLN *t = m_tail[f];
        if (p == h && p == t) {
            m_head.erase(f);
            m_tail.erase(f);
            return;
        }
        if (p == h) {
            h = p->next;
            p->next = NULL;
            h->prev = NULL;
            m_head[f] = h;
            return;
        }
        if (p == t) {
            t = p->prev;
            p->prev = NULL;
            t->next = NULL;
            m_tail[f] = t;
            return;
        }
        
        DLN *p1 = p->prev, *p2 = p->next;
        p1->next = p2;
        p2->prev = p1;
        p->prev = p->next = NULL;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
