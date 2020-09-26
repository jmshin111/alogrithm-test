input_str = '1123432121'


# def find_longest_palindrom(input_str):
#     stack = [1]
#     result = []
#
#     for index_input_str in range(len(input_str)):
#         sub_index = 1
#
#         while sub_index <= index_input_str and index_input_str + sub_index < len(input_str):
#
#
#             if sub_index ==1 and (input_str[index_input_str - sub_index] == input_str[index_input_str + sub_index]):
#                 sub_index = sub_index + 1
#                 if sub_index >= index_input_str and index_input_str + sub_index >= len(input_str):
#                     result.append([sub_index - 1, index_input_str])
#                 continue
#             elif sub_index == index_input_str or input_str[index_input_str - sub_index] != input_str[index_input_str + sub_index]:
#                 if sub_index >1:
#                     result.append([sub_index - 1, index_input_str])
#                 break
#
#
#
#
#             sub_index = sub_index + 1
#
#     max_index = -1
#     max_length = -1
#     for index_result in range(len(result)):
#         if max_length < result[index_result][0]:
#             max_index = result[index_result][1]
#             max_length = result[index_result][0]
#
#     return input_str[(max_index - max_length):(max_index + max_length)+1]

def find_longest_palindrom(input_str):
    stack = [1]
    result = []

    for index_input_str in range(len(input_str)):
        sub_index = 1

        while sub_index <= index_input_str and index_input_str + sub_index < len(input_str) and \
                (input_str[index_input_str - sub_index] == input_str[index_input_str + sub_index]):
            sub_index = sub_index + 1

        if(sub_index > 1):
            result.append([sub_index - 1, index_input_str])






    max_index = -1
    max_length = -1
    for index_result in range(len(result)):
        if max_length < result[index_result][0]:
            max_index = result[index_result][1]
            max_length = result[index_result][0]

    return input_str[(max_index - max_length):(max_index + max_length)+1]
print(find_longest_palindrom(input_str))
