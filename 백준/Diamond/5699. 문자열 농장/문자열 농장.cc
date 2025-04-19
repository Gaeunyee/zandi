#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

const int INF = 1000000;

struct Node {
    bool eos;
    vector<pair<char, Node*>> next;
    Node* fail;
    vector<Node*> inv_fail;
    int visited;
    int deg;

    Node() {
        eos = false;
        fail = nullptr;
        visited = -1;
        deg = 1;
    }

    ~Node() {
        for (auto& p : next) {
            delete p.second;
        }
    }
};

class Trie {
public:
    Node* top;

    Trie() {
        top = new Node();
    }

    ~Trie() {
        delete top;
    }

    Node* find(Node* node, char a) {
        for (auto& [c, p] : node->next) {
            if (c == a) return p;
        }
        return nullptr;
    }

    Node* insert(const string& s) {
        Node* tmp = top;
        for (char key : s) {
            Node* n = find(tmp, key);
            if (!n) {
                Node* p = new Node();
                tmp->next.emplace_back(key, p);
                tmp = p;
            }
            else {
                tmp = n;
            }
        }
        tmp->eos = true;
        return tmp;
    }

    void setFail() {
        queue<Node*> qu;
        top->fail = top;
        qu.push(top);

        while (!qu.empty()) {
            Node* tmp = qu.front();
            qu.pop();

            for (auto& [c, nxt] : tmp->next) {
                Node* tr = tmp->fail;

                if (tmp == top) {
                    nxt->fail = top;
                    qu.push(nxt);
                    continue;
                }

                Node* n = find(tr, c);
                while (!n) {
                    if (tr == top) break;
                    tr = tr->fail;
                    n = find(tr, c);
                }

                if (n) {
                    nxt->fail = n;
                    nxt->deg++;
                    n->inv_fail.push_back(nxt);
                }
                else {
                    nxt->fail = tr;
                    nxt->deg++;
                    tr->inv_fail.push_back(nxt);
                }

                qu.push(nxt);
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        int N;
        cin >> N;
        if (N == 0) break;

        Trie trie;
        string s;

        for (int i = 0; i < N; ++i) {
            cin >> s;
            trie.insert(s);
        }

        trie.setFail();

        trie.top->visited = 0;
        vector<Node*> qu;
        qu.push_back(trie.top);
        int res = 0;

        while (!qu.empty()) {
            Node* tmp = qu.back();
            qu.pop_back();

            int d = tmp->visited;
            res = max(res, d);

            for (auto& [c, nxt] : tmp->next) {
                if (nxt->visited < d + (nxt->eos ? 1 : 0)) {
                    nxt->visited = d + (nxt->eos ? 1 : 0);
                }
                nxt->deg--;
                if (nxt->deg == 0) {
                    qu.push_back(nxt);
                }
            }

            for (Node* nxt : tmp->inv_fail) {
                if (nxt->visited < d + (nxt->eos ? 1 : 0)) {
                    nxt->visited = d + (nxt->eos ? 1 : 0);
                }
                nxt->deg--;
                if (nxt->deg == 0) {
                    qu.push_back(nxt);
                }
            }
        }

        cout << res << "\n";
    }

    return 0;
}
