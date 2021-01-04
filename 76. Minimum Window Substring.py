s = "ADOBECODEBANC"
t = "ABC"
#Output: "BANC"

class Solution:


    def makeDic(self,s,t)->{}:
        char_dic = {}

        for i in t:
            temp_s = s
            temp_list = []
            current_index = 0
            while (temp_s.count(i) > 0):

                target_index = temp_s.index(i)
                if len(temp_list) > 0:
                    temp_list.append(temp_list[-1] + target_index)
                else:
                    temp_list.append(target_index)
                temp_s = temp_s[(target_index + 1):]
            char_dic[i] = temp_list
        return char_dic



    def minWindow(self, s: str, t: str) -> str:
        dic = Solution.makeDic(self, s, t)

        result = []
        start ,end= 0, 0

        last_one = True
        for i in sorted(dic,key= lambda x: (len(dic[x]))):
            if len(dic[i]) == 1:
                result.append(i)
                continue

            elif last_one :
                result = sorted(result)
                if(len(result)>0):
                    start = result[0]
                    end = result[-1]
                else:
                    temp_index = dic[i][0]

                    start = temp_index
                    end = temp_index

                last_one = False


            min_distance = 999999999
            min_index = 9999999
            for j in dic[i]:
                if start < j and j < end:
                    break
                elif j < start:
                    current_distance = start - j
                    if(  current_distance < min_distance):
                        min_distance = current_distance
                        min_index = j
                else:
                    current_distance = j - end
                    if(  current_distance < min_distance):
                        min_distance = current_distance
                        min_index = j
            if min_index < start :
                start = min_index
            else:
                end = min_index

        return s[start:end]


Solution.minWindow(Solution,s,t)
