# 1


# num = [3, 6, 30, 34, 5, 9, 7, 95]
# num = [3, 30, 34, 5, 9]
# num = [6,7,9,88,99,34,765,342,123,983]
#num = [3, 30, 34, 5, 191]
# num = [12,121]
# num = [987,9,9,9]
#num = [999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1]
# num = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
num = [4,404]
one_num_list = []
two_num_list = []
three_num_list = []


def add_one_more_digit_and_find_max_more_line_1(str_to_compare, digit_status):
    temp_str = []
    temp_digital_list = []

    if (int(digit_status.split('_')[0]) >= 1):
        temp_str.append(str(one_num_list[int(digit_status.split('_')[0]) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0]) - 1)+ '_' + str(int(digit_status.split('_')[1]) )+ '_'  + str(int(digit_status.split('_')[2]) )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)
    if (int(digit_status.split('_')[1]) >= 1):
        temp_str.append(str(two_num_list[int(digit_status.split('_')[1]) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0]))+ '_' + str(int(digit_status.split('_')[1]) -1 )+ '_'  + str(int(digit_status.split('_')[2]) )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status.split('_')[2]) >= 1):
        temp_str.append(str(three_num_list[int(digit_status.split('_')[2]) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0]) )+ '_' + str(int(digit_status.split('_')[1]) )+ '_'  + str(int(digit_status.split('_')[2])-1 )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    temp_max = '0'
    temp_max_index = 0
    temp_max_digit_status = '0'
    temp_digit_status = '000'

    for index in range(3):

        if (compare_custom_digit(temp_str[index], temp_max, temp_digital_list[index], temp_max_digit_status)):
            temp_max = temp_str[index]
            temp_max_digit_status = temp_digital_list[index]
            temp_max_index = index

    return [temp_max_index, str_to_compare + temp_str[temp_max_index], temp_max_digit_status]


def add_one_more_digit_and_find_max_more_line_2(str_to_compare, digit_status):
    temp_str = []
    temp_digital_list = []

    # 11,12, 13, 2, 3
    if (int(digit_status.split('_')[0]) >= 2):
        temp_str.append(str(one_num_list[int(digit_status.split('_')[0]) - 1]) + str(one_num_list[int(digit_status[0].split('_')) - 2]))
        temp_digit_status = str(int(digit_status.split('_')[0])-2 ) + '_' + str(int(digit_status.split('_')[1]) ) + '_' + str(int(digit_status.split('_')[2]) )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status.split('_')[0]) >= 1 and int(digit_status.split('_')[1]) >= 1):
        temp_str.append(str(one_num_list[int(digit_status[0].split('_')) - 1]) + str(two_num_list[int(digit_status[1].split('_')) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0]) -1 ) + '_'+ str(int(digit_status.split('_')[1])-1 ) + '_' + str(int(digit_status.split('_')[2]) )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status.split('_')[0]) >= 1 and int(digit_status.split('_')[2]) >= 1):
        temp_str.append(str(one_num_list[int(digit_status[0].split('_')) - 1]) + str(three_num_list[int(digit_status[1].split('_')) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0])-1 ) + '_'+ str(int(digit_status.split('_')[1]) ) + '_' + str(int(digit_status.split('_')[2])-1 )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status.split('_')[1]) >= 1):
        temp_str.append(str(two_num_list[int(digit_status.split('_')[1]) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0])-1 ) + '_'+ str(int(digit_status.split('_')[1]) -1 ) + '_' + str(int(digit_status.split('_')[2]) )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    if (int(digit_status.split('_')[2]) >= 1):
        temp_str.append(str(three_num_list[int(digit_status.split('_')[2]) - 1]))
        temp_digit_status = str(int(digit_status.split('_')[0]) ) + '_'+ str(int(digit_status.split('_')[1]) ) + '_' + str(int(digit_status.split('_')[2])-1 )
        temp_digital_list.append(temp_digit_status)
    else:
        temp_str.append('0')
        temp_digital_list.append(digit_status)

    temp_max = '0'
    temp_max_index = '0'
    temp_max_digit_status = '0'
    temp_digit_status = '000'

    for index in range(5):

        if (compare_custom_digit(temp_str[index], temp_max, temp_digital_list[index], temp_max_digit_status)):
            temp_max = temp_str[index]
            temp_max_digit_status = temp_digital_list[index]
            temp_max_index = index

    return [temp_max_index, str_to_compare + temp_str[temp_max_index], temp_max_digit_status]


def compare_custom_digit(left_num_list_str, right_num_list_str, left_digit_status, right_digit_status):
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
            if len(left_num_list_str) - len(right_num_list_str) == 1:
                max_list = add_one_more_digit_and_find_max_more_line_1(right_num_list_str, right_digit_status)

                if (compare_custom_digit(left_num_list_str, max_list[1], left_digit_status, max_list[2])):
                    return True
                else:
                    return False
            else :
                max_list = add_one_more_digit_and_find_max_more_line_2(right_num_list_str, right_digit_status)

                if (compare_custom_digit(left_num_list_str, max_list[1], left_digit_status, max_list[2])):
                    return True
                else:
                    return False


    elif len(left_num_list_str) < len(right_num_list_str):
        if int(right_num_list_str[0:len(left_num_list_str)]) > int(left_num_list_str):
            return False
        elif int(right_num_list_str[0:len(left_num_list_str)]) < int(left_num_list_str):
            return True
        else:
            if   len(right_num_list_str) -len(left_num_list_str) ==1 :
                max_list = add_one_more_digit_and_find_max_more_line_1(left_num_list_str, left_digit_status)

                if (compare_custom_digit(right_num_list_str, max_list[1], right_digit_status, max_list[2])):
                    return False
                else:
                    return True
            else :
                max_list = add_one_more_digit_and_find_max_more_line_2(left_num_list_str, left_digit_status)

                if (compare_custom_digit(right_num_list_str, max_list[1], right_digit_status, max_list[2])):
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

        current_digit_status = str(len(one_num_list)) + '_' + str(len(two_num_list)) + '_' + str(len(three_num_list))
        max_list = add_one_more_digit_and_find_max_more_line_1(answer, current_digit_status)

        if (max_list[0] == 0 and len(one_num_list) != 0):
            answer += str(one_num_list.pop())
        elif (max_list[0] == 1 and len(two_num_list) != 0):
            answer += str(two_num_list.pop())
        elif (max_list[0] == 2 and len(three_num_list) != 0):
            answer += str(three_num_list.pop())

    return str(int(answer))


#print(solution(num))
# print(solution([6, 10, 2]),6210)
# print(solution([3, 30, 34, 5, 9]),9534330)
# print(solution([40,400]), 40400)
# print(solution([40,404]), 40440)
# print(solution([12,121]), 12121)
# print(solution([3054,305]), 3054305)
# print(solution([3044,304]), 3044304)
# print(solution([340,3403]), 3403403)
# print(solution([340,3402]), 3403402)
# print(solution([340,3405]), 3405340)
# print(solution([40,405]), 40540)
# print(solution([40,404]), 40440)
# print(solution([40,403]), 40403)
# print(solution([40,405]), 40540)
# print(solution([40,404]), 40440)
# print(solution([50,403]), 50403)
# print(solution([50,405]), 50405)
# print(solution([50,404]), 50404)
# print(solution([30,403]), 40330)
# print(solution([30,405]), 40530)
# print(solution([30,404]), 40430)
# print(solution([12,121]), 12121)

print(solution([2,22,223]), 223222)
#print(solution([1, 11, 111, 1111]),1111111111)

# print(solution([41,415]), 41541)
# print(solution([2,22 ]), 222)
# print(solution([70,0,0,0]), 70000)
# print(solution([0,0,0,1000]), 1000000)
# print(solution([0,0,0,0]),0)
# print(solution([0,0,70]),7000)
# print(solution([12,1213]), 121312)
# print(solution([3, 30, 34, 5, 91]),91534330)
# print(solution([3, 30, 34, 5, 191]),534330191)
# print(solution([3, 30, 34, 5, 191, 432789]),543278934330191)
# print(solution([1,2,3,4,5,44]),5444321)
# print(solution([1,2,3,4,5,66]),6654321)
# print(solution([3, 30, 31, 5, 9]),9533130)
# print(solution([3, 30, 31, 34, 5, 9]),953433130)
# print(solution([3, 30, 31, 34, 33, 5, 9]),95343333130)
# print(solution([10, 101]),10110)

print(solution([0, 0, 0, 0, 0, 0]),0)
