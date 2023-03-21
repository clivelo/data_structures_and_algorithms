# Time Complexity: O(n²)
# Space Complexity: O(1)

def insertion_sort(nums):
    nums = nums.copy()

    for i in range(len(nums)):
        curr = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > curr:
            j -= 1
        nums.insert(j + 1, curr)

    return nums
