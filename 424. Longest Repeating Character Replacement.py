#Input:
s = "ABAB"
k = 2

# s = "AABABBA"
# k = 1
#Output:
#4


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        before_char = s[0]
        maximum_distance = 0
        start = 0
        end = 0
        i = 0
        while( i < len(s)):

            if (i == 0):
                i +=1
                continue

            if before_char != s[i]:
                temp_k = k
                count = i - start+1
                index = i
                finish_yn = True
                temp_before_char = before_char
                while finish_yn :
                    if( s[index] != temp_before_char):
                        temp_k -= 1

                    count += 1
                    if s[index] != temp_before_char and temp_k == 0 :
                        finish_yn = False

                    temp_before_char = s[index]

                    if (index < len(s) - 1):
                        index += 1

                maximum_distance = max(maximum_distance,count)
                start = count
                i = count+1
                before_char = s[i-1]
            else:
                before_char = s[i]
                i += 1



        return maximum_distance

print(Solution.characterReplacement(Solution,s,k))

