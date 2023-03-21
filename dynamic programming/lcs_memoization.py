# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

def lcs_memoization(s1, s2):
    memo = {}

    def recurse(idx1=0, idx2=0):
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(s1) or idx2 == len(s2):
            memo[key] = 0
        elif s1[idx1] == s2[idx2]:
            memo[key] = 1 + recurse(idx1 + 1, idx2 + 1)
        else:
            memo[key] = max(recurse(idx1 + 1, idx2), recurse(idx1, idx2 + 1))
        return memo[key]

    return recurse(0, 0)

