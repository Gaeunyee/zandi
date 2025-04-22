#include <iostream>
#include <vector>
#include <bitset>
using namespace std;

const int LOG = 20;
int N, M;
vector<int> candy;
vector<bool> mask(6, false);
vector<vector<int>> tree;
vector<int> depth;
vector<vector<int>> parent;
vector<vector<int>> bit_mask;

void dfs(int n, int d) {
    depth[n] = d;
    for (int next : tree[n]) {
        if (depth[next] == -1) {
            parent[next][0] = n;
            depth[next] = d + 1;
            bit_mask[next][0] = (1 << (candy[n] - 1)) | (1 << (candy[next] - 1));
            dfs(next, d + 1);
        }
    }
}

void setPar() {
    dfs(1, 0);
    for (int j = 1; j < LOG; j++) {
        for (int i = 1; i <= N; i++) {
            parent[i][j] = parent[parent[i][j - 1]][j - 1];
            bit_mask[i][j] = bit_mask[i][j - 1] | bit_mask[parent[i][j - 1]][j - 1];
        }
    }
}

bool LCA(int x, int y, int c) { // x < y
    int ret = (1 << (candy[x] - 1)) | (1 << (candy[y] - 1));
    if (ret & (1 << (c - 1))) return true;

    for (int i = LOG - 1; i >= 0; i--) {
        if (depth[y] - depth[x] >= (1 << i)) {
            if (bit_mask[y][i] & (1 << (c - 1))) return true;
            y = parent[y][i];
        }
    }
    if (x == y) return ret & (1 << (c - 1));

    for (int i = LOG - 1; i >= 0; i--) {
        if (parent[x][i] != parent[y][i]) {
            if ((bit_mask[y][i] | bit_mask[x][i]) & (1 << (c - 1))) return true;
            x = parent[x][i];
            y = parent[y][i];
        }
    }
    return (bit_mask[y][0] | bit_mask[x][0]) & (1 << (c - 1));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    candy.resize(N + 1);
    tree.resize(N + 1);
    depth.assign(N + 1, -1);
    parent.assign(N + 1, vector<int>(LOG, 0));
    bit_mask.assign(N + 1, vector<int>(LOG, 0));

    for (int i = 1; i <= N; i++) {
        cin >> candy[i];
        mask[candy[i]] = true;
    }

    for (int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        tree[a].push_back(b);
        tree[b].push_back(a);
    }

    depth[1] = 0;
    bit_mask[1][0] = 1 << (candy[1] - 1);
    setPar();

    cin >> M;
    int pa, pc;
    cin >> pa >> pc;

    if (mask[pc]) cout << "PLAY\n";
    else cout << "CRY\n";

    for (int i = 1; i < M; i++) {
        int ta, tc;
        cin >> ta >> tc;

        if (depth[ta] > depth[pa]) {
            if (LCA(pa, ta, tc)) cout << "PLAY\n";
            else cout << "CRY\n";
        }
        else {
            if (LCA(ta, pa, tc)) cout << "PLAY\n";
            else cout << "CRY\n";
        }
        pa = ta;
    }

    return 0;
}
