# https://www.hellointerview.com/learn/code/two-pointers/container-with-most-water
# https://leetcode.com/problems/container-with-most-water/description/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def max_area(self, heights):
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height

            max_area = max(max_area, current_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area