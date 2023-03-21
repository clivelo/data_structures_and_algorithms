# Time Complexity: O(2ᵐ⁺ⁿ)
# Space Complexity: O(1)

def lcs_recursion(s1, s2):
    if not s1 or not s2:
        return 0
    if s1[0] == s2[0]:
        return 1 + lcs_recursion(s1[1:], s2[1:])
    return max(lcs_recursion(s1[1:], s2), lcs_recursion(s1, s2[1:]))
