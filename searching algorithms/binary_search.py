# Time complexity: O(log₂ n)
# Space complexity: O(1)

def binary_search(cards: list[int], query: int) -> int:
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2

        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            high = mid - 1
        elif cards[mid] > query:
            low = mid + 1

    return -1
