num = [1,2,3,4]

def product_of_array_except_self(num_array):

    num_list_array = []
    result_array = []
    for index_num_array in num_array:
        num_list_array.append(num_array)

    for index_num_list_array in num_list_array:
        num_list_array[index_num_list_array].remove(index_num_list_array)

        #Ah.... Fail
        result_array.append()


    return result_array

1. 2,3,4,5 일 경우

   2,  2 * 3 , 2 * 3 * 4 , 2 * 3 * 4 * 5
   a    b          c            d

 아래와 같이 로직 짜면 된다^^
    
   5 제외 값  c    
   4 제외 값 (c -(4-1) * b)*5  = 2 * 3 * 5 --> e
   3 제외 값 (e- (3-1)*b)*4 = 2 * 4 * 5 --> f 
   
   별도
   2 제외 ??? --> 3 X 4 X 5

2. 2,3,4,5,6 일 경우
    2,  2 * 3 , 2 * 3 * 4 , 2 * 3 * 4 * 5, 2 * 3 * 4 * 5 * 6

    a    b      c            d                e

   6 제외 값 : d     2 X 3 X 4 X 5
   5 제외 값 : (d -(5-1)*c)* 6  : 2 X 3 X 4 X 6 d2
   4 제외 값 : (d2- (4-1)*?)*5




)




print(product_of_array_except_self(num))