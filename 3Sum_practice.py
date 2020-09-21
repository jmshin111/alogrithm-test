num = [-1,0,1,2,-1,-4]

def sum_3(num_array):

    num_array = sorted(num_array)
    result_arr = []
    print (num_array)

    zero_point = num_array.index(0, 0, len(num_array))
    print("zero point : "+  str(zero_point))
    for first_index_numarray in range(zero_point):
        for second_index_numarray in range(zero_point):
            if( second_index_numarray >first_index_numarray):
                for third_index_numarray in range(len(num_array)):
                    if  third_index_numarray < zero_point:
                        continue
                    if ( num_array[first_index_numarray] + num_array[second_index_numarray] + num_array[third_index_numarray]) == 0:
                        temp = []
                        temp.append(num_array[first_index_numarray])
                        temp.append(num_array[second_index_numarray])
                        temp.append(num_array[third_index_numarray])
                        print ( first_index_numarray, second_index_numarray, third_index_numarray)
                        result_arr.append(temp)


    for first_index_numarray in range(zero_point):
        for second_index_numarray in range(len(num_array)):
            if( second_index_numarray >= zero_point):
                for third_index_numarray in range(len(num_array)):
                    if  third_index_numarray < zero_point or second_index_numarray >= third_index_numarray:
                        continue
                    if ( num_array[first_index_numarray] + num_array[second_index_numarray] + num_array[third_index_numarray]) == 0:
                        temp = []
                        temp.append(num_array[first_index_numarray])
                        temp.append(num_array[second_index_numarray])
                        temp.append(num_array[third_index_numarray])
                        print( first_index_numarray, second_index_numarray, third_index_numarray)
                        result_arr.append(temp)
    return result_arr






print(sum_3(num))