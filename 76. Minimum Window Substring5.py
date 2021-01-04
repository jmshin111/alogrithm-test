#s = "abc"
#t = "ac"
# s = "a"
# t = "a"
import sys



# s = "ADOBECODEBANC"
# t = "ABC"
# s= "aaaaaaaaaabbbbbcdd"
# t = "abcdd"
# s = "AB"
# t = "A"
#s = "bba"
#t ="ab"
#Output: "BANC"
# s

s = "tkopjjgknziznmfwvkgospwkujjklzugjiwvuefhepiteppbzyptplekwnwjmqqybovvsccyrnuxclyclnvbaznxojgdzydcmyxhacftpbrrnrvyftbfuoelxlozjtbyrbftdkoumhnbzlzgeblarslpdbqoutmnwrgzexvsejtfwulcxzcprqgwrykorxboqkpwhnonyjvuggwdfauyqauiafyseziwjztsojimvdiblegrhdrxdmhetfyxfitqjolaytmtyxwjdeckhuingptbxtyedtumihmgcbbayxkbdomliwyqnrrkmropllbvsqbvtexrdjugyirierzsksewktlxepsyhvvabttecpkayejevkyiedeqwsncjhascwudrnjteuwcahhxtffxkmoggdkpllhpjbvcqevuatzaaiyvpftarjixmtoxgxnraitsoqnpkormwpilxbnomwoypcwvclocvhvlxkajaswwjejghzxtvltmprjrcxwzetldfnnffjdrpoxynurkhmwxefqieoikhvooibvqmyhdpgbcdunkgljktatxqdiaywoizkynkhqzqretntftepgxrzvjcdjcbykcklpwufykycfnvngzcmzvnwerzotcogearvwncuaayfptsvvwkwtzsyrtokveqbgjwexyzxazepvzmqvymryeppxfbuluvrdtvcrwbtwikthwjevxvvdmmcrnyehvvnotrhrvcndmgkirofqkavwmzqcxwluuyinsrentuqfccqwqvocykbmltolpafjaqyshfhbbzidbybuwqwuczgnsxykxgvxwusdbbgcbrfcpjwnzvhbuqqpnrzmxujtqdyrfhvgydkpmjdlemoacgprzqdwnprfssxzz"
t = "ufzxqojzrufekhitzcsphr"
# s = "bba"
# t = "ab"

class Solution:

    def makeKeyValue(self,key:{},p_list:[])->{}:

        for i_list in p_list:
            if (key.get(i_list)):
                key[i_list] += 1
            else:
                key[i_list] = 1

        return key

    def minWindow(self, s: str, t: str) -> str:
        minimum_char_list = []
        minimum_index_list = []

        for i in range(len(s)):
            if s[i] in t:
                minimum_char_list.append(s[i])
                minimum_index_list.append(i)

        t_key = {}
        t_key = Solution.makeKeyValue(self,t_key,t)

        founded = False
        k = len(t)


        minimum_size = sys.maxsize
        while(k <= len(minimum_char_list) ):
            for j in range(len(minimum_char_list)-k+1):

                j_key = {}
                j_key = Solution.makeKeyValue(self, j_key, minimum_char_list[j:j+k])
                substring_yn = True

              # print(" K : "+str(k)+" Substirng : "+s[minimum_index_list[j]:minimum_index_list[j + k - 1] + 1])
               # if (k==25 and s[minimum_index_list[j]:minimum_index_list[j + k - 1] + 1])
                for i_t_key in t_key:
                    if(not j_key.get(i_t_key) or j_key[i_t_key] < t_key[i_t_key]):
                        substring_yn = False
                        break

                if not substring_yn:
                    continue

                founded = True
                distance = minimum_index_list[j+k-1] - minimum_index_list[j]

                if (minimum_size > distance):
                    start = j
                    end = j+k-1
                    minimum_size = distance

            # if founded:
            #     break
            k = k+1

        if founded:
            return s[minimum_index_list[start]:minimum_index_list[end]+1]
        else:
            return ""


print(sorted("ytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmo"))
print(sorted("ozgzyywxvtublcl"))
print(Solution.minWindow(Solution,s,t))
