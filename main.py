import json

from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra
from algorithms.tsp import nearest_neighbor_tsp


# Sample parcel data
parcels = [
    {
        "id": "P101",
        "destination": "A",
        "weight": 5,
        "value": 10,
        "deadline": "14:00",
        "priority": 5
    },
    {
        "id": "P102",
        "destination": "B",
        "weight": 8,
        "value": 15,
        "deadline": "10:00",
        "priority": 9
    },
    {
        "id": "P103",
        "destination": "C",
        "weight": 6,
        "value": 12,
        "deadline": "12:00",
        "priority": 8
    },
    {
        "id": "P104",
        "destination": "D",
        "weight": 4,
        "value": 8,
        "deadline": "10:00",
        "priority": 7
    }
]

VEHICLE_CAPACITY = 20
WAREHOUSE = "W"


def main():

    print("=" * 50)
    print("       MINI COURIER PLANNER")
    print("=" * 50)

    # 1. Sort parcels
    print("\n1. PARCEL SORTING")

    sorted_parcels = merge_sort(parcels)

    for parcel in sorted_parcels:
        print(
            parcel["id"],
            "| Deadline:", parcel["deadline"],
            "| Priority:", parcel["priority"]
        )

    # 2. Select parcels using Knapsack
    print("\n2. VEHICLE PACKING (KNAPSACK)")

    selected, max_value, dp = knapsack(
        sorted_parcels, VEHICLE_CAPACITY
    )

    total_weight = sum(p["weight"] for p in selected)

    print("Vehicle Capacity:", VEHICLE_CAPACITY, "kg")
    print("Selected Parcels:")

    for parcel in selected:
        print(
            parcel["id"],
            "| Destination:", parcel["destination"],
            "| Weight:", parcel["weight"], "kg",
            "| Value:", parcel["value"]
        )

    print("Total Weight:", total_weight, "kg")
    print("Total Value:", max_value)
    print("Remaining Capacity:", VEHICLE_CAPACITY - total_weight, "kg")

    # 3. Load delivery graph
    print("\n3. DIJKSTRA SHORTEST PATH")

    with open("data/locations.json", "r") as file:
        graph = json.load(file)

    distances, previous = dijkstra(graph, WAREHOUSE)

    for location in graph:
        print(
            WAREHOUSE, "->", location,
            ":", distances[location], "km"
        )

    # 4. Build all-pairs shortest distance matrix
    distance_matrix = {}

    for source in graph:
        source_distances, _ = dijkstra(graph, source)
        distance_matrix[source] = source_distances

    # 5. Generate delivery route using TSP
    print("\n4. DELIVERY ROUTE (NEAREST NEIGHBOUR TSP)")

    destinations = list(
        dict.fromkeys(p["destination"] for p in selected)
    )

    route, total_distance = nearest_neighbor_tsp(
        distance_matrix,
        WAREHOUSE,
        destinations
    )

    print("Delivery Route:", " -> ".join(route))
    print("Total Route Distance:", total_distance, "km")

    print("\n" + "=" * 50)
    print("       COURIER PLAN GENERATED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()
