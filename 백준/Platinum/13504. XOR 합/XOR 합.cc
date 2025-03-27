#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const int BITS = 31;

class Node {
public:
    Node* next[2];
    int size[2];

    Node() {
        next[0] = next[1] = nullptr;
        size[0] = size[1] = -1;
    }
};

class Trie {
public:
    Node* top;
    
    Trie() {
        top = new Node();
    }

    void insert(int num, int l) {
        Node* tmp = top;
        for (int i = BITS - 1; i >= 0; i--) {
            int bit = (num >> i) & 1;
            tmp->size[bit] = max(tmp->size[bit], l);
            if (!tmp->next[bit]) {
                tmp->next[bit] = new Node();
            }
            tmp = tmp->next[bit];
        }
    }

    int trav(int num, int l) {
        Node* tmp = top;
        int res = 0;
        for (int i = BITS - 1; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (tmp->size[1 - bit] >= l) {
                res |= (1 << i);
                tmp = tmp->next[1 - bit];
            } else {
                tmp = tmp->next[bit];
            }
        }
        return res;
    }
    
    void clear(Node* node) {
        if (!node) return;
        for (int i = 0; i < 2; i++) {
            if (node->next[i]) clear(node->next[i]);
        }
        delete node;
    }

    ~Trie() {
        clear(top);
    }
};

void solve() {
    int T;
    cin >> T;
    while (T--) {
        int N;
        cin >> N;
        vector<int> arr(N);
        for (int i = 0; i < N; i++) {
            cin >> arr[i];
        }
        
        Trie trie;
        int xor_arr[N+1] = {0};
        for (int i = 1; i <= N; i++) {
            xor_arr[i] = xor_arr[i - 1] ^ arr[i - 1];
            trie.insert(xor_arr[i], i);
        }
        
        int res = -1;
        for (int i = 0; i <= N; i++) {
            res = max(res, trie.trav(xor_arr[i], i));
        }
        
        cout << res << "\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}