import collections

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
        counter, seen, stack = collections.Counter(s),set(),[]

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]]>0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
print(Solution.removeDuplicateLetters(Solution,s))