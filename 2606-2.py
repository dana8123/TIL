def virus(graph, start_node, visited_node):
    visited_node.append(start_node)  # visited node [1, 5, 2, 4, 3, 6]

    for node in graph[start_node]:  # 1: [1 5] 5:[2 4] 4:[3 1] 3:[3 2] 2:[1 1]
        if node not in visited_node:
            virus(graph, node, visited_node)


graph = dict()
visited_node = []

case = int(input())
pair = int(input())

for _ in range(pair):
    x, y = map(int, input().split())

    if x in graph:
        graph[x].append(y)
    else:
        graph[x] = [y]
    if y in graph:
        graph[y].append(x)
    else:
        graph[y] = [x]

virus(graph, 1, visited_node)

print(len(visited_node)-1)
