# Time Complexity: O(n * c)
# Space Complexity: O(n * c)

def knapsack_memoization(profits, weights, capacity):
    memo = {}

    def recurse(capacity, idx=0):
        key = (capacity, idx)
        if key in memo:
            return memo[key]
        elif idx == len(profits):
            memo[key] = 0
        elif weights[idx] > capacity:
            memo[key] = recurse(capacity, idx + 1)
        else:
            memo[key] = max(recurse(capacity, idx + 1),
                            profits[idx] + recurse(capacity - weights[idx], idx + 1))
        return memo[key]

    return recurse(capacity, 0)
