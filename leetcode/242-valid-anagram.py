# Problem Statement: https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            letter_cnt = {}
            for letter in s:
                if not letter in letter_cnt:
                    letter_cnt[letter] = 1
                else:
                    letter_cnt[letter] = letter_cnt[letter] + 1
            for letter in t:
                if not letter in letter_cnt:
                    letter_cnt[letter] = 1
                else:
                    letter_cnt[letter] = letter_cnt[letter] - 1
            for letter in letter_cnt:
                if letter_cnt[letter] > 0:
                    return False
            return True
