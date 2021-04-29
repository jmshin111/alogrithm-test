class MyHashMap:

    hash_map = [-1] * 1000001

    def __init__(self):
        hash_map = [-1]*1000001
        for i in range (1000001):
            MyHashMap.hash_map[i] = -1
        print(MyHashMap.hash_map)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if value == 6:
            print (key)
        MyHashMap.hash_map[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

        if MyHashMap.hash_map[key] == -1:
            return -1
        else:
            return MyHashMap.hash_map[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        MyHashMap.hash_map[key] = -1


# Your MyHashMap object will be instantiated and called as such:
hashMAp = MyHashMap()
import array
verts=array.array('i',(0,)*1000)
print(verts)