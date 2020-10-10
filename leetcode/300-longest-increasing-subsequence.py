# Problem Statement: https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = nums
        if not arr:
            return 0
        lens = [1 for num in arr]
        seqs = [None for num in arr]

        for i, num in enumerate(arr):
            curr_num = num
            for j in range(0, i):
                other_num = arr[j]
                if other_num < curr_num and lens[j] + 1 >= lens[i]:
                    lens[i] = lens[j] + 1
                    seqs[i] = j

        return max(lens)
