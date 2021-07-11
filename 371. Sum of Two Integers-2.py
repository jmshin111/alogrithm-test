import math

a= -1000
b= -1000



class Solution:
    def getSum(self, a: int, b: int) -> int:


        def addTwoBinary(a1:str,b1:str)->str:
            result = []
            print('a1',a1)
            print('b1', b1)
            c= 0
            for i in range(12, -1, -1):

                b_a = int(a1[i])
                b_b = int(b1[i])
                sum = (b_a ^ b_b) ^ c
                result.append(str(sum))

                c = (c & (b_a ^ b_b)) | (b_a & b_b)

            result_str = "".join(result[::-1])
            return result_str

        def makeBinary(number:int,minus_flag:bool)->str:

            bianry_number =['0','0']

            for i in range(10,-1,-1):

                if number >= math.pow(2,i):
                    number -= math.pow(2,i)
                    bianry_number.append('1')

                else:
                    bianry_number.append('0')

            result_str =  "".join(bianry_number)
            if minus_flag:
                apply_minus_flag_result_str =[]
                for i in result_str:
                    if i =='0':
                        apply_minus_flag_result_str.append('1')
                    else:
                        apply_minus_flag_result_str.append('0')
                return addTwoBinary("".join(apply_minus_flag_result_str),'0000000000001')

            return result_str

        a_minus_flag= False
        b_minus_flag = False
        if a < 0:
            a_minus_flag = True
        if b < 0:
            b_minus_flag = True
        changed_a = makeBinary(abs(a), a_minus_flag)
        changed_b = makeBinary(abs(b), b_minus_flag)
        print('a',changed_a)
        print('b',changed_b)

        result_binary = addTwoBinary(changed_a,changed_b)
        print('result_binary',result_binary[1:])
        if result_binary[0]=='0':
            return int('0b'+result_binary[1:],2)
        else:
            new_result = []
            for i in result_binary:
                if i =='0':
                    new_result.append('1')
                else:
                    new_result.append('0')

            return - int('0b'+ addTwoBinary("".join(new_result), '0000000000001'),2)




print(Solution.getSum(Solution,a,b))
