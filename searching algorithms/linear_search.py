# Time complexity: O(n)
# Space complexity: O(1)

def linear_search(cards: list[int], query: int) -> int:
    for i in range(len(cards)):
        if cards[i] == query:
            return i

    return -1
