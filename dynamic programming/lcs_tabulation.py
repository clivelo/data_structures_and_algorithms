# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

def lcs_tabulation(s1, s2):
    table = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
    return table[-1][-1]
