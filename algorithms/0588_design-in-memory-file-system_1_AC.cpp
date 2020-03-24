// I hate multiple inheritance, but I hate this problem even more.
// So be it.
#include <map>
#include <string>
#include <vector>
using std::map;
using std::string;
using std::vector;

static const int TYPE_FILE = 1;
static const int TYPE_DIR = 2;

class Node {
public:
    Node(const string &_name): name(_name) {}
    
    string getName() {
        return name;
    }
    
    virtual int type() = 0;
protected:
    string name;
};

class FileInterface {
public:
    virtual string getContent() = 0;
    virtual void appendContent(const string &s) = 0;
    virtual void setContent(const string &s) = 0;
};

class FileNode: public Node, public FileInterface {   
public:
    FileNode(const string &_name): Node(_name), content("") {}
    
    virtual int type() {
        return TYPE_FILE;
    }
    
    virtual string getContent() {
        return content;
    }
    
    virtual void appendContent(const string &s) {
        content += s;
    }
    
    virtual void setContent(const string &s) {
        content = s;
    }
protected:
    string content;
};

class DirInterface {
public:
    virtual Node *getChild(const string &_name) = 0;
    virtual void addChild(const string &_name, Node *_node) = 0;
    virtual vector<string> getList() = 0;
};

class DirNode: public Node, public DirInterface {
public:
    DirNode(const string &_name): Node(_name) {}
    
    virtual int type() {
        return TYPE_DIR;
    }
    
    virtual Node *getChild(const string &_name) {
        if (child.find(_name) != child.end()) {
            return child[_name];
        } else {
            return NULL;
        }
    }
    
    virtual void addChild(const string &_name, Node *_node) {
        if (_name == "" || _node == NULL) {
            return;
        }
        
        Node *ptr = getChild(_name);
        if (ptr != NULL) {
            delete ptr;
        }
        child[_name] = _node;
    }

    virtual vector<string> getList() {
        vector<string> res;
        for (auto &p: child) {
            res.push_back(p.first);
        }
        return res;
    }
protected:
    map<string, Node *> child;
};

class FileSystem {
public:
    FileSystem() {
        root = new DirNode("");
    }
    
    vector<string> ls(string path) {
        vector<string> vt = tokenize(path);
        Node *ptr = root;
        Node *ptr1;
        
        // Needed for type casting
        DirInterface *pd;
        FileInterface *pf;
        
        for (auto &tk: vt) {
            if (ptr->type() != TYPE_DIR) {
                return vector<string>();
            }
            pd = (DirNode *)ptr;
            if ((ptr1 = pd->getChild(tk)) == NULL) {
                return vector<string>();
            }
            ptr = ptr1;
        }
        if (ptr->type() == TYPE_DIR) {
            pd = (DirNode *)ptr;
            return pd->getList();
        } else {
            vector<string> res;
            res.push_back(ptr->getName());
            return res;
        }
    }
    
    void mkdir(string path) {
        vector<string> vt = tokenize(path);
        Node *ptr = root;
        Node *ptr1;
        
        // Needed for type casting
        DirInterface *pd;
        FileInterface *pf;
        
        for (auto &tk: vt) {
            pd = (DirNode *)ptr;
            if ((ptr1 = pd->getChild(tk)) == NULL) {
                ptr1 = new DirNode(tk);
                pd->addChild(tk, ptr1);
            }
            ptr = ptr1;
        }
    }
    
    void addContentToFile(string filePath, string content) {
        vector<string> vt = tokenize(filePath);
        Node *ptr = root;
        Node *ptr1;
        
        // Needed for type casting
        DirInterface *pd;
        FileInterface *pf;
        
        int n = vt.size();
        int i;
        for (i = 0; i < n - 1; ++i) {
            pd = (DirNode *)ptr;
            if ((ptr1 = pd->getChild(vt[i])) == NULL) {
                ptr1 = new DirNode(vt[i]);
                pd->addChild(vt[i], ptr1);
            }
            ptr = ptr1;
        }
        pd = (DirNode *)ptr;
        if ((ptr1 = pd->getChild(vt[n - 1])) == NULL) {
            ptr1 = new FileNode(vt[n - 1]);
            pd->addChild(vt[n - 1], ptr1);
        }
        ptr = ptr1;
        
        if (ptr->type() == TYPE_DIR) {
            // Error
            return;
        }
        pf = (FileNode *)ptr;
        pf->appendContent(content);
    }
    
    string readContentFromFile(string filePath) {
        vector<string> vt = tokenize(filePath);
        Node *ptr = root;
        Node *ptr1;
        
        // Needed for type casting
        DirInterface *pd;
        FileInterface *pf;
        
        for (auto &tk: vt) {
            pd = (DirNode *)ptr;
            if ((ptr1 = pd->getChild(tk)) == NULL) {
                // Error
                return "";
            }
            ptr = ptr1;
        }
        if (ptr->type() != TYPE_FILE) {
            // Error
            return "";
        }
        pf = (FileNode *)ptr;
        return pf->getContent();
    }
private:
    Node *root;
    
    vector<string> tokenize(const string &s) {
        vector<string> v;
        string tk;
        
        int ls = s.size();
        int i = 0;
        while (true) {
            while (i < ls && s[i] == '/') {
                ++i;
            }
            if (i >= ls) {
                break;
            }
            while (i < ls && s[i] != '/') {
                tk.push_back(s[i++]);
            }
            v.push_back(tk);
            tk.clear();
            if (i >= ls) {
                break;
            }
        }
        
        return v;
    }
};

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * vector<string> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * string param_4 = obj.readContentFromFile(filePath);
 */
