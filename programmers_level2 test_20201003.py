# 1


#num = [3, 6, 30, 34, 5, 9, 7, 95]
#num = [3, 30, 34, 5, 9]
#num = [6,7,9,88,99,34,765,342,123,983]
#num = [3, 30, 34, 5, 191]
#num = [12,121]
#num = [987,9,9,9]
num = [999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,9,7,8,6]

one_num_list = []
two_num_list = []
three_num_list = []

def add_one_more_digit_and_find_max_more_line_1(str_to_compare, digit_status):
    temp_str = []
    temp_digital_list =[]

    if (int(digit_status[0]) >= 1):
        temp_str.append(str(one_num_list[int(digit_status[0]) - 1]))
        temp_digit_status = str(int(digit_status[0]) - 1) +digit_status[1:3]
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)
    if (int(digit_status[1]) >= 1):
        temp_str.append(str(two_num_list[int(digit_status[1]) - 1]))
        temp_digit_status = digit_status[0] + str(int(digit_status[1]) - 1) + digit_status[2]
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status[2]) >= 1):
        temp_str.append( str(three_num_list[int(digit_status[2]) - 1]))
        temp_digit_status = digit_status[0:2] + str(int(digit_status[2]) - 1)
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    temp_max = '0'
    temp_max_index = 0
    temp_max_digit_status ='0'
    temp_digit_status = '000'

    for index in range(3):

        if (compare_custom_digit(temp_str[index],temp_max, temp_digital_list[index],  temp_max_digit_status  ) ):
            temp_max =  temp_str[index]
            temp_max_digit_status =temp_digital_list[index]
            temp_max_index = index

    return [temp_max_index, str_to_compare + temp_str[temp_max_index],temp_max_digit_status]


def add_one_more_digit_and_find_max_more_line_2(str_to_compare, digit_status):
    temp_str = []
    temp_digital_list =[]

    #11,12, 13, 2, 3
    if (int(digit_status[0]) >=2):
        temp_str.append( str(one_num_list[int(digit_status[0]) - 1])+ str(one_num_list[int(digit_status[0]) - 2]))
        temp_digit_status = str(int(digit_status[0]) - 2) +digit_status[1:3]
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)


    if (int(digit_status[0]) >= 1 and int(digit_status[1]) >= 1 ):
        temp_str.append( str(one_num_list[int(digit_status[0]) - 1]) + str(two_num_list[int(digit_status[1]) - 1]))
        temp_digit_status = str(int(digit_status[0]) - 1) + str(int(digit_status[1]) - 1) + digit_status[2]
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status[0]) >= 1 and int(digit_status[2]) >= 1 ):
        temp_str.append(str(one_num_list[int(digit_status[0]) - 1]) + str(three_num_list[int(digit_status[1]) - 1]))
        temp_digit_status = str(int(digit_status[0]) - 1)  + digit_status[1]+ str(int(digit_status[2]) - 1)
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status[1]) >= 1):
        temp_str.append( str(two_num_list[int(digit_status[1]) - 1]))
        temp_digit_status = digit_status[0] + str(int(digit_status[1]) - 1) + digit_status[2]
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status[2]) >= 1):
        temp_str.append( str(three_num_list[int(digit_status[2]) - 1]))
        temp_digit_status = digit_status[0:2] + str(int(digit_status[2]) - 1)
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    temp_max = '0'
    temp_max_index = '0'
    temp_max_digit_status ='0'
    temp_digit_status = '000'

    for index in range(5):

        if (compare_custom_digit(temp_str[index],temp_max, temp_digital_list[index],  temp_max_digit_status  ) ):
            temp_max =  temp_str[index]
            temp_max_digit_status =temp_digital_list[index]
            temp_max_index = index

    return [temp_max_index, str_to_compare + temp_str[temp_max_index],temp_max_digit_status]





def compare_custom_digit(left_num_list_str,right_num_list_str,left_digit_status,right_digit_status):

    if len(left_num_list_str) == len(right_num_list_str):
        if int(left_num_list_str) > int(right_num_list_str):
            return True
        else:
            return False
    elif len(left_num_list_str) > len(right_num_list_str):

        if int(left_num_list_str[0:len(right_num_list_str)]) > int(right_num_list_str):
            return True
        elif int(left_num_list_str[0:len(right_num_list_str)]) < int(right_num_list_str):
            return False
        else:
                max_list = add_one_more_digit_and_find_max_more_line_1(right_num_list_str,right_digit_status)

                if(compare_custom_digit(left_num_list_str,max_list[1],left_digit_status,max_list[2])):
                    return True
                else:
                    return False

    elif len(left_num_list_str) < len(right_num_list_str):
        if int(right_num_list_str[0:len(left_num_list_str)]) > int(left_num_list_str):
            return False
        elif int(right_num_list_str[0:len(left_num_list_str)]) < int(left_num_list_str):
            return True
        else:
                max_list = add_one_more_digit_and_find_max_more_line_1(left_num_list_str,left_digit_status)

                if(compare_custom_digit(right_num_list_str,max_list[1],right_digit_status,max_list[2])):
                    return False
                else:
                    return True


    return True


def solution(numbers):
    answer = ''

    for index_num in numbers:
        if len(str(index_num)) == 1:
            one_num_list.append(index_num)
        elif len(str(index_num)) == 2:
            two_num_list.append(index_num)
        elif len(str(index_num)) == 3:
            three_num_list.append(index_num)
        elif len(str(index_num)) == 4:
            answer += str(index_num)

    one_num_list.sort()
    two_num_list.sort()
    three_num_list.sort()


    while (len(one_num_list) != 0 or len(two_num_list) != 0 or len(three_num_list) != 0):

        current_digit_status = str(len(one_num_list))+ str(len(two_num_list))+  str(len(three_num_list))
        max_list = add_one_more_digit_and_find_max_more_line_1(answer, current_digit_status)

        if(max_list[0] == 0 and len(one_num_list) !=0 ):
            answer += str(one_num_list.pop())
        elif(max_list[0] == 1 and len(two_num_list) !=0 ):
            answer += str(two_num_list.pop())
        elif (max_list[0] == 2 and len(three_num_list) !=0 ) :
            answer += str(three_num_list.pop())

    return answer


print(solution(num))

