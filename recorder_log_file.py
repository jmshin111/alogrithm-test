logs = ['dog1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 pwm kit dig', 'let3 art zero']

# init logs two part(digit, letter)
logs_digit = []
logs_letter = []

def compare_log_list(log_str1, log_str2):
    result = True

    log_str1_split = log_str1.split(' ')
    log_str2_split = log_str2.split(' ')

    string_comapre_result = False

    for i in range(len(log_str1_split)):
         if(log_str1_split[i] == log_str2_split[i]):
             string_comapre_result = True
             break

    index_comapre_result = False

    if string_comapre_result :
      if (int(log_str1_split[0][2::])> int(log_str2_split[0][2::])):
          index_comapre_result = True

    #return true SWAP
    #return false Not SWAP

    #Case Different Log --> SWAP
    if (not string_comapre_result and not index_comapre_result):
        return True
    #Case Different Log --> SWAP
    elif (not string_comapre_result and index_comapre_result):
        return True
    #Case Same Log, Compare Index. In Case Left Index is more big than right index. --> SWAP
    elif (string_comapre_result and index_comapre_result):
        return True
    # Case Same Log, Compare Index. In Case Right Index is more big than left index. --> SWAP
    elif (string_comapre_result and not index_comapre_result):
        return False

def sort_order_by_log(logs):

    for i in range (len(logs)):
        for j in range(i-1):
            if compare_log_list(logs[j],logs[j+1]):
                temp_list = logs[j+1]
                logs[j + 1] = logs[j]
                logs[j] = temp_list



# More efficient code >>>> my code
# for logs_index in logs:
#    print(logs_index.split()[1])


#
for logs_index in logs:
    temp_logs = logs_index.replace(" ", "")[5::]
    if temp_logs.isdigit():
        logs_digit.append(logs_index)
    else:
        logs_letter.append(logs_index)

for logs_index in logs_digit:
    print('digit logs ' + logs_index)

for logs_index in logs_letter:
    print('letter logs ' + logs_index)

sort_order_by_log(logs_letter)
for i in logs_letter+logs_digit :
    print('Final Result ' + i)



