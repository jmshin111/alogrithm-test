# s = "abc"
# t = "ac"
# s = "a"
# t = "a"
s = "ADOBECODEBANC"
t = "ABC"
# s = "AB"
# t = "A"

#Output: "BANC"

class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if (t == s):
            return t
        t = sorted(t)
        k = len(t)

        result =''
        while( k<= len(s)):
            for i in range(len(s)-k):
                sorted_s = sorted(s[i:i+k+1])

                finded_count = 0
                for i_t in t:
                    if(i_t in sorted_s):
                        finded_count +=1

                if(finded_count == len(t)):
                    return s[i:i+k+1]
            k += 1


        return ""


print(Solution.minWindow(Solution,s,t))

