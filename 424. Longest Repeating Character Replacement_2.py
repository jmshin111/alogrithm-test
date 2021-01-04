#Input:


s = "AAAB"
k = 0
s = "ABAA"
k = 0
s = "AAAA"
k = 2


s = "AAAA"
k = 2
s = "AABABBA"
k = 1



s = "AABA"
k = 0

s = "ABAA"
k = 0


s = "ABAB"
k = 2
s = "AABABBA"
k = 1
#Output:
#4


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        before_char = s[0]
        maximum_distance = 0
        start = 0
        i = 0

        while( i < len(s)):

            if (start == i):
                i +=1
                continue

            if before_char != s[i]:
                temp_k = k
                repeat_char = before_char
                index = i

                while True :
                    if(index >= len(s)):
                        break
                    if( s[index] != repeat_char):
                        temp_k -= 1
                    if(index +1  < len(s)):
                        index = index +1
                    if s[index] != repeat_char and temp_k <= 0 :
                        if(index +1 == len(s)):
                            index += 1
                        if(temp_k<0):
                            index -= 1
                        if(index<len(s)):
                            before_char = s[index]
                        break

                    index += 1

                maximum_distance = max(maximum_distance,index-start)
                i = index
                start = index


            else:
                if(i==len(s)-1):
                    return i-start+1
                before_char = s[i]
                i += 1

        return maximum_distance

print(Solution.characterReplacement(Solution,s,k))

