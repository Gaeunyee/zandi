#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Node {
public:
    int idx;
    int N, size;
    vector<int> graph;
    vector<int> tree;
    int treeSize, startIndex;

    Node(vector<int>& next, int idx) {
        this->idx = idx;
        this->N = next.size();
        this->size = this->N;
        this->graph.push_back(0); // Placeholder for 1-based indexing
        this->graph.insert(this->graph.end(), next.begin(), next.end());
        this->treeSize = pow(2, ceil(log2(this->N)) + 1);
        this->tree.resize(this->treeSize+20, 0);
        this->startIndex = this->treeSize / 2 - 1;

        for (int i = 0; i < this->N; ++i) {
            this->tree[this->startIndex + 1 + i] = 1;
        }
    }

    void setTree() {
        for (int i = this->startIndex + this->N; i > 0; --i) {
            this->tree[i / 2] += this->tree[i];
        }
    }

    void editTree(int i) {
        while (i > 0) {
            this->tree[i] -= 1;
            i /= 2;
        }
    }

    int getSum(int start, int K) {
        int cnt = 0, idx = start - this->startIndex, size = 1;
        while (cnt < K) {
            if (start % 2 == 1) { // Right child
                if (this->tree[start] + cnt <= K) {
                    cnt += this->tree[start];
                    idx += size;
                    size = 1;
                    start = this->startIndex + idx;
                }
            }
            else {
                if (this->tree[start / 2] + cnt < K) {
                    start /= 2;
                    size *= 2;
                }
                else {
                    cnt += this->tree[start];
                    idx += size;
                    size = 1;
                    start = this->startIndex + idx;
                }
            }
        }
        return idx != 1 ? idx - 1 : 1;
    }

    int find(int t) {
        int l = 1, r = this->N;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (this->graph[mid] == t) {
                return mid;
            }
            else if (this->graph[mid] < t) {
                l = mid + 1;
            }
            else {
                r = mid - 1;
            }
        }
        return -1;
    }
};

vector<Node*> nodes;

void dfs(Node* t) {
    cout << t->idx << " ";
    for (int i : t->graph) {
        if (i == 0) continue;
        Node* n = nodes[i];
        int k = n->find(t->idx);
        if (k != -1) {
            n->editTree(n->startIndex + k);
            n->size -= 1;
        }
    }
    while (t->size != 0) {
        int nxt;
        if (t->size % 2 == 0) {
            nxt = t->getSum(t->startIndex + 1, 1);
        }
        else {
            nxt = t->getSum(t->startIndex + 1, t->size / 2 + 1);
        }
        dfs(nodes[t->graph[nxt]]);
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin >> N >> M;

    vector<vector<int>> graph(N + 1);
    nodes.push_back(nullptr); // Placeholder for 1-based indexing

    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        if (a == b) continue;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for (int i = 1; i <= N; ++i) {
        sort(graph[i].begin(), graph[i].end());
        graph[i].resize(unique(graph[i].begin(), graph[i].end()) - graph[i].begin());
        nodes.push_back(new Node(graph[i], i));
        nodes[i]->setTree();
    }

    dfs(nodes[1]);

    return 0;
}
