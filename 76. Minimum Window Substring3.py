s = "abc"
t = "ac"
# s = "a"
# t = "a"
# s = "ADOBECODEBANC"
# t = "ABC"
# s = "AB"
# t = "A"
s = "bba"
t ="ab"
#Output: "BANC"

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        minimum_char_list = []
        minimum_index_list = []
        for i in range(len(s)):
            if s[i] in t:
                minimum_char_list.append(s[i])
                minimum_index_list.append(i)


        k = len(t)
        start = 0
        end = 0
        minimum_distance = 999999
        founded = False
        for j in range(len(minimum_char_list)-k+1):
           count = 0


           for z in t:
            if z in minimum_char_list[j:j+k]:
             count += 1

           if count == len(t) and minimum_distance >minimum_index_list[j+k-1]-minimum_index_list[j]:
             founded = True
             start = j
             end = j+k-1
             minimum_distance = minimum_index_list[j + k- 1] - minimum_index_list[j]
        if founded:
            return s[minimum_index_list[start]:minimum_index_list[end]+1]
        else:
            return ""


print(Solution.minWindow(Solution,s,t))
