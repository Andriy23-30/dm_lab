import numpy as np

# зчитуємо дані з файлу
with open("data.txt", "r") as file:
    n = int(file.readline())
    distances = np.zeros((n, n))
    for i in range(n):
        row = list(map(int, file.readline().split()))
        for j in range(n):
            distances[i, j] = row[j]

# алгоритм найближчого сусіда
visited = [0]
while len(visited) < n:
    current_city = visited[-1]
    nearest_city = None
    nearest_distance = float('inf')
    for i in range(n):
        if i not in visited and distances[current_city, i] < nearest_distance:
            nearest_city = i
            nearest_distance = distances[current_city, i]
    visited.append(nearest_city)

# обчислюємо довжину маршруту
total_distance = 0
for i in range(n-1):
    total_distance += distances[visited[i], visited[i+1]]
total_distance += distances[visited[-1], visited[0]]

# виводимо результат
print("Маршрут: ", end="")
for city in visited:
    print(city, end=" ")
    print()
print("Довжина маршруту:", total_distance)