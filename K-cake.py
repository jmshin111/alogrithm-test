import heapq

N = 5
K = 1
A = [1, 1, 4, 1, 4]
B = [5, 2, 5, 5, 4]
C = [1, 1, 1, 1, 1]
# 0 , Pass

N = 5
K = 3
A = [1, 1, 4, 1, 4]
B = [5, 2, 5, 5, 4]
C = [1, 1, 1, 1, 1]

# 0 , Pass


N = 5
K = 4
A = [1, 1, 4, 1, 4]
B = [5, 2, 5, 5, 4]
C = [2, 1, 3, 4, 2]

#0, Pass
N = 5
K = 4
A = [1, 1, 4, 1, 4]
B = [5, 2, 5, 5, 4]
C = [1, 2, 3, 4, 4]


N = 5
K = 3
A = [1, 1, 4, 1, 4]
B = [5, 2, 5, 5, 4]
C = [1, 2, 2, 3, 3]

def solution(N, K, A, B, C):
    # write your code in Python 3.6

    h =[]

    for i in range(0,len(C)):
        heapq.heappush(h,(C[i],i))

    result = []
    before_level = 0

    while h:
       next_node =  heapq.heappop(h)

       next_val =next_node[0]
       next_index = next_node[1]

       if before_level != next_val:

           if  next_val ==1 and len(result)==0:
               result = [[A[next_index],B[next_index]]]

           else:

               for i_range in range(0,len(result)):

                   if result[i_range][0] > B[next_index]:
                       result.pop(i_range)


                   elif result[i_range][1] < A[next_index]:
                       result.pop(i_range)


                   else:
                       result.append([max(result[i_range][0],A[next_index]),min(result[i_range][1],B[next_index])])
                       result.pop(i_range)

           if len(result)==0:
               return 0
       else:
           for i_range in  range(0,len(result)):

               if result[i_range][0] > B[next_index]:
                    if next_val ==1:
                        result.append([A[next_index],B[next_index]])

               elif result[i_range][1] < A[next_index]:
                   if next_val == 1:
                        result.append([A[next_index], B[next_index]])

               else:
                   if A[next_index] <= result[i_range][0] and result[i_range][1] <= B[next_index]:
                       continue

                   elif A[next_index] > result[i_range][0] and result[i_range][1] > B[next_index]:
                       result.append([result[i_range][0] , A[next_index] - 1])
                       result.append([B[next_index] + 1], result[i_range][0])

                   elif  B[next_index] < result[i_range][1] :
                       result.append([B[next_index]+1,result[i_range][1]])

                   elif result[i_range][0] < A[next_index]:
                       result.append([result[i_range][0],A[next_index]-1])


                   result.pop(i_range)

       before_level = next_val

    print(result)
    count = 0
    for i in result:
        count +=(i[1]-i[0])+1

    return count

print(solution(N,K,A,B,C))



