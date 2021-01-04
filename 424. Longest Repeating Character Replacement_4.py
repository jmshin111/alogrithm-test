#Input:
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if (len(s) == 0):
            return 0
        repeat_char = s[0]
        maximum_distance = 0
        start = 0
        i = 0

        if(k==0):
            for i_s in range(len(s)):

                if(i_s == start):
                    continue
                if(s[i_s] != repeat_char or len(s)-1 == i_s):
                    if(s[i_s] == repeat_char and len(s)-1 == i_s):
                        maximum_distance = max(maximum_distance, i_s+1 - start)
                    else:
                        maximum_distance = max(maximum_distance, i_s - start)
                    start = i_s
                    repeat_char = s[i_s]

            return maximum_distance
        else:
            start = 0
            end = k
            count_s = collections.Counter(s[start:end+1])
            rest_num = 0
            while(True):
                if(start==12):
                     print(start)
                if end >=len(s)-1 or start >= len(s):
                    break
                max_char = sorted(count_s, key=lambda x: count_s[x],reverse=True)[0]
                # 이것 추가함
                if( count_s[max_char] != 1):
                    rest_num = rest_num + count_s[max_char]-1
                else:
                    rest_num = rest_num + count_s[max_char]
                if(rest_num>k):
                    rest_num = k
                if( count_s[max_char] != 1):
                    added_index = count_s[max_char]-1 +(k - rest_num)
                else:
                    added_index = k
                #added_index = 1 +k-rest_num

                while(True):
                    #이것 추가함
                    if(rest_num > 0 and s[start+added_index]!=max_char):
                        rest_num -=1
                    elif(rest_num == 0 and s[start+added_index]!=max_char):
                        break
                    count_s[s[start+added_index]] +=1
                    added_index += 1
                    if(start+added_index == len(s)):

                        break

                end = start +added_index

                maximum_distance = max(maximum_distance,rest_num+end-start)
                print(start,len(s[start:end]))
                print(s[start:end])

                before_max_char = max_char
                if(k!=1):
                    end -=1

                while( before_max_char == max_char):
                    if start >= end:
                        end = start +k
                        count_s = collections.Counter(s[start:end + 1])
                        rest_num = 0
                        break
                    count_s[s[start]] -= 1
                    start += 1

                    #이거 있고 없고에 따라 값이 바뀜
                    if(start < len(s) and s[start]!=max_char):
                        rest_num += 1

                    max_char = sorted(count_s, key=lambda x: count_s[x], reverse=True)[0]


            if(maximum_distance > len(s)):
                maximum_distance = len(s)
            return maximum_distance

# s = "AAAB"
# k = 0
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 3")
#
#
# s = "AAAA"
# k = 2
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
#
# s = "AABABBA"
# k = 1
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
# #
# s = "ABAB"
# k = 2
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
# s = "ABBB"
# k = 1
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")

# s = "AABABBA"
# k = 1
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
# #
# #
# s = "ABCDE"
# k = 1
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 2")
#
s ="KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
k =4
# 7

print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 7")
#
#
#
# s ="EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"
#
# k =7
# # 7
#
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 11")
#
#
# s ="QLHOSLDHOOBHFLPBSLHMSHMSRDOIFGGRTTSMKKRIENQNEECPLTJKCDMLRNNEPQAJDQFPEOGLKRBHSOMHONNTKLFHKNCHQLDBACMO"
# k =7
#
#
# print("=== s : "+s+" k : "+str(k)+"===")
# print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 10")
