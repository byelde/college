#include <bits/stdc++.h>
using namespace std;

void bfs(int node, vector<bool>&visitado, vector<vector<int>>&adj){

    queue<int>fila;

    fila.push(node);

    visitado[node] = true;
    
    while(!fila.empty()) {
        // pop() remove o 1º da fila
        int vertice = fila.front(); fila.pop();
        cout<<vertice<<" ";
        for(auto vizinho : adj[vertice]){
            if(!visitado[vizinho]){
                visitado[vizinho] = true;
                fila.push(vizinho);
            }
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
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    bfs(1, visitado, adj);

    cout<<"\n";
}

//g++ -std=gnu++17 -O2 -static -o c bfs.cpp && ./c
/*
5 5
1 2
1 3
1 4
2 3
5 4
*/