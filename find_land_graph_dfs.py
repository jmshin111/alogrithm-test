
graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

map = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,0,0,1,0],
    [0,0,1,0,1],
]



discovered = []

def find_land():
    land_count = 0
    for index_map_x in range(len(map)):
        for index_map_y in range(len(map[index_map_x])):
            if [index_map_x,index_map_y] in discovered:
                continue
            else:
                result = recursive_dfs_find_land(index_map_x, index_map_y,map[index_map_x][index_map_y])
                if result == 1 :
                    land_count += 1
    return land_count

def recursive_dfs_find_land(index_x_map,index_y_map,land_or_sea):

    if map[index_x_map][index_y_map] == land_or_sea :
        discovered.append([index_x_map,index_y_map])
        print('land or sea : '+str(land_or_sea)+' x : '+str(index_x_map)+' y: '+str(index_y_map) +' is appended')
    else:
        return map[index_x_map][index_y_map]

    temp_x = index_x_map -1
    temp_y = index_y_map -1

    for index_x in range(3):
        for index_y in range(3):
            temp_x += index_x
            temp_y += index_y
            if( 0 <= temp_x and temp_x < len(map) and 0 <= temp_y and temp_y < len(map[0]) ):
                if (not [temp_x,temp_y] in discovered):
                    recursive_dfs_find_land(temp_x,temp_y,land_or_sea)


            temp_x = index_x_map -1
            temp_y = index_y_map -1


    return map[index_x_map][index_y_map]

print(find_land())
