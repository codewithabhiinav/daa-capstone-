import random
import time
import csv

from algorithms.sorting import merge_sort, quick_sort


def generate_parcels(size):
    parcels = []

    for i in range(size):
        minutes = random.randint(0, 1439)

        hours = minutes // 60
        mins = minutes % 60

        deadline = f"{hours:02d}:{mins:02d}"

        parcels.append({
            "id": f"P{i + 1}",
            "deadline": deadline,
            "priority": random.randint(1, 10)
        })

    return parcels


def measure_time(function, data):
    start = time.perf_counter()
    result = function(data)
    end = time.perf_counter()

    return result, end - start


def main():

    dataset_sizes = [100, 500, 1000, 2000]

    results = []

    print("=" * 55)
    print("       SORTING ALGORITHM PERFORMANCE TEST")
    print("=" * 55)

    for size in dataset_sizes:

        parcels = generate_parcels(size)

        merge_result, merge_time = measure_time(
            merge_sort, parcels.copy()
        )

        quick_result, quick_time = measure_time(
            quick_sort, parcels.copy()
        )

        # Compare sorting keys, not parcel order for equal keys
        merge_keys = [
            (p["deadline"], -p["priority"])
            for p in merge_result
        ]

        quick_keys = [
            (p["deadline"], -p["priority"])
            for p in quick_result
        ]

        assert merge_keys == quick_keys

        results.append({
            "Dataset Size": size,
            "Merge Sort (seconds)": merge_time,
            "Quick Sort (seconds)": quick_time
        })

        print(f"\nDataset Size: {size}")
        print(f"Merge Sort Time: {merge_time:.6f} seconds")
        print(f"Quick Sort Time: {quick_time:.6f} seconds")
        print("Both results match: Yes")

    # Save results to CSV
    with open("results/sorting_performance.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Dataset Size",
                "Merge Sort (seconds)",
                "Quick Sort (seconds)"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nPerformance results saved successfully!")
    print("File: results/sorting_performance.csv")


if __name__ == "__main__":
    main()
