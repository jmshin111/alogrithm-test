
num_list = [2,8,7,1,3,5,6,4]

def partition(i_num_list,lo,hi):
    pivot = i_num_list[hi]
    left = lo

    for right in range(lo,hi):
        if i_num_list[right] < pivot:
            i_num_list[right],i_num_list[left] = i_num_list[left],i_num_list[right]
            left = left+1
    i_num_list[left], i_num_list[hi] = i_num_list[hi], i_num_list[left]
    return left





def quicksort(i_num_list,lo,hi):
    if lo < hi:
        pivot = partition(i_num_list,lo,hi)
        quicksort(i_num_list,lo,pivot-1)
        quicksort(i_num_list,pivot+1,hi)

quicksort(num_list,0,len(num_list)-1)
print(num_list)