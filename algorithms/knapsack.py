# Mini-Courier Planner
# 0/1 Knapsack using Dynamic Programming


def knapsack(parcels, capacity):

    n = len(parcels)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        weight = parcels[i - 1]["weight"]
        value = parcels[i - 1]["value"]

        for w in range(capacity + 1):

            if weight <= w:

                include = value + dp[i - 1][w - weight]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    # Find selected parcels using backtracking
    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            parcel = parcels[i - 1]
            selected.append(parcel)

            w -= parcel["weight"]

    selected.reverse()

    return selected, dp[n][capacity], dp
