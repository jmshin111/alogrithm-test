#Input:
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if(len(s)==0):
            return 0

        end = 0
        count_s = {}
        max_char = ''
        maximum_distance = 0
        temp_k = k
        count_s[s[0]] = 1

        for start in range(len(s)-k):
            if(start == 7):
                print(start)

            if (start !=0 ):
                count_s[s[start-1]] -= 1

            max_char = sorted(count_s, key=lambda x: count_s[x], reverse=True)[0]

            while(True):

                sub_len = (end - start+1)
                temp_k = (sub_len -count_s[max_char])

                if( end == len(s)-1):
                    break


                if(temp_k > k):
                    if (end <len(s) and s[end] in count_s):
                        count_s[s[end]] -= 1
                    end -=1

                end += 1

                if (end < len(s)):
                   if (s[end] in count_s):
                      count_s[s[end]] += 1
                   else:
                      count_s[s[end]] = 1

                if(temp_k >= k):
                    break


            while( end <= len(s)-1 and s[end] == max_char):
                end += 1
                if (end < len(s)):
                    if (s[end] in count_s):
                        count_s[s[end]] += 1
                    else:
                        count_s[s[end]] = 1

                else:
                    break
            #NEw Added
            if( end == len(s)-1 and k > temp_k):
                end +=1
            max_char = sorted(count_s, key=lambda x: count_s[x], reverse=True)[0]

            maximum_distance = max(maximum_distance,(end)-start+k-temp_k)
            # print("=== start : " + str(start))
            # print((end)-start+k-temp_k)
            # print(s[start:(end)+k-temp_k])


        if( maximum_distance > len(s)):
            maximum_distance = len(s)
        return maximum_distance
#
s = "IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR"
k = 2

print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 6")

s = "AABA"
k = 0
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 2")


s = "AAAA"
k = 0
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")



s = "AAAB"
k = 0
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 3")


s = "AAAA"
k = 2
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")



s = "AABABBA"
k = 1
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")
#
#
s = "ABAB"
k = 2
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 4")

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

s = "BAAAB"
k =2
print("=== s : "+s+" k : "+str(k)+"===")
print("Module OutPut : "+ str(Solution.characterReplacement(Solution,s,k))+ " Real Output : 5")
