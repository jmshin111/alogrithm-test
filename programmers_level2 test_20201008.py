import time
# 1


num = [ 4, 4, 4, 5, 0, 1, 2, 3]

def solution(citations):
    answer = ''

    numbers = sorted(citations,reverse=True)

    for index_numbers in range(len(numbers)-1):

        term = numbers[index_numbers] - numbers[index_numbers+1]+1

        for index_c in range(term):
            target_index = numbers[index_numbers] - index_c
            if (index_numbers + 1 >= target_index and len(numbers) - index_numbers - 1 <=  target_index):
                return target_index

    for index_numbers in range(numbers[len(numbers)-1]):
        target_index = numbers[len(numbers)-1] - index_numbers+1
        if (len(numbers) >= target_index) :
            return target_index


    return 0


#print(solution([12, 11, 10, 9, 8, 1]), 5)
#print(solution([6, 6, 6, 6, 6, 1]), 5)
#print(solution([4, 4, 4]), 3)
#print(solution([10, 11, 12, 13]), 4)
print(solution([0, 0, 1, 1]), 1)
#print(solution([0, 1]), 1)
#print(solution([10, 9, 4, 1, 1]), 3)

