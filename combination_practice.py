#n = 4 , k = 2



def combination_practice(input_num_list, input_k):
    result = []

    def dfs(input_dfs_num_list, input_dfs_k):

        temp_result = []
        dfs_result = []
        if(len(input_dfs_num_list) == 1 ):
            return input_dfs_num_list[0]

        if(input_dfs_k == 1):
            for index_input_dfs_num_list in input_dfs_num_list:
                temp_result.append([index_input_dfs_num_list])
            return temp_result

        first_digit_letter = input_dfs_num_list.pop(0)
        temp_dfs_result = dfs(input_dfs_num_list, input_k - 1)
            for index_temp_result in temp_dfs_result:

                index_temp_result.append(index_input_dfs_num_list)

        # for index_input_dfs_num_list in input_dfs_num_list:
        #     input_parameter_dfs_num_list = input_dfs_num_list[:]
        #     input_parameter_dfs_num_list.remove(index_input_dfs_num_list)
        #     temp_dfs_result = dfs(input_parameter_dfs_num_list,input_k-1)
        #     for index_temp_result in temp_dfs_result:
        #
        #         index_temp_result.append(index_input_dfs_num_list)

        return temp_dfs_result
    result = dfs(input_num_list,input_k)
    return result

n = 4
k = 2

num_list = []
for index in range(n):
    num_list.append(index+1)

print( combination_practice(num_list,k) )