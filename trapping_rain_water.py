# coding=utf-8
from pythonds import Stack

water_height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

stack_water_height = Stack()
total_space = 0


def make_stack_water_height(intput_water_height):
    index_intput_water_height = len(intput_water_height)
    for index in intput_water_height[::-1][:(len(water_height) - 1)]:
        temp_list = [index_intput_water_height - 1, index]
        stack_water_height.push(temp_list)
        index_intput_water_height = index_intput_water_height - 1

    print("====  make stacek water height finished ====")


# Stack 생성해서 index_in_input_water와 높이가 같은거 Stack에 넣기 Stack에 넣을 때 X좌표를 넣기
# 가장 위에 있는 x좌표를 가지고와서 넓이 계산하기
# 그다음에는  x좌표 다음번에 x좌표로 출발해서 동일하게 넓이 구하기
# 넓이 구할 때 같은 높이(일직선, 혹은 산 모양은 다 0으로 처리하게 하기)

# def find_space_and_calculate_space(input_water_heigh, input_stack_water_height):
#     print("====  find_space_and_calculate_space started ====")
#     total_space = 0
#     index_cursor = 0
#     width_from_start = 0
#     if not input_stack_water_height.isEmpty():
#         temp_height = input_stack_water_height.pop()
#
#     for index_input_water_height in range(len(input_water_heigh)):
#
#         if width_from_start != 0 and input_water_heigh[index_input_water_height] >= temp_height:
#             print("====  find same height  : " + str(temp_height) + " , started : " + str(
#                 index_input_water_height) + " , ended : " + str(width_from_start) + "====")
#
#             for index_width in range(width_from_start):
#                 index_size = input_water_heigh[index_input_water_height - width_from_start] - input_water_heigh[
#                     index_input_water_height - index_width]
#
#                 print("====  make same space  started_height : " + str(
#                     input_water_heigh[index_input_water_height]) + "ended height : " + str(input_water_heigh[
#                                                                                                index_input_water_height + (
#                                                                                                        index_width + 1)]) * 1 + " ====")
#                 if index_size > 0:
#                     total_space += index_size
#                 print("====  added_space  ====", total_space)
#                 width_from_start = 0
#             if not input_stack_water_height.isEmpty():
#                 temp_height = input_stack_water_height.pop()
#
#         else:
#             width_from_start = width_from_start + 1
#
#     return total_space

def find_space_and_calculate_space(input_water_heigh, input_stack_water_height,total_space):
    #print("====  find_space_and_calculate_space started ====")

    index_input_water_height = 0
    width_from_start = 0
    before_start = 0
    if not input_stack_water_height.isEmpty():
        temp_height = input_stack_water_height.pop()

    while True:

        if width_from_start != 0 and input_water_heigh[index_input_water_height] >= temp_height[
            1] and input_water_heigh[index_input_water_height] >= input_water_heigh[index_input_water_height - width_from_start]:
            # print("====  find same height  : " + str(temp_height[1]) + " current height :   " + str(
            #     input_water_heigh[index_input_water_height]) + " , started : " + str(
            #     index_input_water_height - width_from_start) + " , ended : " + str(index_input_water_height) + "====")

            for index_width in range(width_from_start):
                index_size = input_water_heigh[index_input_water_height - width_from_start] - input_water_heigh[
                    index_input_water_height - index_width]

                # print("====  make same space  started_height : " + str(
                #     input_water_heigh[index_input_water_height - width_from_start]) + " current height : " + str(
                #     input_water_heigh[
                #         index_input_water_height - index_width]) * 1 + " ====")
                if index_size > 0:
                    total_space += index_size
                # print("====  added_space  ====", total_space, index_size)

            # if not input_stack_water_height.isEmpty():
            #     temp_height = input_stack_water_height.pop()
            # else:
            #     make_stack_water_height(water_height[index_input_water_height+1::])
            #     find_space_and_calculate_space(water_height[index_input_water_height+1::], stack_water_height)
            #     break

            width_from_start = 0
            before_start = index_input_water_height
            index_input_water_height = index_input_water_height - 1

        else:
            width_from_start = width_from_start + 1

        index_input_water_height = index_input_water_height + 1

        if not input_stack_water_height.isEmpty() and (index_input_water_height == len(input_water_heigh)  or (temp_height[0] < index_input_water_height)):
            temp_height = input_stack_water_height.pop()
            index_input_water_height = before_start
            width_from_start = 0
        elif index_input_water_height == len(input_water_heigh) and input_stack_water_height.isEmpty():

            if len(input_water_heigh)- before_start > 2:
                make_stack_water_height(input_water_heigh[before_start+1::])
                find_space_and_calculate_space(input_water_heigh[before_start+1::], stack_water_height, total_space)
            break
## Stack을 루프 돌면서 그 높이에 맞는 애들을 리스트에서 찾고 건바이 건으로 높이를 더해주는 로직이 더 효율적임
# def find_space_and_calculate_space(input_water_heigh, input_stack_water_height):
#     print("====  find_space_and_calculate_space started ====")
#     total_space = 0
#     index_cursor = -1
#
#     for index_input_stack_water_height in range(input_stack_water_height.size()):
#
#         temp_height = 0
#         width_from_start = 0
#
#         if not input_stack_water_height.isEmpty():
#             temp_height = input_stack_water_height.pop()
#         else:
#             print("==== height stack is empty ended loop process ====")
#             break
#
#         for index_input_water_height in range(len(input_water_heigh)):
#
#
#             if index_cursor > index_input_water_height:
#                 continue
#
#             if width_from_start !=0 and input_water_heigh[index_input_water_height] >= temp_height:
#
#                 print("====  find stack height  : " + str(temp_height) + " list height " + str(input_water_heigh[
#                                                                                                    index_input_water_height]) + " , started : " + str(
#                     index_input_water_height) + " , ended : " + str(width_from_start) + "====")
#
#                 for index_width in range(width_from_start):
#                     if index_input_water_height + (width_from_start + 1) > len(input_water_heigh):
#                         break
#                     index_size = input_water_heigh[index_input_water_height - width_from_start] - input_water_heigh[index_input_water_height - index_width]
#                     print("====  make same space  started_height : " + str(
#                         input_water_heigh[index_input_water_height]) + " ended height : " + str(input_water_heigh[
#                                                                                                     index_input_water_height + (
#                                                                                                             index_width )]) * 1 + " ====")
#                 if index_size > 0:
#                     total_space += index_size
#
#                 index_cursor = index_input_water_height
#
#                 print("====  added_space  ====", total_space)
#
#                 break
#             else:
#                 width_from_start = width_from_start + 1
#
#     return total_space


def list_test():
    list_temp = list()

    for i in range(5):
        temp = [i + 1, i + 3, i + 5]
        list_temp.append(temp)

    for i in list_temp:
        print(i)


make_stack_water_height(water_height)
find_space_and_calculate_space(water_height, stack_water_height,total_space)
print("☆Total Space :  " + str(total_space))
