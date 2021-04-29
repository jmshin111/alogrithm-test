from typing import List


input = "1+1"
input = "2*3-4*5"
input = "10+5"
class Solution:
    def operationResult(self,a:List,b:List,operator) -> List:
        result = []

        for i in a:
            for j in b:
                if(operator =='+'):
                    print(str(i) + "  +  " + str(j))
                    result.append(int(i)+int(j))
                elif (operator == '-'):
                    print(str(i) + "  -  " + str(j))
                    result.append(int(i) - int(j))
                else:
                    print(str(i) + "  *  " + str(j))
                    result.append(int(i) * int(j))
        return result

    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []

        start = 0
        if(input.isdigit()):
            return [input]
        operator =''
        for i in range(len(input)-2):

            if(input[i]=='*' or input[i]=='+' or input[i]=='-'):
                start = i
                continue
            if( start==0):
                a = [input[0]]
                b= Solution.diffWaysToCompute(self,input[2:])
                operator = input[1]

            elif( i>=2 ):
                a = Solution.diffWaysToCompute(self, input[:i+1])
                b = Solution.diffWaysToCompute(self, input[i+2:])
                operator = input[i+1]

            temp_result = Solution.operationResult(self, a, b, operator)

            for i in temp_result:
                result.append(i)

        return result




print(Solution.diffWaysToCompute(Solution,input))