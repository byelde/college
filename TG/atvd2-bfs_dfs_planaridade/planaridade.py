from typing import List, Dict, Tuple
from itertools import combinations


def temK5(dict_graus: Dict[int, int], matriz_adj: List[List[int]]) -> bool:

    vertices_grau_4oumais: List[int] = [key for key, value in dict_graus.items() if value >= 4]

    if len(vertices_grau_4oumais) < 5:
        return False

    combinacoes = list(combinations(vertices_grau_4oumais, 5))

    for i in range(len(combinacoes)):
        u, v, w, x, y = combinacoes[i]
        if all(a != b or matriz_adj[a][b] for a, b in combinations([u, v, w, x, y], 2)):
            return True
    return False


def dfs_bipartido(vertice: int, cores: Dict[int, int], cor_atual: int, adjs: List[List[int]]) -> Tuple[bool, Dict]:
    cores[vertice] = cor_atual

    for vert_vizinho in adjs[vertice]:
        if cores[vert_vizinho] != 0:
            if cores[vert_vizinho] == cor_atual:
                return False, {}
        else:
            if not dfs_bipartido(vert_vizinho, cores, -cor_atual, adjs)[0]:
                return False, {}
    return True, cores


def temK33(dict_graus: Dict[int, int], matriz_adj: List[List[bool]]) -> bool:

    vertices_grau_3oumais: List[int] = [key for key, value in dict_graus.items() if value >= 3]

    if len(vertices_grau_3oumais) < 6:
        return False

    combinacoes = list(combinations(vertices_grau_3oumais, 6))
    grafo_gerado: List[List[int]] = []

    tem_k33: bool = False

    for combinacao in combinacoes:
        grafo_gerado.clear()
        grafo_gerado = [[] for _ in range(10)]
        for possivel_aresta in combinations(combinacao, 2):
            u, v = possivel_aresta
            if matriz_adj[u][v]:
                grafo_gerado[u].append(v)
                grafo_gerado[v].append(u)

        if dfs_bipartido(0, {x:0 for x in range(10)}, 1, grafo_gerado)[0]:
            tem_k33 = True
            break

    return tem_k33


def verificarPlanaridade(num_vertices: int, matriz_adj: List[List[bool]], dict_graus: Dict[int, int]) -> str:
    if num_vertices <= 4:
        return "sim, menos de 4 vertices"
    elif temK5(dict_graus, matriz_adj):
        return "nao, possui k5"
    elif temK33(dict_graus, matriz_adj):
        return "nao, possui k3,3"
    else:
        return "sim, é planar"


def retirarGrau2(matriz_adj: List[List[bool]], dict_graus: Dict[int, int]) -> None:
    for i in range(len(matriz_adj)):
        if dict_graus[i] == 2:
            adjs: List[int] = []
            for j in range(len(matriz_adj)):
                if matriz_adj[i][j]:
                    adjs.append(j)
                    matriz_adj[i][j] = False
                    matriz_adj[j][i] = False
                    dict_graus[j] -= 1

            matriz_adj[adjs[0]][adjs[1]] = True
            matriz_adj[adjs[1]][adjs[0]] = True
            dict_graus[i] = 0


def main():
    matriz_adj_grafo: List[List[bool]] = [[False for __ in range(10)] for _ in range(10)]
    graus_vertices: Dict[int, int] = {i: 0 for i in range(10)}

    num_vertices: int
    num_arestas: int

    num_vertices, num_arestas = map(int, input().split())

    for _ in range(num_arestas):
        u, v = map(int, input().split())

        matriz_adj_grafo[u - 1][v - 1] = True
        matriz_adj_grafo[v - 1][u - 1] = True

        graus_vertices[u - 1] += 1
        graus_vertices[v - 1] += 1

    retirarGrau2(matriz_adj_grafo, graus_vertices)

    print(verificarPlanaridade(num_vertices, matriz_adj_grafo, graus_vertices))


if __name__ == "__main__":
    main()