## Problem Statement: https://leetcode.com/problems/valid-palindrome/

import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric_chars = string.ascii_lowercase + string.digits
        s = s.lower()
        left_ptr = 0
        right_ptr = len(s) - 1
        
        while left_ptr < right_ptr:
            if s[left_ptr] in alphanumeric_chars and s[right_ptr] in alphanumeric_chars:
                if s[left_ptr].lower() == s[right_ptr].lower():
                    left_ptr += 1
                    right_ptr -= 1
                    continue
                else:
                    return False
            elif s[left_ptr] not in alphanumeric_chars:
                left_ptr += 1
            elif s[right_ptr] not in alphanumeric_chars:
                right_ptr -= 1
            else:
                return False
        return True