import csv
import matplotlib.pyplot as plt

knapsack_sizes = []
knapsack_times = []

dijkstra_sizes = []
dijkstra_times = []

with open("results/other_algorithm_performance.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        size = int(row["Dataset Size"])
        elapsed = float(row["Execution Time (seconds)"])

        if row["Algorithm"] == "Knapsack":
            knapsack_sizes.append(size)
            knapsack_times.append(elapsed)

        elif row["Algorithm"] == "Dijkstra":
            dijkstra_sizes.append(size)
            dijkstra_times.append(elapsed)

# Knapsack graph
plt.figure(figsize=(8, 5))
plt.plot(knapsack_sizes, knapsack_times, marker="o")
plt.xlabel("Number of Parcels")
plt.ylabel("Execution Time (seconds)")
plt.title("Knapsack Performance Analysis")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/knapsack_performance.png", dpi=300)
plt.show()

# Dijkstra graph
plt.figure(figsize=(8, 5))
plt.plot(dijkstra_sizes, dijkstra_times, marker="o")
plt.xlabel("Number of Locations")
plt.ylabel("Execution Time (seconds)")
plt.title("Dijkstra Performance Analysis")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/dijkstra_performance.png", dpi=300)
plt.show()

print("Both performance graphs saved successfully!")
