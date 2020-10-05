num = [3, 6, 30, 34, 5, 9, 7, 95]


def solution(numbers):
    answer = ''
    num_list = numbers
    num_added_zero_list = []

    # find max length
    max_length = 0
    for index_num_list in num_list:
        if (max_length < len(str(index_num_list))):
            max_length = len(str(index_num_list))

    # add zero
    for index_num_list in range(len(num_list)):
        if (max_length > len(str(index_num_list))):

            zero_temp = ''
            zero_count = 0
            for index_zero in range(max_length - len(str(num_list[index_num_list]))):
                zero_temp += '0'
                zero_count = zero_count + 1

            num_added_zero_list.append(
                (str(num_list[index_num_list]) + zero_temp + '_' + str(+zero_count) + '_' + str(index_num_list)))
        else:
            num_added_zero_list.append(str(num_list[index_num_list]) + '_0' + '_' + str(index_num_list))

    num_added_zero_list = sorted(num_added_zero_list)

    print(num_added_zero_list)

    sorted_num_list = []

    for index_num_added_zero_list in range(len(num_added_zero_list)):
         sorted_num_list.append(num_list[int(
         str(num_added_zero_list[index_num_added_zero_list]).split('_')[2])])

    print(sorted_num_list)
    while (len(num_added_zero_list) !=0):
        temp_max = str(num_added_zero_list[len(num_added_zero_list)-1].split(('-'))[0])

        if (len(temp_max)==1):
            answer += num_added_zero_list.pop()
        elif (len(temp_max)==2):
            more_max_digit_founded = False
            for index_num_added_zero_list in range(len(num_added_zero_list)-1):

                first_index = len(num_added_zero_list)-1-index_num_added_zero_list
                if (len(num_added_zero_list[first_index]) == 1  and temp_max[0] == num_added_zero_list[first_index]):
                    for index2_num_added_zero_list in range(len(num_added_zero_list)-1-index_num_added_zero_list):
                        second_index = len(num_added_zero_list)-1-index_num_added_zero_list-index2_num_added_zero_list
                        if (len(num_added_zero_list[second_index]) == 1 and temp_max[1] < num_added_zero_list[second_index]):
                            answer += num_added_zero_list[first_index]
                            answer += num_added_zero_list[second_index]
                            num_added_zero_list.remove(num_added_zero_list[first_index])
                            num_added_zero_list.remove(num_added_zero_list[second_index])
                            more_max_digit_founded = True
                            break
            if not more_max_digit_founded:
                answer += num_added_zero_list.pop()
        elif  (len(temp_max)==3):
            more_max_digit_founded = False
            for index_num_added_zero_list in range(len(num_added_zero_list) - 1):

                first_index = len(num_added_zero_list) - 1 - index_num_added_zero_list
                if (len(num_added_zero_list[first_index]) == 1 and temp_max[0] == num_added_zero_list[first_index]):
                    for index2_num_added_zero_list in range(len(num_added_zero_list) - 1 - index_num_added_zero_list):
                        second_index = len(
                            num_added_zero_list) - 1 - index_num_added_zero_list - index2_num_added_zero_list
                        if (len(num_added_zero_list[second_index]) == 1 and temp_max[1] < num_added_zero_list[
                            second_index]):
                            for index3_num_added_zero_list in range(len(num_added_zero_list) - 1 - index_num_added_zero_list-index2_num_added_zero_list):
                                third_index = len(num_added_zero_list) - 1 - index_num_added_zero_list - index2_num_added_zero_list-index3_num_added_zero_list
                                if(len(num_added_zero_list[third_index]) == 1 and temp_max[1] < num_added_zero_list[
                            third_index] ):
                                    answer += num_added_zero_list[first_index]
                                    answer += num_added_zero_list[second_index]
                                    answer += num_added_zero_list[third_index]
                                    num_added_zero_list.remove(num_added_zero_list[first_index])
                                    num_added_zero_list.remove(num_added_zero_list[second_index])
                                    num_added_zero_list.remove(num_added_zero_list[third_index])
                                    more_max_digit_founded = True
                                    break





            if not more_max_digit_founded:
                answer += num_added_zero_list.pop()

        elif (len(temp_max) == 4):
            answer += num_added_zero_list.pop()








    # for index_num_added_zero_list in range(len(num_added_zero_list)):
    #      answer += str(num_list[int(
    #      str(num_added_zero_list[len(num_added_zero_list) - index_num_added_zero_list - 1]).split('_')[2])])

    return answer



print(solution(num))
