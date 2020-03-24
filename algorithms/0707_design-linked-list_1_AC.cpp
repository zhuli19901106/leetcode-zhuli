// https://leetcode.com/problems/design-linked-list/
typedef struct MyListNode {
    int val;
    struct MyListNode *prev;
    struct MyListNode *next;
    MyListNode(int _val): val(_val), prev(nullptr), next(nullptr) {};
} MyListNode;

class MyLinkedList {
public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        _head = new MyListNode(0);
        _head->next = _head;
        _head->prev = _head;
        _size = 0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index < 0 || index > _size - 1) {
            return -1;
        }
        MyListNode *p = _head;
        for (int i = 0; i <= index; ++i) {
            p = p->next;
        }
        return p->val;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        _insertAfter(_head, val);
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        _insertAfter(_head->prev, val);
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > _size) {
            return;
        }
        if (index <= 0) {
            addAtHead(val);
            return;
        }
        if (index == _size) {
            addAtTail(val);
            return;
        }
        MyListNode *p = _head;
        for (int i = 0; i < index; ++i) {
            p = p->next;
        }
        _insertAfter(p, val);
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index < 0 || index > _size - 1) {
            return;
        }
        MyListNode *p1, *p2;
        p1 = _head;
        for (int i = 0; i < index; ++i) {
            p1 = p1->next;
        }
        p2 = p1->next;
        p1->next = p2->next;
        p2->next->prev = p1;
        delete p2;
        p2 = nullptr;
        --_size;
    }
private:
    MyListNode *_head;
    int _size;

    void _insertAfter(MyListNode* p, int val) {
        MyListNode *node = new MyListNode(val);
        MyListNode *p1 = p->next;
        p->next = node;
        node->prev = p;
        node->next = p1;
        p1->prev = node;
        ++_size;
        //print();
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
