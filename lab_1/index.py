import heapq


# функція для зчитування матриці ваг
def read_weight_matrix(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline())
        weights = []
        for i in range(n):
            row = list(map(int, file.readline().split()))
            weights.append(row)
    return weights


# функція для виконання алгоритму Прим
def prim(weights):
    n = len(weights)
    mst = []  # остове дерево
    visited = [False] * n
    heap = [(0, 0)]  # черга з відстанями та вершинами
    while heap:
        (w, u) = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        mst.append((w, u))
        for v in range(n):
            if weights[u][v] > 0 and not visited[v]:
                heapq.heappush(heap, (weights[u][v], v))
    return mst


# зчитування ваг з файлу та виклик функції prim
if __name__ == '__main__':
    weights = read_weight_matrix('data.txt')
    mst = prim(weights)
    print(mst, sep='\n')
