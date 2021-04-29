
s = "au"
s = "abcabcbb"
s = "aab"
s= "pwwkew"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_count = 0
        char_group = {}
        end_index = 0
        if len(s)==1:
            return 1

        for i in range(len(s)):
            if i == len(s) - 1:
                if s[i] not in char_group:
                    max_count = i - end_index+1
                else:
                    max_count = i - end_index-1
                break


            if s[i] not in char_group:
                char_group[s[i]] = i

            else:
                if i-char_group[s[i]] == 1:
                    max_count = len(char_group)
                    char_group = {}
                    char_group[s[i]] = i
                    end_index = i-1
                else:
                    max_count = max(max_count, i - char_group[s[i]])
                    end_index =char_group[s[i]]
                    char_group[s[i]] = i

        return max_count

print(Solution.lengthOfLongestSubstring(Solution,s))