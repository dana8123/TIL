case = int(input())
pair = int(input())
graph = {}
for i in range(1, pair + 1):
    key = int(i)
    val = input().split()
    graph[key] = val
# dict 나열하는 방법을 이해한대로 다시 재작성 필요


def virus(graph, start_node):
    visited_node = []
    stack = [start_node]
    count = 0
    while stack:
        current_node = stack.pop()
        visited_node.append(current_node)
        for near_node in graph[current_node]:
            if near_node not in visited_node:
                stack.append(near_node)
                count += 1
    return visited_node


virus(graph, 1)
print(count)
