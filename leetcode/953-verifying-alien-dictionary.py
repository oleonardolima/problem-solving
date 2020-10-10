# Problem Statement: https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letter_idx = {}
        for idx, letter in enumerate(order):
            letter_idx[letter] = idx

        ptr1 = 0
        ptr2 = 1

        while ptr2 <= len(words) - 1:
            word1 = words[ptr1]
            word2 = words[ptr2]

            i, j = 0, 0
            len1 = len(word1)
            len2 = len(word2)
            min_len = min(len1, len2)

            if len1 > len2 and word1[:len2] == word2:
                return False

            while i < min_len:
                if letter_idx[word1[i]] < letter_idx[word2[i]]:
                    break
                elif letter_idx[word1[i]] > letter_idx[word2[i]]:
                    return False
                i += 1

            ptr1 += 1
            ptr2 += 1

        return True