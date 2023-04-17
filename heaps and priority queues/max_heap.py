# Push -
# Time complexity: O(log n)
#
# Pop -
# Time complexity: O(log n)

import heapq


def main():
    data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
    heapq.heappush(data, 5)
    data = [-x for x in data]
    heapq.heapify(data)
    print(data)

    while data:
        print(-heapq.heappop(data))


if __name__ == "__main__":
    main()
