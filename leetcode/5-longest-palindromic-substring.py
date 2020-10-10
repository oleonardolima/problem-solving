## Problem Statement: https://leetcode.com/problems/longest-palindromic-substring/

import math
class Solution:
    def expand_from_center(self, string_s, left_ptr, right_ptr):
        if (not string_s or left_ptr > right_ptr):
            return 0

        while (left_ptr >= 0 and right_ptr < len(string_s) and string_s[left_ptr] == string_s[right_ptr]):
            left_ptr -= 1
            right_ptr += 1

        return right_ptr - left_ptr - 1

    def longestPalindrome(self, s: str) -> str:
        contiguous_substring = s
        start_ptr = 0
        end_ptr = 0

        for i in range(len(contiguous_substring)):
            len_1 = self.expand_from_center(contiguous_substring, i, i)
            len_2 = self.expand_from_center(contiguous_substring, i, i + 1)
            max_len = max(len_1, len_2)

            if max_len > (end_ptr - start_ptr):
                start_ptr = i - (max_len - 1) // 2
                end_ptr = i + (max_len // 2)

        return contiguous_substring[start_ptr:end_ptr + 1]
