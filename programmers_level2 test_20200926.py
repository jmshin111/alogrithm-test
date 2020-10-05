

NOTATATION = '0123456789ABCDEF'

def numeral_system(number,base):
    q, r = divmod(number, base)
    n = NOTATATION[r]
    return numeral_system(q,base)+ n if q else n

def array_partiotion(n, t, m, p):

    answer = ''
    number_result=''
    for index in range(t*m):
     number_result += numeral_system(int(index),n)

    for t_index in range(t):
        answer +=number_result[t_index*m+p-1]

    return answer


print(array_partiotion(2,4,2,1))