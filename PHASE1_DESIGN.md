# PHASE 1: COURIER PROBLEM DESIGN AND PLANNING

## 1. Project Title
**Mini-Courier Planner – An Algorithm-Based Delivery Planning System**

## 2. Problem Statement

The Mini-Courier Planner is a Python-based application designed to simulate an intelligent courier delivery planning system.

In courier services, selecting parcels, managing vehicle capacity, and finding efficient delivery routes are important tasks. Delivering parcels without proper planning can increase transportation distance and delivery time.

This project integrates sorting algorithms, Dynamic Programming, graph algorithms, and approximation techniques to develop an efficient courier planning solution.

The system prioritizes parcels according to their delivery deadlines and priority, selects an optimal combination of parcels based on vehicle capacity, calculates shortest paths between delivery locations, and generates an approximate delivery route.

## 3. Objectives

The main objectives of this project are:

1. To prioritize parcels based on delivery deadlines and priority.
2. To implement Merge Sort and Quick Sort for parcel sorting.
3. To apply the 0/1 Knapsack Dynamic Programming algorithm for optimal parcel selection.
4. To represent delivery locations using a weighted graph.
5. To implement Dijkstra's Algorithm for finding shortest paths.
6. To apply the Nearest Neighbor TSP approximation for delivery route planning.
7. To measure and compare the execution time of different algorithms.

## 4. Parcel Data Design

Each parcel is represented using the following attributes:

| Attribute | Description | Example |
|---|---|---|
| Parcel ID | Unique parcel identification | P101 |
| Destination | Delivery location | A |
| Weight | Parcel weight in kg | 5 |
| Priority | Delivery priority score | 8 |
| Deadline | Expected delivery deadline | 12:00 |
| Value | Parcel importance/value | 100 |

The parcel information will be stored using Python dictionaries and a list of dictionaries.

## 5. Delivery Point Design

The delivery network consists of a central warehouse and multiple customer locations.

The following locations will be used:

- W – Central Warehouse
- A – Customer Location A
- B – Customer Location B
- C – Customer Location C
- D – Customer Location D

Each location represents a vertex in the delivery graph.

## 6. Graph Representation

The delivery network will be represented using a weighted adjacency list.

Each vertex represents a delivery location, and each edge represents the distance between two locations in kilometres.

Example:

```python
graph = {
    "W": {"A": 10, "B": 15, "C": 20},
    "A": {"W": 10, "B": 5, "C": 12},
    "B": {"W": 15, "A": 5, "C": 8},
    "C": {"W": 20, "A": 12, "B": 8}
}
```

The graph represents an undirected weighted network, where the distance between two connected locations is the same in both directions.

## 7. Algorithm Selection

The following algorithms will be implemented in the project:

### 7.1 Merge Sort
Merge Sort will be used as the primary parcel sorting algorithm.

It will arrange parcels according to:
- Earlier delivery deadlines first.
- Higher priority first when deadlines are equal.

Time Complexity: O(n log n)

Space Complexity: O(n)

### 7.2 Quick Sort
Quick Sort will also be implemented to sort parcels using the same sorting conditions.

It will be used for comparing the performance of two sorting algorithms.

Average Time Complexity: O(n log n)

Worst-case Time Complexity: O(n²)

### 7.3 0/1 Knapsack Dynamic Programming
The Knapsack algorithm will select the most valuable combination of parcels without exceeding the vehicle's maximum weight capacity.

Each parcel can either be selected completely or rejected.

Time Complexity: O(nW)

Space Complexity: O(nW)

### 7.4 Dijkstra's Algorithm
Dijkstra's Algorithm will calculate the shortest paths and distances from the warehouse to the delivery locations.

A priority queue (min-heap) will be used for efficient processing.

Time Complexity: O((V + E) log V)

Space Complexity: O(V + E)

### 7.5 Nearest Neighbor TSP Approximation
The Nearest Neighbor algorithm will generate an approximate delivery route.

It will start from the warehouse, visit the nearest unvisited delivery location, continue until all selected locations are visited, and finally return to the warehouse.

Time Complexity: O(V²)

Space Complexity: O(V)

## 8. Integrated System Workflow

The system will work in the following sequence:

1. Accept parcel information and delivery locations.
2. Sort parcels using Merge Sort or Quick Sort.
3. Apply 0/1 Knapsack DP to select parcels within vehicle capacity.
4. Identify the delivery locations of the selected parcels.
5. Create the weighted delivery graph.
6. Apply Dijkstra's Algorithm to calculate shortest paths between locations.
7. Apply Nearest Neighbor TSP to generate the delivery sequence.
8. Calculate the total delivery distance.
9. Measure the execution time of the major algorithms.
10. Display the final packing plan and delivery route.

## 9. Route-Planning Logic

The warehouse is considered the starting and ending point of the delivery journey.

The system will first select parcels according to their priority and vehicle capacity. After parcel selection, the destinations of the selected parcels will be considered for route planning.

Dijkstra's Algorithm will calculate shortest-path distances between delivery locations. These distances will be used as travel costs by the Nearest Neighbor TSP algorithm.

The TSP approximation will select the nearest unvisited location at each step until all required delivery locations are covered.

Finally, the system will return to the warehouse and calculate the total route distance.

## 10. Suitability of Selected Algorithms

The selected algorithms are suitable for this project for the following reasons:

- Merge Sort provides reliable O(n log n) sorting performance and maintains the relative order of equal sorting keys.
- Quick Sort provides an additional sorting technique for performance comparison.
- 0/1 Knapsack DP finds the maximum-value parcel combination within a fixed vehicle capacity.
- Dijkstra's Algorithm finds shortest paths in a graph with non-negative edge weights.
- Nearest Neighbor TSP provides a practical approximate route without checking every possible delivery order.

Together, these algorithms provide an integrated solution for parcel prioritization, packing optimization, and delivery route planning.

## 11. Conclusion

In Phase 1, the Mini-Courier Planner problem has been defined and its system design has been prepared. The parcel attributes, delivery locations, graph representation, and algorithm selection have been identified.

The proposed system integrates sorting, Dynamic Programming, shortest-path calculation, and approximate route planning to simulate an intelligent courier delivery system.

The next phases will focus on implementing, testing, and evaluating the selected algorithms using Python.
