# Time Complexity: O(2ⁿ)
# Space Complexity: O(1)

def knapsack_recursion(profits, weights, capacity, idx=0):
    if idx == len(profits):
        return 0
    elif weights[idx] > capacity:
        return knapsack_recursion(profits, weights, capacity, idx + 1)
    else:
        return max(knapsack_recursion(profits, weights, capacity, idx + 1),
                   profits[idx] + knapsack_recursion(profits, weights, capacity - weights[idx], idx + 1))



