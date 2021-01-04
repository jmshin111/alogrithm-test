num_list = [2,8,7,1,3,5,6,4]

# def merge_sort(i_num_list, start, end):
#     if(len(i_num_list)==1):
#         return i_num_list[0]

def split(i_num_list, start, end):
    if(start==end):
        return [i_num_list[start]]

    return merge(split(i_num_list,start,int(end/2)),split(i_num_list,int(end/2)+1,end))


def merge(a:[],b:[]):
    result = []

    while(len(a) > 0 or 0 < len(b)):
        if(len(a)== 0 and len(b)!= 0):
            result.append(b.pop(0))
            continue
        if(len(a) != 0 and len(b)== 0):
            result.append(a.pop(0))
            continue
        if(a[0] > b[0]):
            result.append(b.pop(0))
            continue
        else:
            result.append(a.pop(0))
    return result

split(num_list,0,len(num_list))
print(num_list)

