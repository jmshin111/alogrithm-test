paragraph = "Bob hit a ball, the hit BALL flew after it was hit"
banned = ["hit"]


def str_validation_check(input_str, banned_str):
    # change all string to lowercase
    input_str = input_str.lower()

    # remove ,
    input_str = input_str.replace(',', "")

    for index_banned in banned_str:
        print('index_banned : ' + index_banned)
        input_str = input_str.replace((str(index_banned) + " "), "")
        input_str = input_str.replace( " "+ (str(index_banned)), "")
        input_str = input_str.replace(str(index_banned), "")


    print (input_str)
    # for index in input_str.split(' '):
    #      print(index)
    return input_str.split(' ')

def str_dictionary_insert(input_str):
    str_dictionary = {}
    for index_str in input_str:
        if str_dictionary.has_key(index_str) :
            str_dictionary[index_str] = (str_dictionary[index_str])+1
        else :
            str_dictionary[index_str] = 1

    return str_dictionary
def f(x):
    return x[1]

str_validation_finished = str_validation_check(paragraph, banned)

print(str_validation_finished)
calculation_finished_dic = str_dictionary_insert(str_validation_finished)
print(calculation_finished_dic)

print(sorted(calculation_finished_dic.items(), key=f))
# for index_dictionary in :
#     print(index_dictionary)
