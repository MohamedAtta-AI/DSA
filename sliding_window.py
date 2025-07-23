# https://www.leetcode.com/problems/fruit-into-baskets
# https://www.hellointerview.com/learn/code/sliding-window/variable-length

# Naive solution
# Time Complexity: O(n^3)
# Space Complexity: O(1)
def fruit_into_baskets(fruits: list[int]) -> int:
    max_length = 0

    for i in range(len(fruits)):
        for j in range(i + 1, len(fruits)):
            if len(set(fruits[i: j + 1])) <= 2:
                max_length = max(max_length, j - i + 1)
            else:
                break

    return max_length


# Improvement #1
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def fruit_into_baskets(fruits: list[int]) -> int:
    max_length = 0

    for i in range(len(fruits)):
        state = {}
        for j in range(i, len(fruits)):
            state[fruits[j]] = state.get(fruits[j], 0) + 1
            if len(state) <= 2:
                max_length = max(max_length, j - i + 1)
            else:
                break

    return max_length

