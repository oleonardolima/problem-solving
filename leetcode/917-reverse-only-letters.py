# Problem Statement: https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        #characters = [char for char in S]
        characters = list(S)
        ptr1 = 0
        ptr2 = len(characters) - 1
        while (ptr1 < ptr2):
            while (ptr1 < ptr2 and not(S[ptr1].isalpha())):
                ptr1 += 1
            while (ptr1 < ptr2 and not(S[ptr2].isalpha())):
                ptr2 -= 1

            characters[ptr1], characters[ptr2] = characters[ptr2], characters[ptr1]
            ptr1 += 1
            ptr2 -= 1

        return "".join(characters)