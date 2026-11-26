# Mini-Courier Planner
# Sorting Algorithms: Merge Sort and Quick Sort


# Function to sort parcels using Merge Sort
def merge_sort(parcels):
    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort(parcels[:mid])
    right = merge_sort(parcels[mid:])

    return merge(left, right)


# Merge two sorted lists
def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        key_left = (left[i]["deadline"], -left[i]["priority"])
        key_right = (right[j]["deadline"], -right[j]["priority"])

        if key_left <= key_right:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Function to sort parcels using Quick Sort
def quick_sort(parcels):
    arr = parcels.copy()

    def partition(low, high):
        pivot = (
            arr[high]["deadline"],
            -arr[high]["priority"]
        )

        i = low - 1

        for j in range(low, high):

            current = (
                arr[j]["deadline"],
                -arr[j]["priority"]
            )

            if current <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def sort(low, high):
        if low < high:
            pi = partition(low, high)

            sort(low, pi - 1)
            sort(pi + 1, high)

    sort(0, len(arr) - 1)

    return arr
