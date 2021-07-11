class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x == 0:
            return 0

        second_max_multiply = 1
        for i in range(1,32):
            second_max_multiply *= 2
        minus_flag = False

        if x <0 :
            minus_flag = True
        x= abs(x)
        plus_max_int = second_max_multiply -1
        minus_max_int = -second_max_multiply

        stack = []
        while x % 10 == 0:
            x = int(x /10)

        while x >0:
            stack.append(str(x % 10))
            x = int(x/10)

        reverse_list =[]

        for i in stack:
            reverse_list.append(i)
        print(reverse_list)
        print("".join(reverse_list))
        result = int( "".join(reverse_list))
        if minus_flag:
            result *= -1

        if result > plus_max_int or result < minus_max_int:
            return 0


        return result

print(Solution.reverse(Solution,-12345678000000))
