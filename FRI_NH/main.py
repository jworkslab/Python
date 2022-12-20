from calcpkg.geometry import *
from calcpkg.operation import *

num_list = [int(i) for i in input("숫자 입력: ").split()]
cal1 = Geo(*num_list)

print(cal1.rect_area())
print(cal1.tri_area())
print(cal1.circle_area())