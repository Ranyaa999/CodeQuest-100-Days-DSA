from collections import deque


graph = {}

n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors


def bfs(start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        if current not in visited:
            print(current, end=' ')
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)


start_node = input("Enter starting node: ")
bfs(start_node)
