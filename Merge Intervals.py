test_data = [[2,5],[3,6],[1,2],[6,8],[9,12],[2,4],[13,20],[25,26],[29,31],[30,32]]

def merge_intervals(i_list:[]):

    result = []
    for i_element in sorted(i_list, key=lambda x: x[0]):

        if result and i_element[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1],i_element[1])
        else:
            result.append(i_element)

    return result


print(merge_intervals(test_data))

