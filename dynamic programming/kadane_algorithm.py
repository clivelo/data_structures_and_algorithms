# Time complexity: O(n)
# Space complexity: O(1)

def kadane(nums):
    if len(nums) == 0:
        return 0

    max_current = max_global = nums[0]
    for i in range(1, len(nums)):
        max_current = max(nums[i], max_current + nums[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
