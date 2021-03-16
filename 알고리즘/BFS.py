graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    visited_node = []
    queue = [start_node]
    while queue:
        current_node = queue.pop()
        visited_node.append(current_node)
        for near_node in graph[current_node]:
            if near_node not in queue:
                queue.append(near_node)

    return visited_node


print(bfs_queue(graph, 1))
