#num = [3, 6, 30, 34, 5, 9, 7, 95]
num = [3, 30, 34, 5, 9]


def fine_max(num_list):
    max = -1
    index_max = -1
    for index_num_list in range(len(num_list)):
        if max <=  num_list[index_num_list]:
            index_max = index_num_list
            max = num_list[index_num_list]

    return index_max


def solution(numbers):
    answer = ''

    one_num_list = []
    two_num_list = []
    three_num_list = []

    for index_num in numbers:
        if len(str(index_num)) == 1:
            one_num_list.append(index_num)
        elif len(str(index_num)) == 2:
            two_num_list.append(index_num)
        elif len(str(index_num)) == 3:
            three_num_list.append(index_num)
        elif len(str(index_num)) == 4:
            answer += str(index_num)

    one_num_list = sorted(one_num_list)
    two_num_list = sorted(two_num_list)
    three_num_list = sorted(three_num_list)

    while (len(one_num_list) != 0 or len(two_num_list) != 0 or len(three_num_list) != 0):
        find_max_index_list = []

        # 0 index, 1 1 1
        if len(one_num_list) >= 3:
            last_index = len(one_num_list) - 1
            find_max_index_list.append(int(
                str(one_num_list[last_index]) + str(one_num_list[last_index - 1]) + str(one_num_list[last_index - 2])))
        else:
            find_max_index_list.append(-1)
        # 1 index, 2 2
        if len(two_num_list) >= 2:
            last_index = len(two_num_list) - 1
            find_max_index_list.append(int(
                (str(two_num_list[last_index]) + str(two_num_list[last_index - 1]))[0:3]))
        else:
            find_max_index_list.append(-1)
        # 2 index, 3
        if len(three_num_list) >= 1:
            last_index = len(three_num_list) - 1
            find_max_index_list.append(int((str(three_num_list[last_index]))))
        else:
            find_max_index_list.append(-1)
        # 3 index, 1, 2
        if len(one_num_list) >= 1 and len(two_num_list) >= 1:
            last_one_index = len(one_num_list) - 1
            last_two_index = len(two_num_list) - 1
            find_max_index_list.append(int(
                (str(one_num_list[last_one_index]) + str(two_num_list[last_two_index]))))
        else:
            find_max_index_list.append(-1)
        # 4 index, 1, 2
        if len(one_num_list) >= 1 and len(two_num_list) >= 1:
            last_one_index = len(one_num_list) - 1
            last_two_index = len(two_num_list) - 1
            find_max_index_list.append(int(
                (str(two_num_list[last_two_index]) + str(one_num_list[last_one_index]))))
        else:
            find_max_index_list.append(-1)
        # 5 index 1, 1, 2
        if len(one_num_list) >= 2 and len(two_num_list) >= 1:
            last_one_index = len(one_num_list) - 1
            last_two_index = len(two_num_list) - 1
            find_max_index_list.append(int(
                (str(one_num_list[last_one_index]) + str(one_num_list[last_one_index -1] ) + str(
                    two_num_list[last_two_index])[0:1])))
        else:
            find_max_index_list.append(-1)

        # 6 index 1, 1, 3
        if len(one_num_list) >= 2 and len(three_num_list) >= 1:
            last_one_index = len(one_num_list) - 1
            last_three_index = len(two_num_list) - 1
            find_max_index_list.append(int(
                (str(one_num_list[last_one_index]) + str(one_num_list[last_one_index -1 ]) + str(
                    two_num_list[last_three_index]))))
        else:
            find_max_index_list.append(-1)

        # 7 index 2, 3
        if len(two_num_list) >= 1 and len(three_num_list) >= 1:
            last_two_index = len(two_num_list) - 1
            last_three_index = len(three_num_list) - 1
            find_max_index_list.append(int(
                (str(two_num_list[last_two_index]) + str(
                    three_num_list[last_three_index]))))
        else:
            find_max_index_list.append(-1)

        selected_index = fine_max(find_max_index_list)

        # 0 index, 1 1 1

        # 1 index, 2 2

        # 2 index, 3

        # 3 index, 1, 2

        # 4 index, 1, 2

        # 5 index 1, 1, 2

        # 6 index 1, 1, 3

        # 7 index 2, 3
        if selected_index == 0:
            answer += str(one_num_list.pop())
            answer += str(one_num_list.pop())
            answer += str(one_num_list.pop())
        elif selected_index == 1:
            answer += str(two_num_list.pop())
            answer += str(two_num_list.pop())
        elif selected_index == 2:
            answer += str(three_num_list.pop())
        elif selected_index == 3:
            answer += str(one_num_list.pop())
            answer += str(two_num_list.pop())
        elif selected_index == 4:
            answer += str(two_num_list.pop())
            answer += str(one_num_list.pop())
        elif selected_index == 5:
            answer += str(one_num_list.pop())
            answer += str(one_num_list.pop())
            answer += str(two_num_list.pop())
        elif selected_index == 6:
            answer += str(one_num_list.pop())
            answer += str(one_num_list.pop())
            answer += str(three_num_list.pop())
        elif selected_index == 7:
            answer += str(two_num_list.pop())
            answer += str(three_num_list.pop())

        if len(one_num_list) == 1 and len(two_num_list) == 0 and len(three_num_list) == 0:
            answer += str(one_num_list.pop())

        if len(one_num_list) == 2 and len(two_num_list) == 0 and len(three_num_list) == 0:
          answer += str(one_num_list.pop())
          answer += str(one_num_list.pop())

        if len(one_num_list) == 0 and len(two_num_list) == 1 and len(three_num_list) == 0:
          answer += str(two_num_list.pop())

    return answer


print(solution(num))

