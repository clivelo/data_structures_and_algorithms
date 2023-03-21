# Time Complexity: O(n²)
# Space Complexity: O(1)

def bubble_sort(nums):
    nums = nums.copy()

    for _ in range(len(nums) - 1):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

    return nums
