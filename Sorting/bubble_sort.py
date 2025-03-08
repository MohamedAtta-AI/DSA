# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def bubbleSort(self, nums: list[int]):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums