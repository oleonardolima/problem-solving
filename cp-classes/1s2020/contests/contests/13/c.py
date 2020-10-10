import string
import collections

def s_word(x, memo, alphabet):
    if x not in memo:
        p_x = alphabet[alphabet.index(x) - 1]
        _s_word = s_word(p_x, memo, alphabet)
        word = _s_word + x + _s_word
        memo[x] = word
        return word
    return memo[x]

nth_position = int(input())
alphabet = string.ascii_lowercase

memo = collections.defaultdict(str)
memo['a'] = 'a'

#print(s_word('b', memo, alphabet))
#print(s_word('c', memo, alphabet))

z_word = s_word('z', memo, alphabet)
#print(z_word)
print(z_word[nth_position - 1])