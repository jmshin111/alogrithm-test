tel_num = '23'

dic = { "2":"abc", "3": "def", "4": "ghi","5":"jki","6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
result =[]

def letter_combination_phone_number_recursive(appended_characted ,input_tel_num):


    if(len(input_tel_num)==1):
        for index_characted_input_tel_num in dic[input_tel_num]:
            result.append(appended_characted+index_characted_input_tel_num)
        return

    first_input_tel_num = input_tel_num[0]
    input_tel_num = input_tel_num[1:]
    for index_characted_input_tel_num in dic[first_input_tel_num]:
        letter_combination_phone_number_recursive(appended_characted+index_characted_input_tel_num,input_tel_num)



letter_combination_phone_number_recursive('', tel_num)
print(result)





