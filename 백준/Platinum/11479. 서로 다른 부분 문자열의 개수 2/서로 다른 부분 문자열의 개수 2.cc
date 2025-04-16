#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

string str;
long long N;
long long t = 1;
vector<int> group(N + 1);

bool compare(int a, int b) {
    if (group[a] != group[b]) return group[a] < group[b];
    return group[a + t] < group[b + t];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> str;
    N = str.length();


    group.resize(N + 1);
    for (int i = 0; i < N; ++i) group[i] = str[i];
    group[N] = -1;

    vector<int> res(N);
    for (int i = 0; i < N; ++i) res[i] = i;


    while (t < N) {
        sort(res.begin(), res.end(), compare);

        vector<int> newGroup(N + 1, 0);
        newGroup[N] = -1;
        newGroup[res[0]] = 0;

        for (int i = 1; i < N; ++i) {
            if (compare(res[i - 1], res[i])) {
                newGroup[res[i]] = newGroup[res[i - 1]] + 1;
            }
            else {
                newGroup[res[i]] = newGroup[res[i - 1]];
            }
        }
        group = newGroup;
        t *= 2;

    }

    // str += '$';
    long long lcp = 0;
    long long d = 0;
    vector<int> ir(N);
    for (int i = 0; i < N; ++i) {
        ir[res[i]] = i;
    }


    for (int i = 0; i < N; ++i) {
        if (ir[i] == 0) continue;
        while (str[i + d] == str[res[ir[i] - 1] + d]) d++;
        lcp += d;
        d = (d ? d - 1 : 0);
    }

    cout << (long long)N * (N + 1) / 2 - lcp;
    return 0;
}
