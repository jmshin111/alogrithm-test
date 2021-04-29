s = "cbacdcbc"
s ="abbbbbacccccb"
s = "bcabc"
s = "cbacdcbc"
s = "cdadabcc"
s = "cbacdcbc"
s = "ecbacba"
s = "acacb"
class Solution:

    def checkAllFinished(self,counter:{})->bool:

        for i in counter:
            if counter[i] > -1:
                return False

        return True
    def recursiveMakeDicLetters(self,s:str,counter:{})->str:

        min_char = '{'
        min_index = -1
        prefix_char = ''
        one_char = ''
        one_index =-1
        for i in range(len(s)):
            if (counter[s[i]]==1 and one_char ==''):
                one_char = s[i]
                one_index = i


            if (counter[s[i]] >-1 and s[i]<min_char ):
                min_char = s[i]
                min_index = i
        if one_index != -1 and one_index < min_index:
            min_index = one_index
            min_char = one_char

        for i in range(min_index+1):
            if s[i] <= min_char and counter[s[i]] >-1:
                prefix_char += s[i]
                counter[s[i]] = -1
            else:
                counter[s[i]] -= 1
        print(s, 'prefix_char', prefix_char, 'min_char', min_char, 'min_index', min_index, 'one_char', one_char,  'one_index', one_index, 'counter', counter)
        if min_index == len(s)-1 or Solution.checkAllFinished(Solution,counter) :
            return prefix_char
        else:
            return prefix_char + Solution.recursiveMakeDicLetters(Solution,s[min_index+1:],counter)

    def removeDuplicateLetters(self, s: str) -> str:
        result = ''
        counter = {}
        visited = {}
        new_s = ''
        before_char = ''
        same_char = False
        for i in s:
            if before_char == i:
                same_char = True
                continue
            else:
                if same_char:
                    same_char = False

            if i not in counter:
                counter[i] = 1
            else:
                counter[i] += 1
            new_s += i
            before_char = i
        #print(new_s,counter)
        #print()
        return Solution.recursiveMakeDicLetters(Solution,new_s,counter)

print(Solution.removeDuplicateLetters(Solution,s))