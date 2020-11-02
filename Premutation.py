num_list =[1,2,3,4]
result = []

def permutation(input_str, input_num_list):
    if len(input_num_list) == 1 :
        input_str += str((input_num_list[0]))
        temp_list = []
        for index_str in input_str:
            temp_list.append(int(index_str))
        result.append(temp_list)
        return

    for index_input_num_list in range(len(input_num_list)):
        output_num_list = input_num_list[:]
        output_num_list.remove(input_num_list[index_input_num_list])

        #input_str.append(input_num_list[index_input_num_list])

        permutation(input_str+str(input_num_list[index_input_num_list]),output_num_list)

        # for index_input_num_list_for_output in range(len(input_num_list)):
        #     if index_input_num_list != index_input_num_list_for_output:
        #         output_num_list.append(input_num_list[index_input_num_list_for_output])

permutation('',num_list)
print(result)
print(len(result))