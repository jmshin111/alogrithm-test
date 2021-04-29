from typing import List



input = "10+5"
input = "1+1"
input = "2*3-4*5"

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
        operator_list = []
        start = 0
        if(input.isdigit()):
            return [input]

        before_operator_count = 0
        for i in range(len(input)):
            operator = ''
            a = []
            b = []
            temp_result = []
            if(input[i]=='*' or input[i]=='+' or input[i]=='-'):
                operator_list.append(input[i])

            if( len(operator_list)> before_operator_count ):
                before_operator_count = len(operator_list)
                a = Solution.diffWaysToCompute(self, input[:i])
                b = Solution.diffWaysToCompute(self, input[i+1:])
                operator = operator_list[-1]

                temp_result = Solution.operationResult(self, a, b, operator)
            if(temp_result):
                for i in temp_result:
                    result.append(i)

        return result

print(Solution.diffWaysToCompute(Solution,input))