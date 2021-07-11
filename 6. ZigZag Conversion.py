
numRows = 2
s = "ABC"
s = "PAYPALISHIRING"
numRows = 2
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""

        list = []
        print(s[2:])
        if numRows==1:
            return s
        if numRows==2:
            return "".join(s[0::2])+"".join(s[1::2])

        for i in range(numRows):
            list.append([])

        for i in range(len(s)):

            current_idx = i % (2*(numRows-1))

            if current_idx < numRows:
                list[current_idx].append(s[i])
               #print(current_idx)
            else:
                updated_idx = (numRows-2)-(current_idx%numRows)
                #print(updated_idx)
                list[updated_idx].append(s[i])
        #print(list)
        str_list =[]
        for i in list:
            str_list.append("".join(i))

        return "".join(str_list)


print(Solution.convert(Solution, s,numRows))