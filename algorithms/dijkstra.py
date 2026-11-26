# Mini-Courier Planner
# Dijkstra's Shortest Path Algorithm

import heapq


def dijkstra(graph, start):

    # Initialize distances
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    # Min-heap priority queue
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        # Skip outdated entries
        if current_distance > distances[current_node]:
            continue

        # Visit neighboring locations
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            if distance < distances[neighbor]:

                distances[neighbor] = distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (distance, neighbor)
                )

    return distances, previous


# Reconstruct shortest path
def get_path(previous, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path
