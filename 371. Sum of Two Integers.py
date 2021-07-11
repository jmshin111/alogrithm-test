a= -32
b= 2049

class Solution:
    def getSum(self, a: int, b: int) -> int:

        print('a',bin(a))
        print('b',bin(b))

        mask = 0x7FF
        c = 0

        binary_a = bin(mask & a)
        binary_b = bin(mask & b)

        print('a',binary_a)
        print('b',binary_b)

        binary_a = binary_a[2:]
        binary_b = binary_b[2:]

        if len(binary_a) !=11:
            while True:
                if len(binary_a) != 11:
                    binary_a = '0'+binary_a
                else:
                    break

        if len(binary_b) !=11:
            while True:
                if len(binary_b) != 11:
                    binary_b = '0'+binary_b
                else:
                    break

        print('balance_a',binary_a)
        print('balance_b',binary_b)
        result = []

        for i in range(10,0,-1):
            b_a= int(binary_a[i])
            b_b = int(binary_b[i])
            sum = (b_a ^ b_b) ^ c
            result.append(str(sum))

            c = (c & (b_a ^ b_b)) | (b_a & b_b)

            print('a',b_a,'b',b_b,'sum',sum,'c',c)
            print("".join(result)[::-1])

        result_str = "".join(result[::-1])

        print('answer',result_str)

        if result_str[0] =='1':

            print('result_str',-(512- int(result_str[1:],2)))


            #print(mask&(int('0b'+result_str)))
            return -(512- int(result_str[1:],2))
        else:
            return int(result_str, 2)
print(Solution.getSum(Solution,a,b))