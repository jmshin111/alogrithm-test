num = [7, 1, 5, 3, 6, 4]


def bestTimeToBuyandSell(num_array):
    zero_result_array = []
    zero_min_array = []
    zero_max_array = []

    zero_min_array.append(0)

    for index_num_array in range(len(num_array) - 2):

        if num_array[index_num_array + 1] > num_array[index_num_array] and num_array[index_num_array + 2] < num_array[
            index_num_array + 1]:
            zero_max_array.append(index_num_array + 1)
        elif num_array[index_num_array + 1] < num_array[index_num_array] and num_array[index_num_array + 2] > num_array[
            index_num_array + 1]:
            zero_min_array.append(index_num_array + 1)
    zero_min_array.append(len(num_array) - 1)

    index_min = 0
    index_max = 0
    profit = 0
    min_value = 999

    while (index_min < len(zero_min_array) and index_max < len(zero_max_array)):

        if (zero_min_array[index_min] < zero_max_array[index_max]):
            min_value = min(num_array[zero_min_array[index_min]] ,min_value )
            temp_profit = num_array[zero_max_array[index_max]] - min_value
            if(profit < temp_profit):
                profit = temp_profit
            index_min = index_min + 1
        else:
            index_max = index_max + 1

    return profit



print(bestTimeToBuyandSell(num))
