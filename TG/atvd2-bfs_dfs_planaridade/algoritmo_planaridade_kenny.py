def dfs_find_cycle(graph, u, visited, parent, path):
  """
  Busca em profundidade para encontrar um ciclo.
  Quando encontra um vértice que já está no caminho atual (path) e
  que não é o pai, retorna o ciclo encontrado.
  """
  visited.add(u)
  path.append(u)
  for v in graph[u]:
    if v not in visited:
      parent[v] = u
      cycle = dfs_find_cycle(graph, v, visited, parent, path)
      if cycle:
        return cycle
    elif v in path and (parent.get(u, None) != v):
      # Ciclo encontrado; recupera a parte do path a partir de v.
      idx = path.index(v)
      return path[idx:].copy()
  path.pop()
  return None


def find_cycle(graph):
  """
  Tenta encontrar um ciclo em todo o grafo.
  Retorna uma lista com os vértices que formam um ciclo ou None se não houver.
  """
  visited = set()
  parent = {}
  for u in graph:
    if u not in visited:
      cycle = dfs_find_cycle(graph, u, visited, parent, [])
      if cycle:
        return cycle
  return None


def split_face(face, u, v):
  """
  Dada uma face (lista de vértices em ordem cíclica) que contém os vértices u e v,
  divide a face em duas novas faces obtidas
  percorrendo de u a v e de v a u (em ordem cíclica).
  """
  n = len(face)
  pos_u = face.index(u)
  pos_v = face.index(v)
  # Para facilitar, assumimos que a ordem da face é cíclica (sem repetir o primeiro vértice no fim)
  if pos_u <= pos_v:
    path1 = face[pos_u:pos_v + 1]
    path2 = face[pos_v:] + face[:pos_u + 1]
  else:
    path1 = face[pos_u:] + face[:pos_v + 1]
    path2 = face[pos_v:pos_u + 1]
  return path1, path2


def check_planarity(graph):
  """
  Função simplificada para testar a planaridade de um grafo sem o uso de bibliotecas externas.
  O grafo é representado como um dicionário onde:
     - as chaves são os vértices e
     - os valores são listas de vértices adjacentes.

  Retorna (True, embedding) se conseguir inserir todas as arestas de forma incremental
  sem cruzamentos ou (False, None) se alguma aresta não puder ser inserida.

  OBSERVAÇÕES:
    - Se o grafo for uma árvore (E = V - 1), retorna True imediatamente.
    - A abordagem incremental funciona “bem” para alguns grafos, mas não é robusta para todos os casos.
  """
  vertices = list(graph.keys())
  V = len(vertices)

  # Construir o conjunto de arestas (para grafo não direcionado)
  edges = set()
  for u in graph:
    for v in graph[u]:
      if u != v:  # elimina laços
        edge = frozenset((u, v))
        edges.add(edge)

  E = len(edges)
  # Se for árvore (ou seja, grafo acíclico conexo), é planar.
  if E == V - 1:
    return True, "Grafo é árvore (acíclico) → planar."

  # Tenta encontrar um ciclo para iniciar o embedding.
  cycle = find_cycle(graph)
  if not cycle:
    # Se não há ciclo, o grafo é acíclico (ou seja, árvore/flaoresta) → planar.
    return True, "Grafo é acíclico → planar."

  # Inicializa o embedding com a face formada pelo ciclo encontrado.
  embedding = [cycle]
  # Registra as arestas já embutidas (arestas do ciclo)
  embedded_edges = set()
  n = len(cycle)
  for i in range(n):
    u = cycle[i]
    v = cycle[(i + 1) % n]
    embedded_edges.add(frozenset((u, v)))

  # Define as arestas restantes (que não fazem parte do ciclo inicial)
  remaining_edges = edges - embedded_edges

  # Tenta inserir as arestas restantes de forma incremental.
  progress = True
  while remaining_edges and progress:
    progress = False
    removidos = set()
    # Percorre as arestas restantes
    for edge in list(remaining_edges):
      u, v = tuple(edge)
      inseriu = False
      # Procura uma face cujo contorno contenha tanto 'u' quanto 'v'
      for i, face in enumerate(embedding):
        if (u in face) and (v in face):
          # Insere a aresta dividindo a face em duas novas faces
          face1, face2 = split_face(face, u, v)
          # Remove a face antiga e adiciona as novas faces
          embedding.pop(i)
          embedding.append(face1)
          embedding.append(face2)
          embedded_edges.add(edge)
          removidos.add(edge)
          inseriu = True
          progress = True
          break
      # Se não achou face adequada, a inserção ficará para uma nova rodada
    # Remove as arestas que foram inseridas nesta iteração
    remaining_edges.difference_update(removidos)

  if remaining_edges:
    # Se restaram arestas que não foram inseridas, o algoritmo encerra dizendo que o grafo é não planar.
    return False, None
  else:
    return True, embedding


def main():
  # Exemplo 1: Grafo planar (não maximal) – uma “rede” simples
  # Esse grafo contém o ciclo 1-2-3-1 e outras arestas que podem ser inseridas incrementalmente.
  planar_graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4: [2, 3, 5],
    5: [4]
  }

  resultado, embedding = check_planarity(planar_graph)
  print("Teste do grafo planar:")
  print("O grafo é planar?", resultado)
  if resultado:
    print("Faces do embedding:")
    for face in embedding:
      print(face)
  print("\n" + "=" * 50 + "\n")

  # Exemplo 2: Grafo não planar – K5 (grafo completo com 5 vértices)
  nonplanar_graph = {
    1: [2, 3, 4, 5],
    2: [1, 3, 4, 5],
    3: [1, 2, 4, 5],
    4: [1, 2, 3, 5],
    5: [1, 2, 3, 4]
  }

  resultado, embedding = check_planarity(nonplanar_graph)
  print("Teste do grafo não planar (K5):")
  print("O grafo é planar?", resultado)
  if not resultado:
    print("Alguma(s) aresta(s) não puderam ser inseridas sem cruzamento.")


if __name__ == '__main__':
  main()