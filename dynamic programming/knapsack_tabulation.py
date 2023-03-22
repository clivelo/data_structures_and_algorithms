# Time Complexity: O(n * c)
# Space Complexity: O(n * c)

def knapsack_tabulation(profits, weights, capacity):
    table = [[0 for _ in range(capacity + 1)] for _ in range(len(profits) + 1)]

    for i in range(len(profits)):
        for j in range(1, capacity + 1):
            if weights[i] > j:
                table[i + 1][j] = table[i][j]
            else:
                table[i + 1][j] = max(profits[i] + table[i][j - weights[i]], table[i][j])

    return table[-1][-1]
