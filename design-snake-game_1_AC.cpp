// Edge cases everywhere.
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

static const int offset[4][2] = {{-1, 0}, {+1, 0}, {0, -1}, {0, +1}};

typedef struct MyListNode {
    int x, y;
    struct MyListNode *next;
    
    MyListNode(int _x = 0, int _y = 0): x(_x), y(_y), next(NULL) {}
} MyListNode;

class SnakeGame {
public:
    /** Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0]. */
    SnakeGame(int width, int height, vector<pair<int, int>> food) {
        static const string sd = "UDLR";
        int ls = sd.size();
        int i;
        for (i = 0; i < ls; ++i) {
            di[sd[i]] = i;
        }
        
        n = height;
        m = width;
        
        int sx = 0;
        int sy = 0;
        head = tail = new MyListNode(sx, sy);
        
        f = food;
        fi = 0;
        if (fi < f.size()) {
            fx = f[fi].first;
            fy = f[fi].second;
        } else {
            fx = fy = -1;
        }
        
        b.resize(n, vector<bool>(m, false));
        b[sx][sy] = true;
        
        score = 0;
    }
    
    /** Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body. */
    int move(string direction) {
        int i = di[direction[0]];
        int x, y;
        
        x = tail->x + offset[i][0];
        y = tail->y + offset[i][1];
        if (!inbound(x, y) || (b[x][y] && !(x == head->x && y == head->y))) {
            // Game over
            // An edge case here, watch out.
            return -1;
        }
        
        if (x == fx && y == fy) {
            // Eat something
            tail->next = new MyListNode(x, y);
            tail = tail->next;
            b[x][y] = true;
            ++score;
            
            ++fi;
            if (fi < f.size()) {
                fx = f[fi].first;
                fy = f[fi].second;
            } else {
                fx = fy = -1;
            }
        } else {
            b[head->x][head->y] = false;
            head->x = x;
            head->y = y;
            b[x][y] = true;
            if (head != tail) {
                MyListNode *p = head;
                
                head = p->next;
                p->next = NULL;
                tail->next = p;
                tail = p;
            }
        }
        return score;
    }
    
    ~SnakeGame() {
        di.clear();
        b.clear();
        f.clear();
        
        MyListNode *p = head;
        while (head != NULL) {
            head = head->next;
            delete p;
            p = head;
        }
    }
private:
    unordered_map<char, int> di;
    
    MyListNode *head, *tail;
    int n, m;
    int fx, fy;
    int fi;
    vector<vector<bool>> b;
    vector<pair<int, int>> f;
    
    int score;
    
    bool inbound(int x, int y) {
        return x >= 0 && x <= n - 1 && y >= 0 && y <= m - 1;
    }
};

/**
 * Your SnakeGame object will be instantiated and called as such:
 * SnakeGame obj = new SnakeGame(width, height, food);
 * int param_1 = obj.move(direction);
 */
