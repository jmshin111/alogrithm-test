s = "cbacdcbc"
s ="abbbbbacccccb"

s = "cbacdcbc"
s = "cdadabcc"

s = "ecbacba"
s = "acacb"

s = "cbacdcbc"

s = "bcabc"
s = "cbacdcbc"
#bacd
#acdb
class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        result = ''

        stack = []
        exist_key = {}
        stack.append(s[0])
        exist_key[s[0]] = 1
        queue = []

        for i in range(1,len(s)):

            if stack[-1] == i:
                continue
            else:
                if s[i] not in exist_key:

                    stack.append(s[i])
                    exist_key[s[i]] = 1

                else:
                    while stack:
                        current_stack = stack.pop()

                        if (current_stack == s[i]):
                            if not queue:
                                stack.append(current_stack)
                                break
                            change_node = False

                            for k in queue:
                                if k < current_stack:
                                    change_node = True
                            if change_node:
                                while queue:
                                    stack.append(queue.pop())
                                stack.append(current_stack)
                            else:
                                stack.append(current_stack)
                                while queue:
                                    stack.append(queue.pop())
                            # queue_last = queue[len(queue)-1]
                            #
                            # if current_stack < queue_last:
                            #     stack.append(current_stack)
                            #
                            # while queue:
                            #     stack.append(queue.pop())
                            #
                            # if current_stack >= queue_last:
                            #     stack.append(current_stack)

                            break
                        else:
                            queue.append(current_stack)
            queue = []

        for i in stack:
            result +=i
        return result

print(Solution.removeDuplicateLetters(Solution,s))