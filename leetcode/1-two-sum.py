## Problem Statement: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            len_nums = len(nums)
            for i in range(len_nums):
                for j in range(len_nums):
                    if nums[i] + nums[j] == target:
                        if i != j:
                            result = [i, j]
                            return result