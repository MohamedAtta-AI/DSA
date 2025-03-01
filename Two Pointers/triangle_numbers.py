# https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number
# https://leetcode.com/problems/valid-triangle-number/description/
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count