s = "cbacdcbc"
s ="abbbbbacccccb"

s = "cbacdcbc"
s = "cdadabcc"

s = "ecbacba"
s = "acacb"

s = "cbacdcbc"


s = "cbacdcbc"
s = "bcabc"

s = "cdadabcc"
#bacd
#acdb
class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix_letters = s[s.index(char):]
            if set(s) == set(suffix_letters):
                return char+Solution.removeDuplicateLetters(Solution,suffix_letters.replace(char,''))

        return ''

print(Solution.removeDuplicateLetters(Solution,s))