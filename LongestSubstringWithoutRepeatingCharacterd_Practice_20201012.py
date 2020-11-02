
str = "pwwkew"

def solution(input_str):

    result_max_count = 0
    max_count = 0
    duplicated_hash_key = {}

    for index_inpus_str in range(len(input_str)):

        if( not input_str[index_inpus_str] in duplicated_hash_key):
            duplicated_hash_key[input_str[index_inpus_str]] = 1
            max_count += 1

            if(index_inpus_str == len(input_str)-1):
                if result_max_count < max_count:
                    result_max_count = max_count

        else:
            if result_max_count < max_count:
                result_max_count = max_count
            max_count = 0
            duplicated_hash_key = {}

    return result_max_count



print(solution(str))