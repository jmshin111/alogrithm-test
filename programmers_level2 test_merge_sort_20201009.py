import time
# 1


# num = [3, 6, 30, 34, 5, 9, 7, 95]
num = [3, 30, 34, 5, 9]
# num = [6,7,9,88,99,34,765,342,123,983]
#num = [3, 30, 34, 5, 191]
#num = [12,121]
#num = [987,9,9,9]
import timeit
from datetime import time

#num = [999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1,999,998,997,99,98,97,9,7,8,6,999,998,997,99,98,97,999,998,997,99,98,97,9,7,8,6,5,4,3,2,1,1,1,1,1,1]
# num = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#num = [40,404]

def compare_two_digit(digit1, digit2):
    len_digit1 = len(str(digit1))
    len_digit2 = len(str(digit2))
    str_digit1 = str(digit1)
    str_digit2 = str(digit2)

    if(len_digit1 == len_digit2):
        if digit1 > digit2:
            return True
        else:
            return False
    elif (len_digit1 < len_digit2):
        if int(str_digit2[0:len_digit1]) > digit1:
            return False
        elif int(str_digit2[0:len_digit1]) < digit1:
            return True
        else :
            left_side = int(str_digit1 + str_digit2)
            right_side = int(str_digit2 + str_digit1)

            if left_side >= right_side:
                return True
            else:
                return False

    elif (len_digit1 > len_digit2):
        if int(str_digit1[0:len_digit2]) > digit2:
            return True
        elif int(str_digit1[0:len_digit2]) < digit2:
            return False
        else :
            left_side = int(str_digit1+str_digit2)
            right_side = int(str_digit2+str_digit1)

            if left_side >= right_side:
                return True
            else:
                return False

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    len_left = len(left)
    len_right = len(right)
    while len_left > 0 or len_right > 0:
        if len_left > 0 and len_right > 0:
            if not compare_two_digit(left[0],right[0]) :
                result.append(left[0])
                left = left[1:]
                len_left -= 1
            else:
                result.append(right[0])
                right = right[1:]
                len_right -= 1
        elif len_left > 0:
            result.append(left[0])
            left = left[1:]
            len_left -= 1
        elif len_right > 0:
            result.append(right[0])
            right = right[1:]
            len_right -= 1
    return result

def solution(numbers):
    answer = ''
#    numbers.sort()
    number_list = []
    numbers  = merge_sort(numbers)

    numbers.reverse()
    # last_index = len(numbers)-1
    # for index in range(len(numbers)):
    #     answer += str(numbers[last_index-index])

    answer = ''.join(str(x) for x in numbers)

    return str(int(answer))

print(len(num))
print(solution(num))
