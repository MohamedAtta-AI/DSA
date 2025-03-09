# https://leetcode.com/problems/trapping-rain-water/description/
# https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def trappingWater(self, heights: list[int]):
        if not heights:
            return 0
            
        left, right = 0, len(heights) - 1
        leftMax, rightMax = heights[left], heights[right]
        count = 0

        while left + 1 < right:
            if rightMax > leftMax:
                left += 1
                if heights[left] > leftMax:
                    leftMax = heights[left]
                else:
                    count += leftMax - heights[left]
            else:
                right -= 1
                if heights[right] > rightMax:
                    rightMax = heights[right]
                else:
                    count += rightMax - heights[right]

        return count