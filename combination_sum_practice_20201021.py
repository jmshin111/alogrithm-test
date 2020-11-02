candidates = [2,3,6,7]
target = 14

def combination_sum_list(input_candidate_list,input_target):
    result = []


    def dfs_combination_sum_list(input_sum_list,input_target_dfs,current_sum_list):

        temp_sum_list = input_sum_list[:]
        temp_current_sum_list = current_sum_list[:]
        while(len(temp_sum_list)):
            last_digit = temp_sum_list.pop()
            times = 1

            while last_digit <= input_target_dfs :
                if (last_digit == input_target_dfs):
                    for index in range(times):
                        temp_current_sum_list.append(int(last_digit/times))
                    result.append(temp_current_sum_list)
                    temp_current_sum_list = []

                elif (last_digit < input_target_dfs):
                    remain_target = input_target_dfs - last_digit
                    if (temp_sum_list):
                        for index in range(times):
                            temp_current_sum_list.append(int(last_digit/times))

                        dfs_combination_sum_list(temp_sum_list, remain_target, temp_current_sum_list )
                else:
                    break

                times += 1
                last_digit = int((last_digit/(times-1)) * times)
                while last_digit/times in temp_current_sum_list:
                    temp_current_sum_list.remove(last_digit/times)
            temp_current_sum_list = current_sum_list[:]


    input_candidate_list = sorted(input_candidate_list)
    dfs_combination_sum_list(input_candidate_list,input_target, [])


    return result

print(combination_sum_list(candidates , target))