# Phase 4: Performance Analysis and Testing

## 1. Introduction

In this phase, the performance of the Mini-Courier Planner algorithms was evaluated using different dataset sizes. The objective was to measure execution time, verify correctness, and understand how algorithm performance changes as the input size increases.

## 2. Sorting Algorithm Performance

Merge Sort and Quick Sort were tested using 100, 500, 1000, and 2000 parcels.

| Dataset Size | Merge Sort (seconds) | Quick Sort (seconds) |
|---:|---:|---:|
| 100 | 0.000347 | 0.000192 |
| 500 | 0.003618 | 0.001834 |
| 1000 | 0.004771 | 0.004707 |
| 2000 | 0.015599 | 0.008890 |

**Observation:** Quick Sort was faster in these particular test runs. Both algorithms successfully sorted the parcels according to their deadlines and priorities.

## 3. Knapsack Algorithm Performance

The 0/1 Knapsack algorithm was tested with different numbers of parcels while keeping vehicle capacity fixed at 500 kg.

| Number of Parcels | Capacity (kg) | Execution Time (seconds) |
|---:|---:|---:|
| 20 | 500 | 0.002641 |
| 50 | 500 | 0.008052 |
| 100 | 500 | 0.013946 |
| 200 | 500 | 0.031251 |

**Observation:** Execution time increased as the number of parcels increased. The capacity constraint was satisfied in every test.

## 4. Dijkstra Algorithm Performance

Dijkstra's algorithm was tested on connected graphs containing different numbers of locations.

| Number of Locations | Execution Time (seconds) |
|---:|---:|
| 50 | 0.000230 |
| 100 | 0.000253 |
| 200 | 0.000793 |
| 400 | 0.001750 |

**Observation:** Execution time increased as the number of locations increased. All generated locations were reachable from the starting location.

## 5. Performance Graphs

The following graphs were generated from the experimental results:

- `results/sorting_comparison.png`
- `results/knapsack_performance.png`
- `results/dijkstra_performance.png`

These graphs visually compare the execution time of the algorithms for different input sizes.

## 6. Time Complexity Analysis

| Algorithm | Time Complexity |
|---|---|
| Merge Sort | O(n log n) |
| Quick Sort | Average: O(n log n), Worst: O(n²) |
| 0/1 Knapsack DP | O(nW) |
| Dijkstra with Priority Queue | O((V + E) log V) |
| Nearest Neighbor TSP | O(k²) |

Here, n represents the number of parcels, W represents vehicle capacity, V represents vertices, E represents edges, and k represents delivery locations.

## 7. Optimization Suggestions

1. Use a priority queue in Dijkstra's algorithm to efficiently find the next closest location.
2. Store previously calculated shortest paths to avoid repeated calculations when the graph remains unchanged.
3. Use efficient sorting algorithms to process large parcel datasets.
4. Optimize the Knapsack DP table using a one-dimensional array when memory usage becomes important.
5. Use efficient graph representations such as adjacency lists for sparse graphs.

## 8. Conclusion

The performance testing demonstrated that the implemented algorithms successfully handle different input sizes. Merge Sort and Quick Sort efficiently organize parcels, Knapsack DP selects parcels within vehicle capacity, and Dijkstra calculates shortest paths in the delivery network.

The experimental results show how execution time changes with dataset size and provide a foundation for improving the Mini-Courier Planner in future versions.