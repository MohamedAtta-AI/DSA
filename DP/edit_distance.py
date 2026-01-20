# https://leetcode.com/problems/edit-distance/

# DP Solution
# Time Complexity: O(n*m)
# Time Complexity: O(n*m)
def levenshtein_distance(s1: str, s2: str) -> int:
    # Init DP table
    cache = [[float("inf")] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    
    # Init base case (last row and column)
    for j in range(len(s2) + 1):
        cache[len(s1)][j] = len(s2) - j

    for i in range(len(s1) + 1):
        cache[i][len(s2)] = len(s1) - i

    # Bottom-up
    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2), -1, -1, -1):

            if s1[i] == s2[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

    return cache[0][0]