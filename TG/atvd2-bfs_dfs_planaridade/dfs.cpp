#include <bits/stdc++.h>
using namespace std;

void dfs(int node, vector<bool>&visitado, vector<vector<int>>&adj) {
    visitado[node] = true;
    cout << node << " ";
    for(auto vizinho : adj[node]) {
        if(!visitado[vizinho]) {
            dfs(vizinho, visitado, adj);
        }
    }
}
int main() {

    cin.tie(0) -> sync_with_stdio(0);

    int n, m;
    cin >> n >> m;

    vector<bool>visitado(n+1, false);
    vector<vector<int>>adj(n+1);

    for(int i=0; i<m; i++) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }

    // for(int j=1; j<=n; j++) {
    //     if(!visitado[j]) {
    //         dfs(j, visitado, adj);
    //     }
    // }
    // cout << "\n";

    dfs(1,visitado, adj);
}
//g++ -std=gnu++17 -O2 -static -o c dfs.cpp && ./c
/*
5 4
1 2
1 3
2 4
3 5
*/