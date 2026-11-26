import csv
import matplotlib.pyplot as plt

sizes = []
merge_times = []
quick_times = []

with open("results/sorting_performance.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sizes.append(int(row["Dataset Size"]))
        merge_times.append(float(row["Merge Sort (seconds)"]))
        quick_times.append(float(row["Quick Sort (seconds)"]))

plt.figure(figsize=(9, 5))

plt.plot(sizes, merge_times, marker="o", label="Merge Sort")
plt.plot(sizes, quick_times, marker="s", label="Quick Sort")

plt.xlabel("Number of Parcels")
plt.ylabel("Execution Time (seconds)")
plt.title("Merge Sort vs Quick Sort Performance")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("results/sorting_comparison.png", dpi=300)

plt.show()

print("Performance chart saved successfully!")
print("File: results/sorting_comparison.png")
