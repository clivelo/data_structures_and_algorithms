# Time complexity: O(n log₂ n)
# Space complexity: O(1)

def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = nums.copy()
        end = len(nums) - 1

    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums, start, pivot - 1)
        quick_sort(nums, pivot + 1, end)

    return nums


def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1

    l, r = start, end - 1

    while l < r:
        if nums[l] <= nums[end]:
            l += 1
        elif nums[r] > nums[end]:
            r -= 1
        else:
            nums[l], nums[r] = nums[r], nums[l]

    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
