import collections
from typing import List

#people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
#Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]


#people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
people = [[2,4],[3,4],[9,0],[0,6],[7,1],[6,0],[7,3],[2,5],[1,1],[8,0]]
#Output : [[6,0],[1,1],[8,0],[7,1],[9,0],[2,4],[0,6],[2,5],[3,4],[7,3]]

#Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
class Solution:

    def makeList(self, i_people: List[List[int]])-> List[List]:

        new_people = []
        for i in range(2001):
            new_people.append([])

        for i in i_people:
            new_people[i[1]].append(i[0])

        for i in new_people:
            if(len(i)>0):
                i.sort(reverse=True)

        return new_people

    def find_next_heigh(self,current_index,sorted_people,min,skip):
        if( len(sorted_people[current_index])>0 and (min >= sorted_people[current_index][-1] or skip )):
            return [sorted_people[current_index].pop(),current_index]
        else:
            return Solution.find_next_heigh(self,current_index-1,sorted_people,min,True)

    def find_next_heigh_using_counter(self,current_index,sorted_people,counter:{}):
        temp_index = current_index
        while(temp_index >=0):
            if( len(sorted_people[temp_index]) >0 ):
                temp_val = sorted_people[temp_index][-1]
                temp_sum = 0

                for i in counter:
                    if i >= temp_val:
                        temp_sum += counter[i]

            if( temp_sum >= temp_index):
                break
            temp_index -=1

        return [sorted_people[temp_index].pop(),temp_index]


    def counter_set(self,counter:{},val):
        if val in counter:
            counter[val] +=1
        else:
            counter[val] = 1


    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        result = []
        sorted_people = (Solution.makeList(self,people))
        index = 0
        minimum = 1000000

        counter ={}


        while(True):
            if(index >= len(people)):
                break
            next_height_val = Solution.find_next_heigh_using_counter(self,index,sorted_people,counter)
            result.append(next_height_val)

            Solution.counter_set(self,counter,next_height_val[0])

            counter = sorted(counter)

            #minimum = min(minimum, next_height_val[0])
            index += 1

        return result


print(Solution.reconstructQueue(Solution,people))



