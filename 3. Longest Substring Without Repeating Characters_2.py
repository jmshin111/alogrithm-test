




s = "aab"




s = "au"
s = "abcabcbb"


s ="dvdf"
s= "pwwkew"
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_count = 0
        j = 0
        char_group = {}
        if len(s) == 0 :
            return 0

        for i in range(len(s)):

            if s[i] in char_group:
                j = max(j,char_group[s[i]]+1)

            char_group[s[i]] = i

            max_count = max(max_count,i-j+1)
        return max_count

print(Solution.lengthOfLongestSubstring(Solution,s))