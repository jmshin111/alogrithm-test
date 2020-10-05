str = "Zbcdefg"



def array_partiotion(str):
    str_list = []

    for index in str:
        str_list.append(index)

    str_list= sorted(str_list,reverse=True)


    return  ''.join(str_list)






print(array_partiotion(str))