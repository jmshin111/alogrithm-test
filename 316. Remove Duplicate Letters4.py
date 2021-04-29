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
        result = ''

        stack = []
        exist_key = {}
        queue = []
        counter = {}

        for i in s:
            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1



        for i in s:
            if i not in exist_key:
                while stack:
                    if stack[-1] <= i or counter[stack[-1]] == 1:
                        break
                    else:
                        remove_char = stack.pop()
                        del exist_key[remove_char]
                        counter[remove_char] -= 1
                if not stack or stack[-1] != i:
                    stack.append(i)
                    exist_key[i] = 1
                else:
                    counter[i] -= 1
            else:

                while stack:
                    if stack[-1] == i:
                        counter[i] -= 1
                        if queue and i < queue[-1]:
                            while queue:
                                stack.append(queue.pop())
                        else:
                            stack.pop()
                            while queue:
                                stack.append(queue.pop())
                            stack.append(i)

                        break
                    else:
                        queue.append(stack.pop())



        for i in stack:
            result +=i
        return result

print(Solution.removeDuplicateLetters(Solution,s))