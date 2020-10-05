num = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#num = ["img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

# answer 1 [2,1,3,4,1]	[2,3,4,5,6,7]
# answer 2 [5,0,2,7]	[2,5,7,9,12]

def solution(files):
    answer = []
    file_list = []
    number = 0

    for index_files in files:
        number = number+1
        temp_file_name = ''
        temp_digit = ''
        temp_full_filename = ''
        end_file_name = False
        zero_digit_skip = False

        for index_file in range(len(index_files)):
            # find alpha and change uppper
            if not end_file_name and index_files[index_file].isalpha():
                temp_file_name += index_files[index_file].upper()
            elif not zero_digit_skip and index_files[index_file].isdigit() and '0' == index_files[index_file]:
                continue

            elif zero_digit_skip and index_files[index_file].isdigit() and '0' == index_files[index_file]:
                temp_digit += index_files[index_file]

            elif index_files[index_file].isdigit() and 0 < int(index_files[index_file]) < 10:
                end_file_name = True
                zero_digit_skip = True
                temp_digit += index_files[index_file]

            else:
                break


        zero_temp = ''
        for index in range(5-len(temp_digit)):
          zero_temp +='0'

        temp_full_filename = temp_file_name+zero_temp+temp_digit+'_'+ str(number)
        file_list.append(temp_full_filename)

    file_list = sorted(file_list)

    for index_file_list in file_list:
        answer.append(files[int(index_file_list.split('_')[1])-1])

    return answer


print(solution(num))
