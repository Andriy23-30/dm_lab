from typing import List, Tuple


def read_graph_from_file(file_path: str) -> Tuple[int, List[List[int]]]:
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())
        graph = []
        for i in range(n):
            row = list(map(int, f.readline().strip().split()))
            graph.append(row)
    return n, graph


def find_path(graph: List[List[int]], source: int, sink: int, parent: List[int]) -> bool:
    n = len(graph)
    visited = [False] * n
    queue = []
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[sink]


def ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    n = len(graph)
    parent = [-1] * n
    max_flow = 0

    while find_path(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == '__main__':
    file_path = 'data.txt'
    n, graph = read_graph_from_file(file_path)
    source = 0
    sink = n - 1
    max_flow = ford_fulkerson(graph, source, sink)
    print(f"Maximum flow: {max_flow}")
