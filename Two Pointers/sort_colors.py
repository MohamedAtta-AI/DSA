# https://www.hellointerview.com/learn/code/two-pointers/sort-colors
# https://leetcode.com/problems/sort-colors/description/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def sortColors(self, nums: list[int]):
        # Dutch National Flag Algorithm
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1
        return nums