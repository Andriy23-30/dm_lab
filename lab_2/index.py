import heapq

def dijkstra(graph, start):
    # Ініціалізуємо всі відстані як нескінченність
    distances = {node: float('infinity') for node in graph}
    # Початкова відстань від початкової вершини до неї самої дорівнює 0
    distances[start] = 0

    # Використовуємо heapq для зберігання вершин в порядку зростання відстаней
    pq = [(0, start)]

    while len(pq) > 0:
        # Дістаємо вершину з мінімальною відстанню
        current_distance, current_node = heapq.heappop(pq)

        # Якщо ми вже дістались до цільової вершини, то можемо завершити пошук
        if current_distance > distances[current_node]:
            continue

        # Оновлюємо відстані до сусідніх вершин
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Відкриваємо файл з даними
with open('data.txt', 'r') as f:
    # Зчитуємо кількість вершин у графі
    n = int(f.readline())

    # Ініціалізуємо граф
    graph = {i: {} for i in range(n)}

    # Зчитуємо матрицю вагів та додаємо їх до графу
    for i in range(n):
        row = f.readline().split()
        for j in range(n):
            weight = int(row[j])
            if weight != 0:
                graph[i][j] = weight

# Ініціалізуємо мінімальну відстань як нескінченність
min_distance = float('infinity')

# Застосовуємо алгоритм Дейкстри для кожної точки графу
for i in range(n):
    distances = dijkstra(graph, i)
    # Знаходимо найкоротший шлях, що проходить через всі точки
total_distance = sum(distances.values())
if total_distance < min_distance:
    min_distance = total_distance
    path = [str(i) for i in range(n)]
print(f"Мінімальна відстань від точки {i}: {total_distance}")
print(f"Найкоротший шлях: {' -> '.join(path)}, відстань: {min_distance}")
