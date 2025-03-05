# https://www.hellointerview.com/learn/code/two-pointers/move-zeroes
# https://leetcode.com/problems/move-zeroes/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def moveZeroes(self, nums: list[int]):
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums