import heapq

def astar(graph, heuristics, start_node, end_node):
    open_set = []
    closed_set = set()
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start_node] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start_node] = g_score[start_node] + heuristics[start_node]

    heapq.heappush(open_set, (f_score[start_node], start_node))

    while open_set:
        current_node = heapq.heappop(open_set)[1]

        if current_node == end_node:
            return reconstruct_path(came_from, end_node)

        closed_set.add(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current_node] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristics[neighbor]

                if neighbor not in open_set:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path

# Example usage:
# Replace 'graph' and 'heuristics' with your data, and 'start_node' and 'end_node' with user input
# path = astar(graph, heuristics, start_node, end_node)
# if path:
#     print("A* minimum cost path")
#     print(path)
# else:
#     print("No path found")
