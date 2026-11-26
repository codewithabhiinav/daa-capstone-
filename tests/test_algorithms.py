from algorithms.sorting import merge_sort, quick_sort

parcels = [
    {"id": "P101", "deadline": "14:00", "priority": 5},
    {"id": "P102", "deadline": "10:00", "priority": 9},
    {"id": "P103", "deadline": "12:00", "priority": 8},
    {"id": "P104", "deadline": "10:00", "priority": 7}
]

print("========== MERGE SORT ==========")

merge_result = merge_sort(parcels)

for p in merge_result:
    print(p)

print("\n========== QUICK SORT ==========")

quick_result = quick_sort(parcels)

for p in quick_result:
    print(p)

# Verify both algorithms
assert merge_result == quick_result

print("\nBoth sorting algorithms passed!")

from algorithms.knapsack import knapsack

print("\n========== KNAPSACK DP ==========")

parcels = [
    {"id": "P101", "weight": 5, "value": 10},
    {"id": "P102", "weight": 8, "value": 15},
    {"id": "P103", "weight": 6, "value": 12},
    {"id": "P104", "weight": 4, "value": 8}
]

capacity = 20

selected, max_value, dp_table = knapsack(parcels, capacity)

print("Vehicle Capacity:", capacity, "kg")

print("\nSelected Parcels:")

total_weight = 0

for parcel in selected:
    print(parcel["id"],
          "- Weight:", parcel["weight"],
          "- Value:", parcel["value"])

    total_weight += parcel["weight"]

print("\nTotal Weight:", total_weight, "kg")
print("Total Value:", max_value)
print("Remaining Capacity:", capacity - total_weight, "kg")

print("\nDP Table:")

for row in dp_table:
    print(row)

assert total_weight <= capacity
assert max_value == 37
assert {p["id"] for p in selected} == {"P101", "P102", "P103"}

print("\nKnapsack test passed!")



from algorithms.tsp import nearest_neighbor_tsp

print("\n========== NEAREST NEIGHBOR TSP ==========")

# Shortest distance matrix using the given graph
distance_matrix = {
    "W": {"W": 0, "A": 10, "B": 15, "C": 20, "D": 25},
    "A": {"W": 10, "A": 0, "B": 5, "C": 12, "D": 15},
    "B": {"W": 15, "A": 5, "B": 0, "C": 8, "D": 10},
    "C": {"W": 20, "A": 12, "B": 8, "C": 0, "D": 6},
    "D": {"W": 25, "A": 15, "B": 10, "C": 6, "D": 0}
}

destinations = ["A", "B", "C", "D"]

route, total_distance = nearest_neighbor_tsp(
    distance_matrix, "W", destinations
)

print("Delivery Route:", " -> ".join(route))
print("Total Route Distance:", total_distance, "km")

assert route == ["W", "A", "B", "C", "D", "W"]
assert total_distance == 54

print("\nTSP test passed!")
