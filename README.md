# Mini-Courier Planner

A Python-based courier planning system developed for the Design and Analysis of Algorithms (DAA) assignment.

## Project Overview

The Mini-Courier Planner organizes parcel deliveries by deadline and priority, selects parcels according to vehicle capacity, and calculates delivery routes using graph algorithms.

## Algorithms Implemented

1. **Merge Sort:** Sorts parcels by deadline and priority.
2. **Quick Sort:** Provides an alternative sorting implementation for performance comparison.
3. **0/1 Knapsack (Dynamic Programming):** Selects parcels to maximize total value without exceeding vehicle capacity.
4. **Dijkstra's Algorithm:** Calculates shortest paths between delivery locations.
5. **Nearest Neighbor TSP:** Generates an approximate delivery route.

## Project Structure

```text
Mini-Courier-Planner/
├── algorithms/
│   ├── __init__.py
│   ├── sorting.py
│   ├── knapsack.py
│   ├── dijkstra.py
│   └── tsp.py
├── data/
│   └── locations.json
├── tests/
│   ├── __init__.py
│   ├── test_algorithms.py
│   ├── test_performance.py
│   ├── test_dp_graph_performance.py
│   └── plot_performance.py
├── results/
├── screenshots/
├── main.py
├── config.py
├── requirements.txt
├── PHASE1_DESIGN.md
├── PHASE4_PERFORMANCE_ANALYSIS.md
└── README.md
```

## Requirements

- Python 3.10 or later
- Matplotlib

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd Mini-Courier-Planner
```

Create and activate a virtual environment:

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the Project

```powershell
python main.py
```

## Run Algorithm Tests

```powershell
python -m tests.test_algorithms
```

## Run Performance Tests

```powershell
python -m tests.test_performance
python -m tests.test_dp_graph_performance
```

## Generate Performance Graphs

```powershell
python -m tests.plot_performance
python -m tests.plot_other_performance
```

## Sample Output

The integrated program demonstrates:

- Parcels sorted by deadline and priority.
- Selected parcels within the 20 kg vehicle capacity.
- Total selected parcel value of 37.
- Shortest distances from warehouse W.
- Approximate delivery route: W → A → B → C → W.
- Total route distance: 43 km.

## Performance Analysis

Performance was evaluated using different dataset sizes. Execution times were recorded in CSV files and visualized using Matplotlib.

Refer to `PHASE4_PERFORMANCE_ANALYSIS.md` for experimental results and complexity analysis.

## Conclusion

This project demonstrates the practical application of sorting, dynamic programming, shortest-path algorithms, and approximation algorithms in a courier delivery planning problem.