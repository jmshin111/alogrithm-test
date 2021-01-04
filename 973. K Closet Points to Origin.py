points = [[3,3],[5,-1],[-2,4]]
k=2

def get_point_distance(i_points, k):
    return sorted(i_points,key= lambda x : (x[0]*x[0]+x[1]*x[1])**0.5)[:k]



print(get_point_distance(points,k))





