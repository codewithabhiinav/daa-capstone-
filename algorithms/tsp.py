def nearest_neighbor_tsp(distance_matrix, start, destinations):
    unvisited = set(destinations)
    unvisited.discard(start)

    current = start
    route = [start]
    total_distance = 0

    while unvisited:
        next_location = min(
            unvisited,
            key=lambda location: distance_matrix[current][location]
        )

        total_distance += distance_matrix[current][next_location]
        current = next_location
        route.append(current)
        unvisited.remove(current)

    # Return to warehouse
    if current != start:
        total_distance += distance_matrix[current][start]
        route.append(start)

    return route, total_distance
