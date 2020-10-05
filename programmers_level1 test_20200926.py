num = [5,0,2,7]

#answer 1 [2,1,3,4,1]	[2,3,4,5,6,7]
#answer 2 [5,0,2,7]	[2,5,7,9,12]

def array_partiotion(num):

    result = []
    num = sorted(num)
    before_num = -1

    for index_num in range(len(num)):
       # if int(num[index_num]) == before_num:
        #    continue
        for index2_num in range(len(num)):
            if(index2_num<=index_num):
                continue
            result.append(num[index_num]+num[index2_num])

        #before_num = num[index_num]


    result_set = set(result)  # 집합set으로 변환
    result = list(result_set)  # list로 변환
    print(sorted(result))

    return result






print(array_partiotion(num))