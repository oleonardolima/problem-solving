## Problem Statement: https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        element_freq = {}
        for element in nums:
            if element not in element_freq:
                    element_freq[element] = 1
            else:
                    element_freq[element] += 1
        
        single_number = -1
        for element in element_freq:
            if element_freq[element] == 1:
                single_number = element
                break
        return single_number
