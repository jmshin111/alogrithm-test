A = [2, 3, 3, 4]
L = 3
R = 1


A = [1, 4, 5, 5]
L = 6
R = 4


A = [5, 2, 5, 2]
L = 8
R = 1

A = [1, 5, 5]
L = 2
R = 4


A = [7]
L = 7
R = 7


A = [3]
L = 2
R = 6

A = [3,4,5,6,7,7,7,7,4]
L = 4
R = 4


import heapq

def solution(A, L, R):
    # write your code in Python 3.6
    h = []

    for i in A:
        heapq.heappush(h,i)

    l_list = []
    r_list = []
    rest_list = []

    l_key = set()
    r_key = set()

    while h:
        next_val =  heapq.heappop(h)

        if next_val >= L:
            rest_list.append(next_val)
            break

        if next_val not in l_key:
            l_list.append(next_val)
            l_key.add(next_val)
        else:
            rest_list.append(next_val)

    print('L',len(l_list),l_list)

    for i in rest_list:
        if R < i and i not in r_key:
            r_key.add(i)
            r_list.append(i)

    while h:
        next_val = heapq.heappop(h)

        if next_val <= R:
            continue

        if next_val not in r_key:
            r_list.append(next_val)
            r_key.add(next_val)
    print('R', len(r_list), r_list)

    return len(l_list)+len(r_list)


print(solution(A,L,R))