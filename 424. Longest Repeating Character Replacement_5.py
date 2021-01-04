#Input:
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        end = 0
        count_s = {}
        max_char = ''
        maximum_distance = 0
        temp_k = k
        count_s[s[0]] = 1


        for start in range(len(s)-k):


            if (start !=0 ):
                count_s[s[start-1]] -= 1

            max_char = sorted(count_s, key=lambda x: count_s[x], reverse=True)[0]

            temp_k = 0
            while(True):

                sub_len = (end - start+1)
                temp_k = (sub_len -count_s[max_char])

                if(temp_k > k):
                    end -=1
                    break

                if( end == len(s)-1):
                    break

                while( end < len(s)-1 and k == temp_k and s[end+1] == max_char):
                    if (end < len(s)):
                        if (s[end] in count_s):
                            count_s[s[end]] += 1
                        else:
                            count_s[s[end]] = 1
                    end +=1

                #new Added

                # if(k==temp_k):
                #     break

                end += 1

                if(end < len(s)):
                    if (s[end] in count_s):
                        count_s[s[end]] += 1
                    else:
                        count_s[s[end]] = 1
                else:
                    break
                max_char = sorted(count_s, key=lambda x: count_s[x], reverse=True)[0]

            maximum_distance = max(maximum_distance,end-start+1+k-temp_k)


        if( maximum_distance > len(s)):
            maximum_distance = len(s)
        return maximum_distance

s = "AABA"
k = 0
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 2")
#

s = "AAAA"
k = 0
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")



s = "AAAB"
k = 0
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 3")
#
#
s = "AAAA"
k = 2
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
#

s = "AABABBA"
k = 1
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
# #
s = "ABAB"
k = 2
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
s = "ABBB"
k = 1
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")

s = "AABABBA"
k = 1
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
# #
# #
s = "ABCDE"
k = 1
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 2")
#
s ="KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
k =4
# 7

print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 7")
#
#
#
s ="EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH"

k =7
# 7

print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 11")
#
#
s ="QLHOSLDHOOBHFLPBSLHMSHMSRDOIFGGRTTSMKKRIENQNEECPLTJKCDMLRNNEPQAJDQFPEOGLKRBHSOMHONNTKLFHKNCHQLDBACMO"
k =7


print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 10")
