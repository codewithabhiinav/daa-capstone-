import random
import time
import csv

from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra


random.seed(42)


def generate_parcels(size):
    parcels = []

    for i in range(size):
        parcels.append({
            "id": f"P{i + 1}",
            "weight": random.randint(1, 20),
            "value": random.randint(10, 100)
        })

    return parcels


def generate_graph(size):
    graph = {
        f"L{i}": {} for i in range(size)
    }

    # Connect locations in a chain so the graph is connected
    for i in range(size - 1):
        a = f"L{i}"
        b = f"L{i + 1}"
        weight = random.randint(1, 20)

        graph[a][b] = weight
        graph[b][a] = weight

    # Add extra random roads
    target_edges = size * 3

    while sum(len(neighbors) for neighbors in graph.values()) // 2 < target_edges:
        a, b = random.sample(list(graph.keys()), 2)

        if b not in graph[a]:
            weight = random.randint(1, 20)
            graph[a][b] = weight
            graph[b][a] = weight

    return graph


def main():

    results = []

    print("=" * 55)
    print("   KNAPSACK AND DIJKSTRA PERFORMANCE TEST")
    print("=" * 55)

    # KNAPSACK PERFORMANCE
    print("\n========== KNAPSACK PERFORMANCE ==========")

    parcel_sizes = [20, 50, 100, 200]
    capacity = 500

    for size in parcel_sizes:
        parcels = generate_parcels(size)

        start = time.perf_counter()
        selected, max_value, dp = knapsack(parcels, capacity)
        end = time.perf_counter()

        elapsed = end - start

        total_weight = sum(p["weight"] for p in selected)

        assert total_weight <= capacity

        print(f"\nNumber of Parcels: {size}")
        print(f"Vehicle Capacity: {capacity} kg")
        print(f"Execution Time: {elapsed:.6f} seconds")
        print("Capacity constraint passed: Yes")

        results.append({
            "Algorithm": "Knapsack",
            "Dataset Size": size,
            "Capacity": capacity,
            "Execution Time (seconds)": elapsed
        })

    # DIJKSTRA PERFORMANCE
    print("\n========== DIJKSTRA PERFORMANCE ==========")

    location_sizes = [50, 100, 200, 400]

    for size in location_sizes:
        graph = generate_graph(size)

        start = time.perf_counter()
        distances, previous = dijkstra(graph, "L0")
        end = time.perf_counter()

        elapsed = end - start

        assert len(distances) == size
        assert all(distance != float("inf") for distance in distances.values())

        print(f"\nNumber of Locations: {size}")
        print(f"Execution Time: {elapsed:.6f} seconds")
        print("All locations reachable: Yes")

        results.append({
            "Algorithm": "Dijkstra",
            "Dataset Size": size,
            "Capacity": "N/A",
            "Execution Time (seconds)": elapsed
        })

    # SAVE RESULTS
    with open(
        "results/other_algorithm_performance.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Algorithm",
                "Dataset Size",
                "Capacity",
                "Execution Time (seconds)"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nPerformance results saved successfully!")
    print("File: results/other_algorithm_performance.csv")


if __name__ == "__main__":
    main()
