num = [1,4,3,2,5]

def array_partiotion(num_array):
    result_num = 0

    if len(num_array) % 2 == 0:
        num_array =  sorted(num_array)
    else:
        num_array = sorted(num_array)
        num_array = num_array[1:(len(num_array))]


    max_list =[]
    min_list = []

    for index_num_array in range(len(num_array)):
        if index_num_array % 2 == 0:
            min_list.append(num_array[index_num_array])
        else:
            max_list.append(num_array[index_num_array])


    for index_list in range(len(min_list)):
        result_num += min(min_list[index_list],max_list[index_list])

    return result_num






print(array_partiotion(num))