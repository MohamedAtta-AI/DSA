# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[left] == nums[right]:
                continue
            left += 1
            nums[left] = nums[right]
        return left + 1